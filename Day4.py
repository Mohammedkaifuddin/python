# DAY-4 (18/04/2024)


# nested list comprehension
'''

matrix = [[j for j in  range(5)] for i in range(5)]
print(matrix)
'''
'''
intger_input = list(map(int,input('Enter integers separated by space : ').split()))
float_input = list(map(float,input('Enter float separated by space : ').split()))
string_input = list(map(str,input('Enter string separated by space : ').split()))
print(intger_input)
print(float_input)
print(string_input)'''

'''
data = list(map(int,input('Enter integers separated by space : ').split()))
data.extend(list(map(float,input('Enter floats separated by space : ').split())))
data.extend(input('Enter strings separated by space : ').split())
print(data)
'''
'''
Employee = {'Name':'abc','Age':20,'salary':200000,'company':'efg','dob':'2000-10-01'}
print(Employee)
print(type(Employee))

#empty dictionary
Dict = {}
print(Dict)
print(type(Dict))
'''

'''
Employee = {"Name":"abc","Age":20,"salary":200000,"company":"efg"}
print(type(Employee))
print("Name : %s"%Employee["Name"])
print("Age : %d"%Employee["Age"])
print("salary : %s"%Employee["salary"])
print("company : %s"%Employee["company"])'''

'''
Dict = {}
Dict[0] = 'a'
Dict[1] = 'b'
Dict[2] = 'c'
print(Dict)

Dict['age'] = 2,3,4
print(Dict)'''

# getting the input from the user in dict
'''
Employee = {'Name':'abc','Age':20,'salary':200000,'company':'efg'}
print(Employee)

Employee['Name'] = input("Name : ")
Employee['Age'] = input("Age : ")
Employee['salary'] = input("salary : ")
Employee['company'] = input("company : ")

print(Employee)'''

'''
Employee = {'Name':'abc','Age':20,'salary':200000,'company':'efg'}
print(type(Employee))
print(Employee)
del Employee["Name"]
print(Employee)
del Employee
print(Employee)'''

'''
Dict1 =  {1:'abc',2:20,3:200000,4:'efg'}
#pop function used in dict
pop_key = Dict1.pop(2)
print(Dict1)
print()

#for loop to print all the values of the dict
Employee = {'Name':'abc','Age':20,'salary':200000,'company':'efg'}
for x in Employee:
    print(Employee[x])

print()

Employee.pop("Age")
#value key word is used to display the values in dict
for x in Employee.values():
    print(x)

print()
#display the items in the dict
for x in Employee.items():
    print(x)

print()

dict = {7:'z',5:'e',8:'g',1:'b'}
print(sorted(dict))

#it is used to clear
#dict.clear()

#it is used to copy the dict
dict_demo = dict.copy()
#we pop the key 1 element in x
x = dict_demo.pop(1)
print(x)

print(dict_demo)

#keys keyword used to display key value from dict
print(dict.keys())
print(sorted(dict.keys()))

#update() method -> it is used to update the dict
print(dict)
dict.update({5:"a",8:"b"})

print(dict)'''

# names = []
# vowels = 'aeiou'
'''
print(name) #abcdef
print(name[:]) #abcdef
print(name[2:]) #cdef
print(name[-1:]) #f
print(name[-5:-1]) #bcde
print(name[::-1]) #fedcba'''

# res = [char for char in name if char in vowels]
# print(res)
'''
for x in name:
    if(x not in vowels):
        print(x,end = ' ')
'''
'''
for i in range(1,len(name)-2):
    print(name[:i],end='-')'''
# for i in range(0,len(name)):
#   print(name[i],end = '-')

'''
names = "abcdefgh"
for i in range(0,len(names)):
    if(i%3==0 and i!=0):
        print('-',end = '')
    else:
        print(names[i],end = '')'''

'''
fileptr = open('abc.txt','a')

if fileptr:
    print("file opened successfully")

fileptr.write("python")
print(fileptr)'''

'''
a = abs(-20)
print(a)
print()

boolean_list = [True,False]
res = all(boolean_list)
print(res)

boolean_list = [False , True]
res = any(boolean_list)
print(res)

text = 'python'
print(ascii(text))'''

'''
st = 'abc'
st1 = 'ef'
st2 = '123abc'
print(st2.isalnum())
print(st1.capitalize())
print(st.case fold())
print(st2.count('p'))
print(st.endswith('h'))
print(st2.find('3'))
'''

# fileptr = open('abc.txt','a')

# print(dir(locals()['__builtins__']))  #builtin function
'''
try:
    num = 10
    deno = 0

    result = num/deno

    print(result) #Arithematic

except:
    print("Error: Denominator cannot be 0")

finally:
    print("This is finally block")'''

'''
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[2]/0)

except ZeroDivisionError:
    print("Denominator cannot be 0")

'''
'''
try:
    num = int(input('Enter a number : '))
    assert num%2==0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
'''

'''
file_path = 'abc.txt'

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred : {e}")
finally:
    print("closing the file")
'''
'''year = int(input("Year: "))
month = int(input("Month: "))

day = int(input("Day: "))
result = ( day + 13 * (month+1) // 5 + year + year // 4 - year// 100 + year // 400 ) % 7

weekday = {0: "Saturday",1: "Sunday", 2: "Monday",3: "Tuesday",4:"Wednesday",5: "Thursday",6: "Friday"}

print("The day is " + weekday[int(result)] + ".")
'''
