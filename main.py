import json
import uuid
import random
import smtplib
import re
from bcrypt import *

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

try:
    login_info={}
    file=open('C:/Users/ashwi/Desktop/Python Programs/Password/new.txt', 'r')
    login=file.read()
    login_info=json.loads(login)
    file.close()
except:
    print("Something Wrong with File Opening")


#Email Credentials
MY_EMAIL= 'sqlmy321@gmail.com'
PASSWORD = 'As@123456'

#Function to produce a Four Digit OTP
def otp():
    return random.randint(1111,9999)

#Function to send otp to email and authenticate
def email_auth(email, password, receiver):
    MY_EMAIL = email
    PASSWORD = password
    reciever = receiver
    t_otp=otp()
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(MY_EMAIL,PASSWORD)

        subject = 'Password Reset'
        body = 'You OTP is: ' + str(t_otp)

        msg = f'Subject: {subject} \n\n{body}'

        smtp.sendmail(MY_EMAIL, reciever, msg )
        print("OTP Sent to you Mail Id", reciever)

    user_otp=int(input("Enter Otp:"))
    if user_otp == t_otp:
        return True
    else:
        return False

#Function to send email after creation
def email_after(email,password,receiver,username,u_password,mobile,unique):
    MY_EMAIL = email
    PASSWORD = password
    reciever = receiver

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(MY_EMAIL,PASSWORD)

        subject = 'Account Created !!!'
        body = '''Your Account is Successfully created with Us 

        Username: {}

        Password: {}

        Mobile No: {}

        Unique ID: {}

        Thank you'''.format(username,u_password,mobile,unique)

        msg = f'Subject: {subject} \n\n{body}'

        smtp.sendmail(MY_EMAIL, reciever, msg )
        print("All Details Sent to your Mail ID", reciever)
    


#Function to produce unique ID
def file_opening_uniqueID():
    file=open('C:/Users/ashwi/Desktop/Python Programs/Password/unique1.txt', 'r')
    uni=file.read()
    uni_info=json.loads(uni)
    return uni_info

def main_unique_id(uni_info):
    def ran():
        return random.randint(111111,999999)

    uni_gen = 0
    Count= 0
    a= True
    while a:
        uni_gen = ran()
        if Count>999999:
            print("All Numbers Used")
            break
        if uni_gen in uni_info:
            uni_gen = ran()
            Count +=1
        else:
            uni_info.append(uni_gen)
            a=False
            return uni_gen

def file_closing_uniqueID(uni_info):
    with open('C:/Users/ashwi/Desktop/Python Programs/Password/unique1.txt', 'w') as convert_file:
        convert_file.write(json.dumps(uni_info))

def unique_id():
    uni_info = file_opening_uniqueID()
    uni_gen=main_unique_id(uni_info)
    file_closing_uniqueID(uni_info)
    return uni_gen

#Function to save the dict to txt file
def saving_file():
    try:
        with open('C:/Users/ashwi/Desktop/Python Programs/Password/new.txt', 'w') as convert_file:
            convert_file.write(json.dumps(login_info))
        file.close()
        return True
    except:
        print("Something wrong with file saving...")

#Login Function
def login(username,password):
    password = password.encode('ASCII')
    for i in login_info.values():
        if i['username'] == username:
            if checkpw(password , i['password'].encode('ASCII')):
                print()
                print("Welcome",i['details']['Name'] )
                print()
                print('Your Profile Deatils')
                print()
                print('Unique Profile ID:', i['details']['Unique ID'])
                print("Mobile NO:",i['details']['Mobile'])
                print("Email ID:", i['details']['Email ID'] )
                print()
                print("1. Change password")
                print("2. Change Mobile")
                print("3. Change E-Mail")
                print("4. DELETE PROFILE")
                print("5. Logout")
                after_login = int(input())
                if after_login==1:
                    for i in login_info.values():
                        new_password= hashpw(input("Enter New password:").encode('ASCII'),gensalt()).decode('ASCII')
                        i['password']=new_password
                        if saving_file():
                            print("Change Successfull")
                        else:
                            print("Try Again #Password change error")
                elif after_login==2:
                    for i in login_info.values():
                        new_mobile = int(input("Enter New Mobile NO:"))
                        i['details']['Mobile']= new_mobile
                        if saving_file():
                            print("Change Successfull")
                        else:
                            print("Try Again #Mobile NO Change error")
                elif after_login==3:
                    for i in login_info.values():
                        new_email = input("Enter New E-Mail:")
                        otp_result=email_auth(MY_EMAIL,PASSWORD,new_email)
                        if otp_result:
                            i['details']['Email ID']= new_email
                            if saving_file():
                                print("Change Successfull")
                            else:
                                print("Try Again #Email Change error")
                elif after_login==4:
                    unique_del=i['details']['Unique ID']
                    otp_result=email_auth(MY_EMAIL,PASSWORD,i['details']['Email ID'])
                    if otp_result:
                        del login_info[unique_del]
                        if saving_file():
                            print("Profile Deleted!! :(")
                        else:
                            print("Try Again #Profile Deletion error")   
                elif after_login==5:
                    print('Bye!!')
                    exit()

#Function to create a user
def create_user(name,mobile,email,user,passw):
    user_duplicate = False
    passw= hashpw(passw.encode('ASCII'),gensalt()).decode('ASCII')
    if login_info == {}:
        user_duplicate = True
    else:
        for i in login_info.values():
            if i['username']==user:
                print("Username Already Exists!!")
                user_duplicate = False
                break
            else:
                user_duplicate = True
    if user_duplicate:
        unique=str(unique_id())
        otp_result = email_auth(MY_EMAIL,PASSWORD,email)
        if otp_result:
            login_info[unique]={'username':user,'password':passw,'details':{'Name':name,'Mobile':mobile,'Email ID':email,'Unique ID':unique}}
        else:
            print("Wrong OTP")
        if saving_file():
            print("User Succesfully Added!!!")
            print("Your Unique Profile ID is:",unique)
    return unique

#Admin login function
def admin(admin_u,admin_p):
    try:
        admin_info={}
        file_a=open('C:/Users/ashwi/Desktop/Python Programs/Password/admin_info.txt', 'r')
        admin=file_a.read()
        admin_info=json.loads(admin)
        file_a.close()
    except:
        print("Error With Admin File")
    admin_p = admin_p.encode('ASCII')
    if admin_u == admin_info['admin']['username']:
        if checkpw(admin_p,admin_info['admin']['password'].encode('ASCII')):
            print("Login Successfull!!")
            print()
            print('1. Print All Users')
            print('2. Delete a User')
            print('3. Reset Password for A User')
            uc = int(input())
            if uc==1:
                print(login_info)
            elif uc==2:
                print()
                unique_id_admin=input("Enter their Unique ID:")
                del login_info[unique_id_admin]
                if saving_file():
                    print("Profile Deleted!! :(")
                else:
                    print("Try Again #Profile Deletion error")
            elif uc==3:
                def specific_string():  
                    temp_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#%?/' 
                    result = ''.join((random.choice(temp_pass)) for x in range(10))  
                    return result
                print()
                unique_id_admin=input("Enter their Unique ID:")
                temp_pass_user=str(specific_string())
                hash_temp_pass= hashpw(temp_pass_user.encode("ASCII"),gensalt())   
                login_info[unique_id_admin]['password']=hash_temp_pass.decode('ASCII')
                if saving_file():
                    print("Temporary Password for ",login_info[unique_id_admin]['details']['Name'],'is',temp_pass_user)
                else:
                    print("Try Again #Pass reset error")
        else:
            print("Sorry!!! Wrong Admin Password...")
    else:
        print('Sorry!!! Wrong Admin Username...')

#Function to reset forgotten password
def pass_reset(username_reset):
    for i in login_info.values():
        if i['username'] == username_reset:
            otp_result=email_auth(MY_EMAIL,PASSWORD,i['details']['Email ID'])
            if otp_result:
                new_password= hashpw(input("Enter you password:").encode('ASCII'),gensalt()).decode('ASCII')
                i['password']=new_password
                if saving_file():
                    print("Reset Successfull")
                else:
                    print("Try Again #Email Pass Reset error")

def main(n):
    if n==1:
        username = input("Enter Username:")
        password = input("Enter you password:")
        login(username,password)
    elif n==2:
        name=input("Enter your Name:")
        mobile=int(input("Enter your mobile Number:"))
        email=input("Enter Email ID:")
        user=input("Enter your Username:")
        passw=input("Enter you password:")
        if re.fullmatch(regex,email):
            print()
            print("Sending OTP")
            unique = create_user(name,mobile,email,user,passw)
            email_after(MY_EMAIL,PASSWORD,email,user,passw,mobile,unique)
        else:
            print('Invalid Email!!')
    elif n==3:
        admin_u = input("Enter Admin Username:")
        admin_p = input("Enter Password:")
        admin(admin_u,admin_p)
    elif n==4:
        username_reset = input("Enter Your Username:")
        pass_reset(username_reset)
    else:
        print("Wrong Choice")

print("Welcome to User Login System")
print("""
1. Exsisting User
2. Create User
3. Developer Profile 
4. Reset your password""")
user_choice=int(input('Enter Your Choice:'))
main(user_choice)
