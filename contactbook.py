#%%
# Contact Book

# Dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added successfully.")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}")
    else:
        print("\nNo contacts available.")

# Function to search for a contact by name or phone number
def search_contact():
    query = input("\nSearch by name or phone number: ").lower()
    found = False
    for name, info in contacts.items():
        if query in name.lower() or query == info['phone']:
            print(f"\nFound: Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")
            found = True
    if not found:
        print("\nContact not found.")

# Function to update contact details
def update_contact():
    name = input("\nEnter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter new phone number (leave blank to skip): ")
        email = input("Enter new email (leave blank to skip): ")
        address = input("Enter new address (leave blank to skip): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"\nContact {name} updated successfully.")
    else:
        print("\nContact not found.")

# Function to delete a contact
def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\nContact {name} deleted successfully.")
    else:
        print("\nContact not found.")

# Main menu loop for user interaction
def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")

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
            print("\nExiting Contact Book.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the main loop
if __name__ == "__main__":
    main()


# %%
