class Node():
    def __init__(self, value):
        self.value = value
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.ref is not None:
                node = node.ref

            node.ref = new_node

    def add_begin(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    def add_after(self, value, after):
        new_node = Node(value)

        if self.head == None:
            print("Linked List does not contain any Nodes")

        else:
            node = self.head
            while node.ref is not None:
                if node.value == after:
                    break
                else:
                    node = node.ref

            new_node.ref = node.ref
            node.ref = new_node
            
    def pop(self):
        if self.head == None:
            print("Cannot remove Elemnet from an empty linked list")

        elif self.head.ref == None:
            self.head = None
        else:
            node = self.head
            while node.ref.ref is not None:
                node = node.ref

            node.ref = None

    def pop_start(self):
        if self.head == None:
            print("Linked List is empty")

        else:
            node = self.head
            self.head = node.ref

    def __str__(self):
        if self.head == None:
            return "Linked List Is Empty"
        else:
            node = self.head
            data = "["
            while node is not None:
                data+=f"{node.value} "
                node = node.ref
            data+= "]"

        return data

            

my_list = LinkedList()
for i in range(10):
    my_list.append(i)

print(my_list)

my_list.pop_start()

print(my_list)