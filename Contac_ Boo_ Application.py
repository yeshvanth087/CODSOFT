# Contact Book Application

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts available.")
        return

    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    key = input("Enter name or phone to search: ")

    found = False
    for contact in contacts:
        if key.lower() in contact['name'].lower() or key == contact['phone']:
            print("\n🔍 Contact Found:")
            print(contact)
            found = True

    if not found:
        print("❌ Contact not found.")

def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if contact['phone'] == phone:
            print("Enter new details (leave blank to keep old value)")
            contact['name'] = input("New Name: ") 
            contact['email'] = input("New Email: ") 
            contact['address'] = input("New Address: ") 
            print("✅ Contact updated successfully!")
            return

    print("❌ Contact not found.")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return

    print("❌ Contact not found.")

def menu():
    while True:
        print("\n📱 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

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
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")

menu()

