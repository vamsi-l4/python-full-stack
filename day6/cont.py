def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!")
    def view_contacts():
        try:
            with open("contacts.txt", "r") as file:
                contacts = file.readlines()
                if not contacts:
                    print("No contacts found.")
                else:
                    for contact in contacts:
                        name, phone, email = contact.strip().split(",")
                        print(f"Name: {name}, Phone: {phone}, Email: {email}")
        except FileNotFoundError:
            print("No contacts file found.")

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                if search_name in line.lower():
                    name, phone, email = line.strip().split(",")
                    print(f"Name: {name}, Phone: {phone}, Email: {email}")
                    found = True
                    break
        if not found:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file does not exist.")
