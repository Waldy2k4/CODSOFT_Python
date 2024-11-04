contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip().title()
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully.\n")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print()

def search_contact():
    search = input("Enter name or phone number to search: ").strip().title()
    found = False
    for name, details in contacts.items():
        if search in name or search == details['phone']:
            print(f"\nContact Found - Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the contact name to update: ").strip().title()
    if name not in contacts:
        print("Contact not found.")
        return
    print(f"\nUpdating Contact - {name}")
    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()
    address = input("Enter new address: ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' updated successfully.\n")

def delete_contact():
    name = input("Enter the contact name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
