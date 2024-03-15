from src.classes import AddressBook

from src.services import *

# from src.services import parse_input, add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays, show_commands, add_address, edit_address, show_address, remove_address, new_note, edit_note, delete_note, show_notes

from src.disk import save_to_json, load_from_json


def main():
    # book = AddressBook()
    # print(book)
    book, notes = load_from_json()
    # print("main load", book)
    # print("main new", book)

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command ===>  ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            save_to_json(book, notes)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(show_commands())
        # All
        elif command == "all":
            print(show_all(book))  #
        elif command == "delete":
            print(delete(args, book))
        # elif command == "find":      # відкладена
        #     print(find(args, book))

        # Find
        elif command == "find-contact":
            print(find_contacts(args, book))

        # Phone
        elif command == "add":
            print(add_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))  #
        elif command == "change":
            print(change_contact(args, book))

        # Birthday
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "delete-birthday":
            print(delete_birthday(args, book))
        elif command == "birthdays":
            birthdays(args, book)
            
        # Email
        elif command == "add-email":
            print(add_email(args, book))
        elif command == "email":
            print(show_email(args, book))
        elif command == "delete-email":
            print(delete_email(args, book))

        # Address
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "edit-address":
            print(edit_address(args, book))
        elif command == "show-address":
            print(show_address(args, book))
        elif command == "remove-address":
            print(remove_address(args, book))
        # Note
        elif command == "add-note":
            print(new_note(notes))
        elif command == "edit-note":
            print(edit_note(notes))
        elif command == "delete-note":
            print(delete_note(notes))
        elif command == "show-notes":
            print(show_notes(notes))
            print("=" * 50)

        else:
            print('Invalid command. Enter "help" for help')


if __name__ == "__main__":
    main()

# Comment
