class Person():
    def __init__(self, name, age, email, phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def __str__(self):
        out = f"{self.name}\n    age: {self.age} \n    email: {self.email}\n    phone: {self.phone}"
        return out
    
    def change_age(self, age):
        self.age = age

    def to_dict(self):
        out = {}
        out['name'] = self.name
        out['age'] = self.age
        out['email'] = self.email
        out['phone'] = self.phone

        return out