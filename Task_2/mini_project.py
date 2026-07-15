
# ## Capstone — Mini Project

# Build a *Contact Book* that saves data between runs:

# 1. Create a Contact class with name, phone, and email.
# 2. Keep a list of Contact objects in your program.
# 3. Show a menu in a loop:
#    - 1 Add a contact
#    - 2 View all contacts
#    - 3 Search for a contact by name
#    - 4 Delete a contact
#    - 5 Save and exit
# 4. When the user adds or deletes contacts, the data should survive after the program closes. Save the contacts to a contacts.json file and load them back when the program starts.
# 5. Handle the case where contacts.json does not exist yet on the very first run.
# 6. Handle invalid menu input without crashing.

import json
import os



# Contact Class

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }



# Global Contact List

contacts = []



# Load Contacts

def load_contacts():
    global contacts

    if not os.path.exists("contacts.json"):
        contacts = []
        return

    with open("contacts.json", "r") as file:
        data = json.load(file)

        contacts = []

        for item in data:
            contact = Contact(
                item["name"],
                item["phone"],
                item["email"]
            )
            contacts.append(contact)


# -------------------------
# Save Contacts
# -------------------------
def save_contacts():

    data = []

    for contact in contacts:
        data.append(contact.to_dict())

    with open("contacts.json", "w") as file:
        json.dump(data, file, indent=4)


# -------------------------
# Add Contact
# -------------------------
def add_contact():

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = Contact(name, phone, email)

    contacts.append(contact)

    print("\nContact Added Successfully.\n")


# -------------------------
# View Contacts
# -------------------------
def view_contacts():

    if len(contacts) == 0:
        print("\nNo Contacts Found.\n")
        return

    print("\n----- Contact List -----")

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact.name}")
        print(f"   Phone : {contact.phone}")
        print(f"   Email : {contact.email}")
        print()


# -------------------------
# Search Contact
# -------------------------
def search_contact():

    name = input("Enter Name to Search: ").lower()

    found = False

    for contact in contacts:

        if contact.name.lower() == name:
            print("\nContact Found")
            print("Name :", contact.name)
            print("Phone:", contact.phone)
            print("Email:", contact.email)

            found = True
            break

    if not found:
        print("\nContact Not Found.\n")


# -------------------------
# Delete Contact
# -------------------------
def delete_contact():

    name = input("Enter Name to Delete: ").lower()

    for contact in contacts:

        if contact.name.lower() == name:
            contacts.remove(contact)

            print("\nContact Deleted Successfully.\n")
            return

    print("\nContact Not Found.\n")


# -------------------------
# Main Menu
# -------------------------
def main():

    load_contacts()

    while True:

        print("========== Contact Book ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Save and Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            save_contacts()

            print("\nContacts Saved Successfully.")
            print("Goodbye!")

            break

        else:
            print("\nInvalid Choice. Please Try Again.\n")


# -------------------------
# Start Program
# -------------------------
main()