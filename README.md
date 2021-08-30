# Simple-Login-Authentication-System
<h3> This is a simple user login system </h3>
<p></p>
This ia a simple user login system which stores the user info in a text file. To secure the users password I have implemented hashing to store password and users will wil able to reset the password using an OTP sent to their Email ID.
The user info is stored in a nested dictionary of the format in the login_info.txt file
<p></p>

**{unique_id:{'username':'username_of_user','password':'Hashed_Password','details':{"Name":"user_name",'mobile':'user_mobile_no','email id':'user_email_ID',"unique id":Unique ID}}}**

This script also has an admin panel whose credentials are stored in the admin_info.txt file and the admin will be able to reset a users password and to delete a user permanently.

If the script succefully run then the screen will be like

<a href="https://imgbb.com/"><img src="https://i.ibb.co/chvZgKJ/1.png" alt="1" border="0"></a>

In the Existing User Section, If the login is successfull the screen will be like 

<a href="https://imgbb.com/"><img src="https://i.ibb.co/vxSYqzH/2.png" alt="2" border="0"></a>

The admin panel will be like

<a href="https://imgbb.com/"><img src="https://i.ibb.co/L0dyKVL/3.png" alt="3" border="0"></a>

To test this file in your pc first star and fork this repo and clone this into your pc and run the following code

```pip install requirements.txt ```

Install the dependencies using this command 
<p></p>
Note: Correctly Specify the requirements.txt file location

Then you are ready to go and test
