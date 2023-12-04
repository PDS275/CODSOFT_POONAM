contacts = []

def add_contact():
    print("Add a new contact:")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contacts.append(contact)
    if found_contacts:
        print("Search Results:")
        for found_contact in found_contacts:
            print(f"Name: {found_contact['Name']}")
            print(f"Phone: {found_contact['Phone']}")
            print(f"Email: {found_contact['Email']}")
            print(f"Address: {found_contact['Address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter the number of the contact to update: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"Update contact: {contact['Name']}")
        contact['Name'] = input("New Name: ")
        contact['Phone'] = input("New Phone Number: ")
        contact['Email'] = input("New Email: ")
        contact['Address'] = input("New Address: ")
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
