import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "contacts.json"
contacts = []

class Contact:
    def __init__(self, name, mobile, email):
        self.name = name
        self.mobile = mobile
        self.email = email

    def display(self):
        print("----------")
        print("Name: ", self.name)
        print("Mobile: ", self.mobile)
        print("Email: ", self.email)

    def to_dict(self):
        return{
            "name": self.name,
            "mobile": self.mobile,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["mobile"], data["email"])

def add_contact():
    name = input("\nEnter name: ")
    mobile = input("Enter mobile: ")
    email = input("Enter email: ")

    new_contact = contact(name, mobile, email)
    contacts.append(new_contact)
    save_contacts_to_file()
    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("There is no contact!")
        return
      
    for contact in contacts:
        contact.display()

def save_contacts_to_file():
    datalist = []

    for contact in contacts:
        datalist.append(contact.to_dict())
    
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(datalist, f, indent=4)

def load_contacts_from_file():
    global contacts
    try:
        with open(JSON_PATH, encoding="utf-8") as f:
            datalist = json.load(f)

        for data in datalist:
            contacts.append(contact.from_dict(data))

    except FileNotFoundError:
        contacts = []

load_contacts_from_file()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    option = input("Choose your option: ")

    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        break
    else:
        print("Invalid Option!")