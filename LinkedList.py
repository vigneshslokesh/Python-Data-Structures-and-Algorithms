class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList: #linkedlist constructor
    def __init__(self, value):
        #create the node
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
        pass
    def prepend(self, value):
        pass
    def insert(self, index, value):
        pass

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)