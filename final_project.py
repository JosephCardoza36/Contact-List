import json


def create_contact(name, last, phone, other):

    with open('contact.txt', 'a') as f:
        new_contact = {"First": name, "Last": last,
                       "Phone": f"({phone[0:3]}){phone[3:6]}-{phone[6:10]}", "Other": other}
        with open('contact.txt', 'r') as r:
            if r.readlines() == []:
                f.write(json.dumps(new_contact))
                # check to see if text file is empty, does not write new line
                print(f"\nSuccessfully Added {name} into contact book!")
            else:
                f.write("\n")
                f.write(json.dumps(new_contact))

                print(f"\nSuccessfully Added {name} into contact book!")


def delete_contact(first, last):
    with open('contact.txt', 'r') as data:
        lines = data.readlines()

    with open("contact.txt", "w") as f:
        for line in lines:
            res = json.loads(line)
            if res["First"].upper() == first.upper() and res["Last"].upper() == last.upper():
                deleted = [line]
                print(f"\nDeleted: {deleted[0]}")

            else:
                f.write(line)


def search_contact(first, last):
    with open('contact.txt', 'r') as file:
        reads = file.readlines()
        last_int = last[0]
        for i in reads:
            res = json.loads(i)
            if res["First"] == first and res["Last"][0] == last_int:
                print("\n")
                for i in res:
                    print(f"{i:>20}: {res[i]}")


def read_contact():
    with open('contact.txt', 'r') as file:
        reads = file.readlines()
        print("+------------------------------------------------+")
        print("|  Here are all the names in your contact list:  |")
        print("+------------------------------------------------+")
        for i in reads:
            res = json.loads(i)
            print(
                f"|{res['First']:>25} {res['Last'][0]}.                    |")
        print("+------------------------------------------------+")


print("+------------------------------------------------+")
print("|           Welcome to Cardoza Contact!          |")
print("+------------------------------------------------+")
print("| You can choose to VIEW an existing contact     |")
print("| ADD a new contact, UPDATE or DELETE a contact  |")
print("+------------------------------------------------+")

contact_list = True
while contact_list:
    user_choice = (
        input("\nEnter 'A' for Add, 'V' for View 'D' for Delete \nor 'E' to exit: ")).upper()

    # exit queue
    if user_choice == 'E':
        contact_list = False
        print("Have a great day and love your friends and family!\n")

    # Add contact
    elif user_choice == 'A':
        print("\n")
        name = input("Enter the first name of your contact: ")
        last = input("Enter their last name or last name initial: ")
        phone = input("Enter their phone number (example: 'xxxxxxxxxx'): ")
        other = input("Enter any other information: ")

        create_contact(name, last, phone, other)

    # view contact
    elif user_choice == 'V':
        read_contact()
        first_name = input(
            "\nEnter firstname or ENTER to return to menu: ")

        if len(first_name) > 3:
            last_name = input(
                "Enter the last name or initial: ")

            if first_name and last_name:
                search_contact(first_name, last_name)

            else:
                print("Sorry, we didn't get that name")

    # Delete Contact
    elif user_choice == 'D':
        read_contact()
        first_name = input(
            "\nEnter the first name the contact you want to delete: ")
        last_name = input(
            "Enter their last name: ")
        delete_contact(first_name, last_name)
