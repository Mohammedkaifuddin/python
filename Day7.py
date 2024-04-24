#DAY-7 22/02/2024

#pointers

'''
#id of 5
print("id of 5 = ",id(5))

a = 5
#id of a
print("id of a = ",id(a))

b = a
#id of b
print("id of b = ",id(b))

c = 5.0
#id of c
print("id of c  = ",id(c))

apple = 20
banana = 20.0

print("id of apple = ",id(apple))
print("id of banana = ",id(banana))

print(apple is banana)
print(apple == banana)

pineapple=[10,20,30]
grapes = [10,20,30]

print("'id of pineapple = ",id(pineapple))
print("'id of pineapple = ",id(grapes))

print(pineapple is grapes)
print(pineapple == grapes)

#decimal to octal
print('oct(10) is : ',oct(10))
#hexadecimal to octal
print('oct(0XA) is : ',oct(0XA))
#binary to octal
print('oct(0b101) is : ',oct(0b101))
'''

#use pass inside if statement
'''
n=10
if n >= 10:
    pass
    print('test')
else:
    print('take care')

print('python')
print('good')
'''


'''
from abc import ABC,abstractmethod

class car(ABC):
    def mileage(self):
        pass
    def bitm_mileage(self):
        print('non abstract method')

class tesla(car):
    def mileage(self):
        print("abstract method defined in 'tesla' class-The mileage")

class suzuki(car):
    def mileage(self):
        print("abstract method defined in 'suzuki' class-The mileage")

class duster(car):
    def mileage(self):
        print("abstract method defined in 'duster' class-The mileage")

class renault(car):
    def mileage(self):
        print("abstract method defined in 'duster' class-The mileage")


t = tesla()
t.mileage()

r = renault()
r.mileage()

s = suzuki()
s.mileage()

d = duster()
d.mileage()

c = car()
c.mileage()
c.bitm_mileage()
'''


'''
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")

    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: sar{amount}")
        print(f"Withdrawal successful. Remaining balance: sar{account['balance']}")


def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: sar{amount}")
    print(f"Deposit successful. Remaining balance: sar{account['balance']}")


def get_balance(account):
    return account['balance']


def get_transaction_history(account):
    str1 = "\n".join([str(i) for i in account['transactions']])
    try:
        a = open("trans2.txt", "x")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: sar')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']
    except FileExistsError:
        a = open("abcd.txt", "w")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: sar')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']


# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}
bal = 'sar' + str(account['balance'])
# Dictionary to map user choices to functions
m = 0
e = input("enter your email:")
p = input("enter your password:")
p1 = "0123"
e1 = "abc@gmail.com"
if (e == e1) and (p == p1):
    choices = {
        '1': deposit,
        '2': withdraw,
        '3': get_balance,
        '4': get_transaction_history
    }

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)

            elif choice == '2':

                m = m + 1
                if m > 5:
                    print("withdrawing limit reached")
                else:
                    amount = float(input("Enter amount: "))
                    choices[choice](account, amount)

            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid credentials")'''


#Data structure in python

#stack

def create_stack():
    stack = []
    return
