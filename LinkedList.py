class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList: #linkedlist constructor
    def __init__(self, value):
        #create the node with head and tail
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next): # moves the pre and temp in the list
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else : 
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        for _ in range(index):
            temp =temp.next
        return temp.value

    def insert(self, index, value):
        pass

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.prepend(6)

print("List items are: ")
my_linked_list.print_list()

# print("Popped items are: ")
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())

print("First Popped items are: ")
print(my_linked_list.pop_first())

print("New list items are: ")
my_linked_list.print_list()

print("\nGet method: ")
print(my_linked_list.get(1))


