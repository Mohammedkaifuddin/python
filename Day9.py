#Day 9 24/04/2024


'''

from functools import reduce
n = int(input('Enter the number of elements : '))
decimal = []
binary = []
for i in range(0,n):
    binary = (input('Enter the binary number : '))
    num = reduce(lambda x, y: 2 * x + y, map(int, binary))
    decimal.append(num)
print(decimal)

for num in  decimal:
    if(num%5)==0:
        print(num,' is divisible by 5')
'''

'''
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)
'''

'''
from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("Full : ",q.full())
print(q.get())
print(q.get())
print(q.get())
print("empty : ",q.empty())
'''

'''
class Queue:
    def __init__(self):
        self.queue = list()

    def addtoqueue(self,value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def size(self):
        return len(self.queue)

msh = Queue()
msh.addtoqueue('a')
msh.addtoqueue('b')
msh.addtoqueue('c')
print(msh.size())
'''

'''
class Queue:
    def __init__(self):
        self.queue = list()

    def addtoqueue(self,value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def removefromqueue(self):
        if  len(self.queue)>0:
            return self.queue.pop()
        return ("No element in queue")
    def size(self):
        return len(self.queue)

msh = Queue()
msh.addtoqueue('a')
msh.addtoqueue('b')
msh.addtoqueue('c')
print(msh.size())
print(msh.removefromqueue())
print(msh.removefromqueue())
print(msh.removefromqueue())
'''


'''

def validity_password(password):
    specail_sys = ['$','@',"#"]

    val = True
    if len(password) < 6:
        print('length should be at least 6')
        val = False
    if len(password) > 16:
        print('length should be at least 16')
    for char in password:
        if ord(char) >= 48 and ord(char) <=57:
password = 'Abc@123'''


'''
months = {'jan':31,'feb': '28,29','mar':31,'apr':30,'may':31,'jun':30,'jul':31,'aug':31,'sep':30,'oct':31,'nov':30,'dec':31}

m = input('Enter the month : ').lower()

if m in months.keys:
    print(months[m])
else:
    print("invalid input")
'''

