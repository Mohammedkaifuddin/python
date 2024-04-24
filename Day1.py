'''
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
if(a>b):
    print("{} is greater than {}".format(a,b))
else:
    print("{} is less than {}".format(a,b))'''

'''
age1 = int(input("Enter the age 1 : "))
age2 = int(input("Enter the age 2 : "))
if(age1>age2):
    age3=age1+age2
    print("my age added",age3)
else:
    age3=age1-age2
    print("my age subtract",age3)'''

'''
email = 'abc@gmail.com'
password = 'abc@123'
eemail=str(input("Enter the email id  : "))
epassword = str(input("Enter the password : "))

if(email==eemail and password==epassword):
    print("login in successful!")
else:
    print("login in failed")'''


'''
email = 'abc@gmail.com'
password = 'abc@123'
eemail = str(input("Enter the email id  : "))
epassword = str(input("Enter the password : "))

if(email == eemail):
    if(password == epassword):
        print("login successful")
        otp=int(input("Enter the otp : "))
        if(otp==12345):
            print("Transaction successful!")
        else:
            print("Transaction failed,due to incorrect otp")
    else:
        print("login failed,due to incorrect password")
else:
    print("login failed,due to incorrect email id")'''


'''
num1 = int(input("Enter the value num1 : "))
num2= int(input("Enter the value num1 : "))
if (num1 == num2):
    print(num1,"is equal to ",num2)
else:
    if(num1>num2):
        print(num1," is greater")
    else:
        print(num2," is greater")'''

num1 = int(input("Enter the value num1 : "))
num2= int(input("Enter the value num2 : "))
if(num1>num2):
    print(num1," is greater")
elif(num1 == num2):
    print(num1," is equal to ",num2)
else:
    print(num2," is greater")
        
