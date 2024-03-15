from src.classes import AddressBook
from termcolor import colored
from src.services import *

# from src.services import parse_input, add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays, show_commands, add_address, edit_address, show_address, remove_address, new_note, edit_note, delete_note, show_notes

from src.disk import save_to_json, load_from_json

command_keywords = {
    "add": ["додати", "new", "new contact"],
    "delete": ["видалити", "remove"],
    "change": ["редагувати", "edit"],
    "add-address": ["address", "new address", "адреса"],
    "delete-address":["address", "new address", "видалити адресу"]
    # Можна ще додати ключові слова, 
}


def guess_command(user_input):
    user_input_lower = user_input.lower()
    max_score = 0
    guessed_commands = []

    for command, keywords in command_keywords.items():
        score = sum(keyword in user_input_lower for keyword in keywords)
        if score > max_score:
            max_score = score
            guessed_commands = [command]
        elif score == max_score and score != 0:
            guessed_commands.append(command)

    if len(guessed_commands) == 1:
        return guessed_commands[0]
    elif len(guessed_commands) > 1:
        print("Found several possible commands: ")
        for i, cmd in enumerate(guessed_commands, start=1):
            print(f"{i}. {cmd}")
        choice = input("Please enter the command number you had in mind: ")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(guessed_commands):
                return guessed_commands[choice_index]
        except ValueError:
            pass
    return "unknown"





def main():
    # book = AddressBook()
    # print(book)
    book, notes = load_from_json()
    # print("main load", book)
    # print("main new", book)

    print("Welcome to the assistant bot!")
    # Після визначення функції main() і перед while True:
    while True:
        user_input = input("Enter a command ===>  ")
        guessed_command = guess_command(user_input)
        if guessed_command != "unknown":
            print(f"Did you mean '{guessed_command}'? Y/n")
            confirmation = input().strip().lower()
            if confirmation in ['', 'y', 'yes']:
                command = guessed_command
                args = user_input.split()[1:]  # Оновлення: зберігаємо аргументи, відокремлюючи їх від команди
            else:
                print("Please, try to specify your command more clearly.")
                continue
        else:
            command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            save_to_json(book, notes)
            print(colored("Good bye!", 'cyan', attrs=['bold']))
            break
        elif command == "hello":
            print(colored("How can I help you?", 'white', 'on_blue', attrs=['bold']))
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

#Phone

        elif command == "add":
            if len(args) >= 2:
                response = add_contact(args, book) 
                print(colored("✅ " + response, 'green', attrs=['bold']))
            else:
                print(colored("Error: 'add' command requires a name and a phone number.", 'red'))
        elif command == "phone":
            print(show_phone(args, book))  #
        elif command == "change":
            print(change_contact(args, book))

        # Birthday
        elif command == "add-birthday":
            print(colored(add_birthday(args, book), 'green', attrs=['bold']))
        elif command == "show-birthday":
            print(show_birthday(args, book),'magenta')
        elif command == "change-birthday":
            print(change_birthday(args, book))
        elif command == "delete-birthday":
            print(delete_birthday(args, book))
        elif command == "birthdays":
            birthdays(args, book)
            
        # Email
        elif command == "add-email":
            print(colored(add_email(args, book), 'cyan', attrs=['bold']))
        elif command == "email": 

            print(show_email(args, book))
        elif command == "delete-email":
            print(colored(delete_email(args, book), 'red', attrs=['bold']))

        # Address
        elif command == "add-address":
            print(colored(add_address(args, book), 'green', attrs=['bold']))
        elif command == "change-address":
            print(edit_address(args, book))
        elif command == "show-address":

            print(show_address(args,book))
        elif command == "delete-address":
            print(colored(remove_address(args, book), 'red', attrs=['bold']))
# Note
        elif command == "add-note":
            print(colored(show_notes(notes), 'green', attrs=['bold']))
        elif command == "edit-note":
            print(edit_note(notes))
        elif command == "delete-note":
            print(colored(delete_note(notes), 'red'), attrs=['bold'])
        elif command == "show-notes":
            print(show_notes(notes))
            print("=" * 50)

        else:
            print('Invalid command. Enter "help" for help')


if __name__ == "__main__":
    main()

# Comment