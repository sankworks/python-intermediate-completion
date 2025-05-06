contacts = []

def show_menu():
    print("\n=====Contacts Manager ver 1.1=====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

while True:  
    show_menu()
    choice = input("Choose an option (1-5) : ")

    if choice == "1":
        while True: #Fix bug
            name = input("Enter a name : ")
            if name.strip(): #Refatored to add input validation
                break
            print("Name cannot be empty! Please try again.")
        
        while True: #Fix bug
            number = input("Enter a number : ")
            if number.isdigit(): #Restored to add input validation
                break
            print("Phone number must be digits only! Please try again.") 
            
        contact = {"name": name, "number": number} #Fixed(Del '()')  
        contacts.append(contact)
        print(f"{contact} has been added!")

    elif choice == "2":
        if not contacts: #Refactored to be simple
            print("No contacts available")
        else:
            name = input("Enter a name to search : ") 
            for contact in contacts:  
                if contact['name'].lower() == name.lower(): #Refactored to make more stable
                    print(f"Name: {contact['name']}, Number: {contact['number']}")  #Refactored to make more readable
                    break
            else:
                print("Incorrect name!")

    elif choice == "3":
        if not contacts: #Refactored to be simple
            print("There are no contacts to show")
        else:
            name = input("Enter a name to delete : ")
            for contact in contacts:
                if contact['name'].lower() == name.lower(): #Refactored to make more stable
                    choice_d = input("Do you really want to delete?[y/n] : ")
                    if choice_d == "y":
                        print(f"{contact} has been deleted!")  
                        contacts.remove(contact)  
                        break
                    elif choice_d == "n":
                        break
                    else:
                        print("Incorrect choice")
                        break
            else:
                print("Incorrect name")

    elif choice == "4":
        if not contacts: #Refactored to be simple
            print("There are no contacts to show")
        else:
            print("\n===== List of your contacts =====") #Refactored to make readable #Fix(location)
            for contact in contacts:
                print(f"Name: {contact['name']}, Number: {contact['number']}") #Refactored to make readable

    elif choice == "5":
        print("Goodbye!")
        break
