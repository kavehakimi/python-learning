class contact:
    def __init__(self, name, mobile, email):
        self.name = name
        self.mobile = mobile
        self.email = email
    
    def display(self):
        print("Name: ", self.name)
        print("Mobile: ", self.mobile)
        print("Email: ", self.email)

    def say_hello(self):
        print("Hello, my name is: ", self.name)

contact1 = contact(
    "Kaveh",
    "07495681253",
    "khakimi@gmail.com"
)

contact2 = contact(
    "Hoda",
    "7495681265",
    "h.h.farahani@gmail.com"
)

contact1.display()
contact2.display()

contact1.say_hello()
contact2.say_hello()