#this file for console app registeration and login
# To get users/projects data
# Assume each first line in file for metadata 
# Actual data start from second line
import general
import os
import re
# this file to store users data
USERS_FILE = "users.txt"

# validate phone =>  Egyptian phone number format
def validate_phone_number(phone_number):
    pattern = "^01[0-2|5][0-9]{8}$"
    return bool(re.match(pattern, phone_number))

# Validate email 
def validate_email(email):
    pattern = "^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{3,}$"
    return bool(re.match(pattern, email))

# Validate password confirmission
def validate_password(password,conf_password):
    return password == conf_password

# ckeck if user exists
def ckeck_user(id,email):
        if os.path.exists('projects.txt'):
            with open('users.txt', 'r') as file:
             for line in file:
                fields = line.strip().split(':')
                if  fields[0] == id and fields[3] == email:
                    return True
                # print(fields[0],fields[3])        
            file.close()             
        else:
            with open('projects.txt',"a") as file:
             pass
            file.close()    

# register new user
def register():
    # 1- get user inputs
        # Get user information
    id = input("Enter your id: ")
    while not general.validate_id(id):
        print("Re-enter id  ")
        id = input("Enter your id: ")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Re-enter email  ")
        email = input("Enter your email: ")
    # 
    if ckeck_user(id,email):
        print(f"User with id {id} and email {email} Already exists..")
        return
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    while not validate_password(password,confirm_password):
        print("Re-enter password ")
        password = input("Enter your password: ")
        print("Re-enter confirm password  ")
        confirm_password = input("Enter your confirm password: ")
    phone = input("Enter your mobile phone number: ")
    while not validate_phone_number(phone):
        print("Re-enter phone")
        phone = input("Enter your phone: ")



    # now save new user
    data=f"{id}:{f_name}:{l_name}:{email}:{phone}:{password}:{confirm_password}"
    record="id:fname:lname:email:phone:password:confirmpassword"+"\n"
    general.save('users.txt',data,record)    
    print("User Scssfully Saved, now you can login...")

# Login
def login():
     # 1 get user data
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    while not check_login(email,password):
         print("Error Email or Password")
         email = input("Enter your email address: ")
         password = input("Enter your password: ")                
         check_login(email,password)
    else:
        # 
        print(f"Welcome ....")
        os.system("python3 menu.py")
def check_login(email,password):
      with open('users.txt', 'r') as file:
            for line in file:
                fields = line.strip().split(':')
                if  fields[3] == email and fields[5] == password:
                    return True
      file.close()   
     
   