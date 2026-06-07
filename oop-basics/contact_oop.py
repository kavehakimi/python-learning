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

    new_contact = Contact(name, mobile, email)
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
            contacts.append(Contact.from_dict(data))
    
    except FileNotFoundError:
        contacts = []

def search_contact():
    name_to_search = input("\nEnter name to search: ")

    found = False

    for contact in contacts:
        if contact.name.lower() == name_to_search.lower():
            contact.display()
            found = True

    if not found:
        print("Contact not found!")

def delete_contact():
    name_to_delete = input("\nEnter name to delete: ")

    for contact in contacts:
        if contact.name.lower() == name_to_delete.lower():
            contacts.remove(contact)
            save_contacts_to_file()
            print("Contact deleted successfully!")
            return
    
    print("Contact not found!")

def update_contact():
    name_to_update = input("\nEnter name to update: ")
    for contact in contacts:
        if contact.name.lower() == name_to_update.lower():
            contact.name = input("Enter new name: ")
            contact.mobile = input("Enter new mobile: ")
            contact.email = input("Enter new email: ")

            save_contacts_to_file()
            print("Contact updated successfully!")
            return

    print("Contact not found!")


load_contacts_from_file()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    option = input("Choose your option: ")

    if option == "1":
        add_contact()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        delete_contact()
    elif option == "5":
        update_contact()
    elif option == "6":
        break
    else:
        print("Invalid Option!")