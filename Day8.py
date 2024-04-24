#DAY - 8  23/4/2024


'''string = str(input('Enter the string : '))
i = []
l = string.split()
wordfreq = [l.count(p) for p in l]
#print(zip(l,wordfreq))
print(dict(zip(l, wordfreq)))'''


'''
my_dict = {'apple':10,'ball':20,'air':30,'ballon':40,'c':100,'z':120}

for key,value in my_dict.items():
    if key[0].lower() == 'a':
        print(f'The value of {key} is {value}')
'''

'''
d = {'A':1,'B':2,'C':3}
key = input('Enter key to check : ')
if key in d.key:
    print('key is present and value of the key is : ')
    print(d[key])
else:
    print("key isn't present")
'''


'''
def sum_number():
    lst= input('Enter number separated by spaces : ').split()
    lst = [int(x) for x in lst]
    negative_sum = 0
    even_positive_sum = 0
    odd_positive_sum = 0
    for num in lst:     #34 56 78 54 77
        if num < 0:
            negative_sum += num
            print(negative_sum)
        elif num % 2 == 0:
            even_positive_sum += num
            print(even_positive_sum)
        else:
            odd_positive_sum += num
            print(odd_positive_sum)

        print(negative_sum)
        print(even_positive_sum)
        print(odd_positive_sum)
sum_number()
'''

'''
values  = [2,4,1,-3,-5,7]
negative_value = max(i for i in values if i<0)
positive_num = max(j for j in values if j%2 == 0)
print(negative_value)
print(positive_num)
'''

#1) Python Program to Print Sum of Negative Numbers,Positive Even Numbers and Positive Odd numbers in a List

#2) Python Program to Print Largest Even and Largest Odd Number in a List


'''
#-------------------------
n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print("Sum of all positive even numbers:",sum1)
print("Sum of all positive odd numbers:",sum2)
print("Sum of all negative numbers:",sum3)

#------------------------------------

n=int(input("Enter the number of elements to be in the list:"))
b=[]
for i in range(0,n):
    a=int(input("Element: "))
    b.append(a)
c=[]
d=[]
for i in b:
    if(i%2==0):
        c.append(i)
    else:
        d.append(i)
c.sort()
d.sort()
count1=0
count2=0
for k in c:
    count1=count1+1
for j in d:
    count2=count2+1
print("Largest even number:",c[count1-1])
print("Largest odd number",d[count2-1])

#3----------------------------------
'''

# Python Program to Create and Display Linked List

# Create a node
'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

#create a head node and set as null. Here dont be use null. Be use None 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
# Append the data in last
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
'''


# Python Program to Check if Two Lists are Equal




'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next


def is_equal(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head
    while (current1 and current2):
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False


llist1 = LinkedList()
llist2 = LinkedList()

data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))

data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))

if is_equal(llist1, llist2):
    print('The two linked lists are the same.')
else:
    print('The two linked list are not the same.', end='')

# Python Program to Find Intersection and Union of Two Linked Lists
'''
'''

class Node:
    def __init__(self, data):
       self.data = data
       self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.data)
            copy.insert_at_end(node)
            current = current.next
        return copy

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

'''
'''def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next


def find_union(llist1, llist2):
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union

    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)

    return union


def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return LinkedList()

    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.insert_at_end(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)

    return intersection


a_llist1 = LinkedList()
a_llist2 = LinkedList()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist2.insert_at_end(node)

union = find_union(a_llist1, a_llist2)
intersection = find_intersection(a_llist1, a_llist2)

print('Their union: ')
union.display()
print()
print('Their intersection: ')
intersection.display()
print()

'''

'''
# Python Program to Create and Display Linked List
'''
# Create a node
'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

#create a head node and set as null. Here dont be use null. Be use None 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
# Append the data in last
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

a_llist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    a_llist.append(data)
print('The linked list: ', end = '')
a_llist.display()
'''

'''
# Python Program to Check if Two Lists are Equal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next


def is_equal(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head
    while (current1 and current2):
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    if current1 is None and current2 is None:
        return True
    else:
        return False


llist1 = LinkedList()
llist2 = LinkedList()

data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    llist1.append(int(data))

data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    llist2.append(int(data))

if is_equal(llist1, llist2):
    print('The two linked lists are the same.')
else:
    print('The two linked list are not the same.', end='')
'''
# Python Program to Find Intersection and Union of Two Linked Lists

'''
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current

    def duplicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            node = Node(current.data)
            copy.insert_at_end(node)
            current = current.next
        return copy

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next

def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        data = current1.data
        while current2:
            temp = current2
            current2 = current2.next
            if temp.data == data:
                llist.remove(temp)
        current1 = current1.next


def find_union(llist1, llist2):
    if llist1.head is None:
        union = llist2.duplicate()
        remove_duplicates(union)
        return union
    if llist2.head is None:
        union = llist1.duplicate()
        remove_duplicates(union)
        return union

    union = llist1.duplicate()
    last_node = union.head
    while last_node.next is not None:
        last_node = last_node.next
    llist2_copy = llist2.duplicate()
    last_node.next = llist2_copy.head
    remove_duplicates(union)

    return union


def find_intersection(llist1, llist2):
    if (llist1.head is None or llist2.head is None):
        return LinkedList()

    intersection = LinkedList()
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        data = current1.data
        while current2:
            if current2.data == data:
                node = Node(data)
                intersection.insert_at_end(node)
                break
            current2 = current2.next
        current1 = current1.next
    remove_duplicates(intersection)

    return intersection

'''
'''
a_llist1 = LinkedList()
a_llist2 = LinkedList()
data_list = input('Please enter the elements in the first linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist1.insert_at_end(node)
data_list = input('Please enter the elements in the second linked list: ').split()
for data in data_list:
    node = Node(int(data))
    a_llist2.insert_at_end(node)

union = find_union(a_llist1, a_llist2)66666
intersection = find_intersection(a_llist1, a_llist2)


print('Their union: ')
union.display()
print()
print('Their intersection: ')
intersection.display()
print()
'''

'''
userinput = input('Enter the string : ')
print([word for word in userinput.split() if 's' in word])
'''


