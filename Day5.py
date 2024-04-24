#DAY 5 - 19/04/2024

'''
def abc():
    return "This is my bank balance"

#initializing dictionary
#check for function name as key
test_dict = {'fname':abc,'age':50,'address':'def'}

#printing original dictionary
print("The original dictionary is : "+str(test_dict))

#calling function using brackets
res = test_dict['fname']()

#printing result
print("The required call result : "+str(res))
'''

'''
def abc(a,b):
    print("my result banck balance = ",a+b)


test_dict = {'fname':abc,'age':50,'address':'def'}

print("The original dictionary is : "+str(test_dict))
res = test_dict['fname'](10,20)
'''

'''
class abcd:
    def __init__(self):
        print("this is what?")
    def test1(self):
        print("this is without para")
    def test2(self,a,b):
        print(a+b,"this is with para")
    def test3(self,a):
        print('check it magical prime or not')
    def test4(self,a):
        print('check neon or not')

abc = abcd()
abc.test1()
abc.test2(10,20.5)
abc.test3(101)
abc.test4(7)
'''
'''
class Bankaccount:
    def __init__(self,initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance-=amount
            self.transactions.append(f"withdrawal:sar{amount}")
            print(f"withdrawal successful. Remaining balance:sar{self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f"Deposit:sar{amount}")
        print(f"Deposit successful.Remaining balance:sar{self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

account = Bankaccount(1000)
print("Balance : ",account)
'''

'''

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def withdraw(shetty, amount):
        if amount > shetty.balance:
            print("Insufficient funds!")
        else:
            shetty.balance -= amount
            shetty.transactions.append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${shetty.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions

# Example usage:
account = BankAccount(1000)
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(200)
account.withdraw(1000)
print("Balance:", account.get_balance())
print("Transaction History:", account.get_transaction_history())'''


'''

year = int(input("Year: "))
while not int(year) in range(1583, 10000):
    year = input("Out of allowed range 1583 - 9999. Please enter a valid number: ")

month = int(input("Month: "))
while not int(month) in range(1, 13):
 month = input("Out of allowed range 1 - 12. Please enter a valid number: ")

if month == 1 or month == 2:
    month += 12
    year -= 1

day = int(input("Day: "))
while not int(day) in range(1, 32):
        day = input("Out of allowed range 1 - 31. Please enter a valid number: ")


result = ( day + 13 * (month+1) // 5 + year + year // 4 - year// 100 + year // 400 ) % 7


weekday = {0: "Saturday",1: "Sunday", 2: "Monday",3: "Tuesday",4:
"Wednesday",5: "Thursday",6: "Friday"}

print("The day is " + weekday[int(result)] + ".")
'''
'''
import math
date = int(input('Enter the date : '))
month = int(input('Enter the month : '))
year = int(input('Enter the year : '))

c = year//100
d = year%100
month = month-2
f = date + ((13*month-1)/5) + d + (d/4) + (c/4) - 2 * c


fres = int(f%7)
print(fres)
day = {0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}

#weekday = {0: "Saturday",1: "Sunday", 2: "Monday",3: "Tuesday",4:"Wednesday",5: "Thursday",6: "Friday"}
print(day[fres])
'''

