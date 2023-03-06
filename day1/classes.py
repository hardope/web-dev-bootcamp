class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}, age : {self.age}"

    def change(self, new_age):
        self.age = new_age

james = person("James", 25)
james.change(28)
print(james)