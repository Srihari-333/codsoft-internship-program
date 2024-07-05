class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name}: {contact.phone_number}")
    
    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print("Contact not found.")
    
    def update_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print("Enter new details (leave blank to keep current):")
                new_name = input(f"Name ({contact.name}): ").strip() or contact.name
                new_phone_number = input(f"Phone number ({contact.phone_number}): ").strip() or contact.phone_number
                new_email = input(f"Email ({contact.email}): ").strip() or contact.email
                new_address = input(f"Address ({contact.address}): ").strip() or contact.address
                contact.name = new_name
                contact.phone_number = new_phone_number
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")
                found = True
        if not found:
            print("Contact not found.")
    
    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_list = ContactList()
    
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            new_contact = Contact(name, phone_number, email, address)
            contact_list.add_contact(new_contact)
        
        elif choice == '2':
            contact_list.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_list.search_contact(search_term)
        
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ").strip()
            contact_list.update_contact(search_term)
        
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ").strip()
            contact_list.delete_contact(search_term)
        
        elif choice == '6':
            print("Exiting the Contact Management System.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
