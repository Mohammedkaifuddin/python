#DAY 6 - 20/04/2024
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

'''
d = int(input('Enter the date : '))
if(d>0 and d<=31):
    m = int(input('Enter the month : '))
    if(m>0 and m<=12):
        if(((d<=31) and (m == 1 or m==3 or m==5 or m==7 or m==8 or m==12)) or (())):
            y=int(input('Enter the year : '))
            if(y>1900 and y<9999):
                c=y//100
                D=y%100
                temp=m
                if m>2:
                    m-=2
                else:
                    m+=1
                if((d==29) and (temp==2)):
                    if(y%400 == 0) and (y%100 == 0):
                        f=d+((13*m-1)/5)+D+D/4+(c/4)-2*c
                        fres=int(f%7)
                        day = {0:'sunday',1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday'}
'''

#oops

#single inheritance
'''
class person:
    def __init__(self ,name,age):
        self.name = name
        self.age = age

class professor(person):
    def isprofessor(self):
        return f"{self.name} is a professor"

sir = professor("abc",20)

a = sir.isprofessor()
print(a)'''

#multiple inheritance

'''class s:
    num1 = 3

class ms:
    num2 = 5

class son1(s,ms):
    def addition(self):
        return self.num1+self.num2

obj = son1()
print(obj.addition())'''

#multiple inheritance
'''
class s:
    num1 = 3
    def home(self ,a,b):
        self.a = a
        self.b = b
        print("s home property value = ",self.a+self.b)

class ms:
    num2 = 5
    def jewels(self,a):
        self.a = 1000
        print("ms jewels property value = ",self.a)

class son1(s,ms):
    def addition(self):
        print(self.num1+self.num2)

obj = son1()
obj.addition()
obj.jewels(1000)
obj.home(100000,200000)
'''

'''
class parentclass:
    def call_me(self):
        print("I am a parent class")

class childclass(parentclass):
    def call_me(self):
        print("I am a child class")

pobj = parentclass()
pobj.call_me()
pobj.callme()'''

'''
class book:
    def __init__(self,title,quantity,author,price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book:{self.title},Quantity:{self.quantity},author:{self.author},price:{self.price}"

book1 = book('Book 1',12,'Author 1',120)
book2 = book('Book 2',18,'Author 2',220)
book3 = book('Book 3',28,'Author 3',320)

print(book1)
print(book2)
print(book3)
'''

'''
class a:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_mp(self, n):
        num_str = str(n)
        for i in range(len(num_str)):
            new_num = int(num_str[:i] + num_str[i + 1:])
            if not self.is_prime(new_num):
                return False
        return True

    def find_mp(self, start, end):
        mp = []
        for num in range(start, end + 1):
            if self.is_prime(num) and self.is_mp(num):
                mp.append(num)
        return mp

class neon(a):
    def neon(self):
        num = int(input('Enter the neon to check neon or not : '))
        sqr = num*num
        sum = 0
        while sqr>0:
            sum = sum + sqr%10
            sqr = sqr//10

        if(num == sum):
            print("neon number")
        else:
            print("Not a neon number")

class pattern(a):
    def x_pattern(self):
        name = str(input("Enter the name : "))
        length = len(name)

        for i in range(length):
            for j in range(length):
                if i == j or i + j == length - 1:
                    print(name[i], end=' ')
                else:
                    print(' ', end=" ")
            print()

class banking(pattern,neon):
    def bank(self):
        class BankAccount:
            def __init__(self, initial_balance):
                self.balance = initial_balance
                self.transactions = []

            def withdraw(self, amount):
                if amount > self.balance:
                    print("Insufficient funds!")
                else:
                    self.balance -= amount
                    self.transactions.append(f"Withdrawal: ${amount}")
                    print(f"Withdrawal successful. Remaining balance: ${self.balance}")

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
        print("Transaction History:", account.get_transaction_history())

class reverse(a):
    def reverse_string(self):
        string = str(input('Enter the sting to reverse : '))
        str1 = ""
        for i in string:
            str1 = i + str1
        return str1

b = banking()
b.neon()
b.x_pattern()
b.bank()

r = reverse()
res = r.reverse_string()
print(res)
#mp = r.mp(10,100)
#print(mp)
'''


