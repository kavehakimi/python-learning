class Person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def introduce(self):
        print("My name is ", self.name)

    def say_hello(self):
        print("Hello ", self.name)

class Contact(Person):
    def __init__(self, name, age, sex, mobile, email):
        super().__init__(name, age, sex)
        self.mobile = mobile
        self.email = email
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Sex: ", self.sex)
        print("Mobile: ", self.mobile)
        print("Email: ", self.email)

contact1 = Contact(
    "Kaveh",
    50,
    "Male",
    "07495681253",
    "khakimi@gmail.com"
)

contact1.introduce()
contact1.say_hello()
contact1.display()