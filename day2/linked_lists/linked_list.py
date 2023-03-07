class Node():
    def __init__(self, value):
        self.value = value
        self.ref = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            node = self.head
            while node.ref is not None:
                node = node.ref

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
    my_list.add(i)

for i in range(14):
    my_list.pop()
    print(my_list)

