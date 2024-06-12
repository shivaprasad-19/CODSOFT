class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"
contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone, email, address)
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"\nContact {idx}")
            print(contact)

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact.name or search_term in contact.phone]
    if not found_contacts:
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(contact)

def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
            contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term in contact.name or search_term in contact.phone:
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
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
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
