import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "contacts.json"

contacts = []

def add_contact():
    print("\n")
    name = input("Enter name: ")
    mobile = input("Enter mobile: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "mobile": mobile,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("There is no contact!")
        return
    
    for contact in contacts:
        print("----------")
        print("Name: ", contact["name"])
        print("Mobile: ", contact["mobile"])
        print("Email: ", contact["email"])

def add_to_json_file():
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f)

def read_json_file():
    global contacts
    try:
        with open("contacts.json", encoding="utf-8") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

def search_contact():
    search_name = input("Enter name to search: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("----------")
            print("Name: ", contact["name"])
            print("Mobile: ", contact["mobile"])
            print("Email: ", contact["email"])
            found = True
    
    if not found:
        print("Contact not found!")

def delete_contact():
    delete_name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            contacts.remove(contact)
            add_to_json_file()
            print("Contact deleted successfully.")
            return
    
    print("Contact not found!")


read_json_file()

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    option = input("Choose your option: ")

    if option == "1":
        add_contact()
        add_to_json_file()
    elif option == "2":
        view_contacts()
    elif option == "3":
        search_contact()
    elif option == "4":
        delete_contact()
    elif option == "5":
        break
    else:
        print("Invalid Option!")





