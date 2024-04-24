import random
import time
from datetime import date
'''
abc=[]
n=int(input('Enter the list size : '))
for i in range(0,n):
    ele=int(input('Enter the elements : '))
    abc.append(ele)
print(abc)
'''

'''

a=[10,20,30,40,50]
b=[60,70,80,90,100]
c=a+b
print(c)
print(type(a))
print(type(b))
print(type(c))
print(c*2)
print(len(c))
print(max(c))
print(min(c))
'''

'''
a=[10,25,37,40,57,65]
sum=0
for i in a:
    if i%10==7:
        print(i)
        sum=sum+i
        time.sleep(1)
print(sum)
'''

'''
abc=[10,20,30,40,50,30,50]
ef=[]
for i in abc:
    if i not in ef:
        ef.append(i)

print(ef)
'''

'''

abc=[]
n=int(input('Enter the abc list size : '))
for i in range(0,n):
    ele=int(input('Enter the elements : '))
    abc.append(ele)
print(abc)
time.sleep(1)
ef=[]
n=int(input('Enter the ef list size : '))
for i in range(0,n):
    ele=int(input('Enter the elements : '))
    ef.append(ele)
print(ef)
time.sleep(1)
for i in abc:
    for j in ef:
        if i==j:
            print(i)
'''

'''
for i in range(-10,10,2):
    print(i+1)
'''

'''
a=[2004,1996,17,10,85]
print('leap year : ',end=' ')
for i in a:
    if i%4==0:
        print(i,end=' ')

print()
print('prime number : ',end=' ')
for i in a:
     if i%i==0 and i%1==0:
         print(i,end=' ')
'''

'''
numbers = [10,20,30,40,50]
double_number = []
double_numbers = [num*2 for num in numbers]
print(double_numbers)


numbers = [10,20,30,40,50]
square_number = []
square_numbers = [num*num for num in numbers]
print(square_numbers)
'''

#conditional comprehension
#[expression for item in list if condition == True]
'''
even_numbers = [num for num in range(1,10) if num%2==0]
print(even_numbers)
print(type(even_numbers)) '''

#finding the vowels from the word
'''
word = 'abcdef'
vowels = 'aaeiou'
#find vowel in the string 'abcdef'
res = [char for char in word if char in vowels]
print(res)'''

'''

state = {'A','B','C','D','E'}
print(state)
print(type(state))
print("looping through the set elements...")
for i in state:
    print(i)
'''
'''

set3 = set([10,20,30,40,50])
print(set3)

set3.add(100)
print(set3)

set3.update([110,120])
print(set3)
set3.discard(100)#if element is not in set than it shows error
print(set3)

set3.remove(110) #if element is not in set than it shows error
print(set3)

set3.pop()
print(set3)

set3.clear()
print(set3) #it is used to clear the set
'''

'''
set1 = {1,2,3}
set2 = {2,3,4}
set3 = {3,4,5}
common = set1.union(set2,set3)
print(common)'''

'''
set1 = {1,2,3}
set2 = {2,3,4}
set3 = {3,4,5}
common_in_all = set1.intersection(set2,set3)
print(common_in_all)'''


'''

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.difference(set2))'''

'''

a = {1,2,3,4}
b = {1,2,4,5}
c = a^b
print(c)

c = a.symmetric_difference(b)
print(c)
'''
'''
set1 = {1,2,3,4}
set2 = {1,2}
set3 = {1,2,3}

#set1 is the superset of set2 hence it will print true
print(set1>set2)#true
#prints false since set1 is not subset of set2
print(set1<set2)#false
#prints false since set2 and set13 are not equivalent
print(set2==set3)#false'''