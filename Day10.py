#Day - 25/04/2024


'''
name = 'abcde'
for i in name:
    print(i,end = ' ')

for _ in  range(0,100):
    print(_)

milllion = 1_000_000
binary = 0b_1110
octa = 0o_64
hexa = 0x_23_ab
print(milllion)
print(binary)

print(octa)
print(hexa)
'''

'''
a,_,c = (1,2,3)
print(a,_,c)
for _ in range(5):
    print(_)
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_mid(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Position out of range")
                return
            current_node = current_node.next
        if current_node is None:
            print("Position out of range")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def remove_first(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def remove_last(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def remove_mid(self, position):
        if not self.head:
            print("List is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        prev_node = None
        current_node = self.head
        for _ in range(position):
            if current_node is None:
                print("Position out of range")
                return
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Position out of range")
            return
        prev_node.next = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Main program
linked_list = SinglyLinkedList()

while True:
    print("\n1. Add node at first")
    print("2. Add node at last")
    print("3. Add node at middle")
    print("4. Remove node at first")
    print("5. Remove node at last")
    print("6. Remove node at middle")
    print("7. Display the list")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter data to add at first: ")
        linked_list.add_first(data)
    elif choice == '2':
        data = input("Enter data to add at last: ")
        linked_list.add_last(data)
    elif choice == '3':
        data = input("Enter data to add: ")
        position = int(input("Enter position to add (0 for first): "))
        linked_list.add_mid(data, position)
    elif choice == '4':
        linked_list.remove_first()
    elif choice == '5':
        linked_list.remove_last()
    elif choice == '6':
        position = int(input("Enter position to remove (0 for first): "))
        linked_list.remove_mid(position)
    elif choice == '7':
        linked_list.display()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
'''

#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

arr = [12,11,13,5,6]

insertion_sort(arr)
print("sorted array is : ",arr)


#selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i] #swapping


arr = [64,25,12,22,11]
selection_sort(arr)
print("sorted array is : ",arr)

#Bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [64,34,25,12,22,11,90]
bubble_sort(arr)
print('sorted array is : ',arr)

print(37*2)
print(len(arr))

