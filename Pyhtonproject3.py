#PythonProject3

import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        found_contacts = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        if not found_contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(found_contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

    def update_contact(self, keyword, name=None, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact['name'] == keyword or contact['phone'] == keyword:
                if name:
                    contact['name'] = name
                if phone:
                    contact['phone'] = phone
                if email:
                    contact['email'] = email
                if address:
                    contact['address'] = address
                self.save_contacts()
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, keyword):
        for i, contact in enumerate(self.contacts):
            if contact['name'] == keyword or contact['phone'] == keyword:
                del self.contacts[i]
                self.save_contacts()
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)
        elif choice == '4':
            keyword = input("Enter name or phone number to update: ")
            name = input("Enter new name (leave blank to keep unchanged): ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            address = input("Enter new address (leave blank to keep unchanged): ")
            contact_book.update_contact(keyword, name or None, phone or None, email or None, address or None)
        elif choice == '5':
            keyword = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(keyword)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

