contacts = []

def show_menu():
    print("\n=====Contacts Manager ver 1.0=====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Exit")

while True:  #TODO
    show_menu()
    choice = input("Choose an option (1-5) : ")

    if choice == "1":
        name = input("Enter a name : ")
        number = input("Enter a number : ")
        contact = ({"name": name, "number": number})  #OOPS
        contacts.append(contact)
        print(f"{contact} has been added!")

    elif choice == "2":
        if len(contacts) < 1:
            print("No contacts available")
        else:
            name = input("Enter a name to search : ")  #Try 'for-else'
            for contact in contacts:  #OOPS
                if contact['name'] == name:
                    print(f"{contact}")  #BUG
                    break
            else:
                print("Incorrect name!")

    elif choice == "3":
        if len(contacts) < 1:
            print("There are no contacts to show")
        else:
            name = input("Enter a name to delete : ")
            for contact in contacts:
                if contact['name'] == name:  #TODO
                    choice_d = input("Do you really want to delete?[y/n] : ")
                    if choice_d == "y":
                        print(f"{contact} has been deleted!")  #BUG
                        contacts.remove(contact)  #BUG
                        break
                    elif choice_d == "n":
                        break
                    else:
                        print("Incorrect choice")
                        break
            else:
                print("Incorrect name")

    elif choice == "4":
        if len(contacts) < 1:
            print("There are no contacts to show")
        else:
            for contact in contacts:
                print(f"{contact}")

    elif choice == "5":
        print("Goodbye!")
        break
