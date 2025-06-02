
import json
import os
import random

CONTACTS_FILE = 'contacts.json'

def  load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE,'r') as  file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE,'w') as file:
        json.dump(contacts, file,indent=4)

def add_contact():
    name =input("Enter name:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    contacts=load_contacts()
    contacts.append({"name":name,"phone":phone,"email":email})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts():
        print("No contacts found")
        return
    for idx, contact in enumerate(contacts,start=1):
        print(f"{idx}.name:{contact['name']},phone:{contact['phone']},Email:{contact['email']}")

def edit_contact():
    contacts = load_contacts()
    view_contacts()
    try:
        index=int(input("Enter contact number to  edit:")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enternew name:")
            contacts[index]['phone']= input("Enter new phone:")
            contacts[index]['email']=input("Enter new email:")
            save_contacts(contacts)
            print("contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact():
    contacts = load_contacts()
    view_contacts()
    try:
        index = int(input("Enter conntact number to delete:")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact:{removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def play_random_number_game():
    number = random.randint(1,100)
    attempts = 0
    print("Guess the number between 1 and 100.")
    while True:
        try:
            guess = int(input("your guess:"))
            atteempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"congratulations! you guessedd it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("contact Management system")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("Delete Contact")
        print("5. Play Random Number Game (Bonus)")
        print("6. Exit")
        choice  =input("Choose an option:")

        if choice == '1':
            add_contact()
        elif choice =='2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            play_random_number_game()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
   main()










