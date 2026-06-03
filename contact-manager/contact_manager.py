contacts = []

def add_contact():
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
        print("Invalid Otion!")





