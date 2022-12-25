#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

# To get the register / login inputs from user

user_ip = input("""
1.Press 1 to register: 
2.Press 2 to Login: 
3.Press 3 for Forgot password:
""")
Email_valid = ''
Pwrd_valid = ''
Email_Flag = False
Pwrd_Flag = False
List1=[]


# Make a regular expression
# for validating an Email
User_Reg = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Local variables to check the passwords

Lower,Upper,Digits,Special = 0,0,0,0

if int(user_ip) == 2:
    user = input("Enter Your Username: ")
    if user in List1:
        print("User Exist in the System")
    else:
        print("User Not Exist in the System Pls Go For Registration")
        
if int(user_ip) == 3:
    user = input("Enter Your Username: ")
    if user in List1:
        for user_t in range(len(List1)):
            if user == List1[user_t]:
                print(List1[user_t+1])
    else:
        print("User Not Exist in the System Pls Register yourself")

if int(user_ip) == 1 or (user not in List1) :
    email = input("Enter Your Email: ")

    if(re.fullmatch(User_Reg, email)):
        print("Valid Email")
        Email_valid = email
        Email_Flag = True
        Password = input("Enter your Password: ")
        
        if len(Password) >5 and len(Password) < 16:
            for i in Password:
                if (i.islower()):
                    Lower+=1
                if (i.isupper()):
                    Upper+=1
                if (i.isdigit()):
                    Digits+=1
                if (i=='@' or i=='#' or i =='$' or i =='!' or i =='&' or i =='_' or i=='%' or i =='-'):
                    Special+=1
            if (Lower>= 1 and Upper >=1 and Digits >=1 and Special >=1) :
                    print("Registererd Succesfully")
                    Pwrd_valid = Password
                    Pwrd_Flag = True
            else:
                print("Invalid password")
        else:
                print("Invalid password")
 
    else:
        print("Invalid Email")

List_Usernames = []        
if Email_Flag and Pwrd_Flag:
    File_open = open("Assignments1.txt",'a')
    File_open.write('\n'+f'{Email_valid}')
    File_open.write('\n'+f'{Pwrd_valid}')
    File_open.close
    
File = open("Assignments1.txt",'r') 
test = File.read()
List1 = test.split()






# In[ ]:





# In[ ]:




