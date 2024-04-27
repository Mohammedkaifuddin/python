#Day 11 26/04/2024

'''
def rec(i):
    if(i<=100):
        print(i,end=' ')
        rec(i+1)

rec(1)
'''

'''
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
'''
'''
  
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

txt = "mango planet"

#Check if the string starts with 'hello':

x = re.findall("^mangos", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
  
txt = "hello planet world"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
  
txt = "hellcffgfo planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)

txt = "heo planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)

txt = "hellhho planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{4}o", txt)

print(x)

txt = "The rain in Spain fallses mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "The rain in Spain 125 take care"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 
txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 
txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
   
txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "The rain in Spain 2"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  
txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
'''
#The search() function searches the string for a match, and returns a Match object if there is a match.

#If there is more than one match, only the first occurrence of the match will be returned:
'''

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Mango", txt)
print(x)'''

'''
def binary_search(arr, target):
    """
    Perform binary search on the given sorted array to find the target element.
    
    Args:
    - arr: The sorted array to search in.
    - target: The element to search for.
    
    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If target is not present in the array
    return -1

# Example usage:
#arr = [1, 3, 5, 7, 9, 11, 13]
arr = ['apple','banana','carrot','chennai','zebra']
target = 'chennai'
index = binary_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")'''


'''
def linear_search(arr, target):
    """
    Returns:
    - index: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if target element is not found

# Example usage:
arr = [4, 2, 7, 1, 9, 5]
target = -7
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")'''

#module

import math as m
print(m.pi)

from math import *
print(pi)

import random
random.seed(2)
print(random.random())
print(random.random())
print(random.random())

from module import *
print(add(2,3))
print(sub(5,3))
print(mul(2,3))
print(name)

from module import rec
print(rec(1))

from math import sqrt,factorial
print(sqrt(16))
print(factorial(5))

import sys
print(sys.path)

import math as m
print(m.sqrt(16))

import random
print(random.randint(1,5))

import builtins
print(dir(builtins))

