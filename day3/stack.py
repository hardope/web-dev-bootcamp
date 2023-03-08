class Stack():
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.append(value)

        print(self.values)


    def remove(self):
        try:
            self.values.pop(len(self.values) - 1)
            print(self.values)
        except:
            print("Stack is empty")


my_stack = Stack()

my_stack.add(1)
my_stack.add(2)
my_stack.add(3)
my_stack.remove()
my_stack.remove()
my_stack.remove()
my_stack.remove()
