#practise.py file is also a DAY 2 CLASS PROGRAMS
#DAY 2 CLASS PROGRAMS

'''
a=-5
print(abs(a))
print(pow(2,3))'''

#importing the math package
#and using ceil and floor method
'''
import math
a=math.sqrt(5)
print(a)             #2.23606797749979

print(math.ceil(a))  #3
print(math.floor(a)) #2
print(math.ceil(-5.01)) #-5'''

'''
def function():
    print("python")

function()'''
'''
def add(x,y):
    return x+y

print(add(2,3))'''

'''
def pattern():
    for i in range(1,6):
        for j in range(1,6):
            print('*',end=' ')
        print()

pattern()'''

'''
def even_odd(num):
    if(num%2)==0:
        print("Entered number is even")
    elif(num==0):
        print("Entered number is zero")
    else:
        print("Entered number is odd")

num=int(input("Enter the value of n : "))
even_odd(num)'''

#factorial n numbers
'''
def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(n*fact(n-1))
    
n=int(input("Enter the value of n : "))
print(fact(n))'''


#sum of n natural number
'''
def function(n):
    for i in range(n):
        sum=sum+i
        
n=int(input("Enter the limit : "))
print(function(n))'''


#leap year
'''
def leap_year(year):
    if(year%4)==0:
        print("Entered year is leap year")
    else:
        print("Entered year is not a leap year")

year=int(input("Enter the year : "))
leap_year(year)'''

#checking whether current year is leap year or not
'''
from datetime import datetime
if(datetime.today().year%4)==0:
    print("current year is leap year")
else:
    print("current year is not leap year")'''


import time
import random
from datetime import date
todays_date = date.today()
print("Today's date : ",todays_date)
print()
print("Day : ",time.strftime("%A"))
print()
current_time = time.strftime("%H:%M %p")
print("current time : ",current_time)

time.sleep(random.randint(0,2))

