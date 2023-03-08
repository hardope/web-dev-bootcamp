class Queue():
    def __init__(self):
        self.values = []

    def add(self, value):
        self.values.insert(0, value)
        print(self.values)
    
    def remove(self):
        try:
            self.values.pop()
            print(self.values)
        except IndexError:
            print("Print Stack is empty")

my_queue = Queue()
my_queue.add(0)
my_queue.add(3)
my_queue.add(5)
my_queue.remove()
my_queue.remove()
my_queue.remove()
my_queue.remove()
my_queue.remove()