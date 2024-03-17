try:
    from src.classes import AddressBook
    from src.services import *
    from src.disk import save_to_json, load_from_json
except ModuleNotFoundError:
    from .src.classes import AddressBook
    from .src.services import *
    from .src.disk import save_to_json, load_from_json
from termcolor import colored
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML


class FirstWordCompleter(Completer):
    def __init__(self, word_list):
        self.word_list = word_list

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        word = text.split(" ")[0]

        if " " not in text:
            for word in self.word_list:
                if word.startswith(text):
                    yield Completion(word, start_position=-len(text))


commands = [
    'close', 'exit', 'good bye', 'hello', 'help', 'all', 'delete',
    'find-contact', 'add', 'phone', 'change', 'add-birthday', 'show-birthday',
    'change-birthday', 'delete-birthday', 'birthdays', 'add-email', 'email',
    'change-email', 'delete-email', 'add-address', 'change-address',
    'show-address', 'delete-address', 'add-note', 'edit-note', 'delete-note',
    'show-notes', 'deposit', 'withdraw', 'money', 'bank'
]


def main():
    try:
        result = load_from_json()
        if isinstance(result, tuple) and len(result) == 2:
            book, notes = result
        else:
            book = result
            notes = []
    except Exception as e:
        print(f"Failed to load data: {e}")
        book = AddressBook()
        notes = []

    print("Welcome to the assistant bot!")
    session = PromptSession(completer=FirstWordCompleter(commands))
    # Після визначення функції main() і перед while True:
    while True:
        user_input = session.prompt(
            HTML("<ansigreen>Enter a command ===></ansigreen> ")
        ).strip()
        parts = user_input.split(" ", 1)
        command = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []
        if command in ["close", "exit", "good bye"]:
            save_to_json(book, notes)
            print(colored("Good bye!", "blue", "on_light_green", attrs=["bold"]))
            break
        elif command == "hello":
            print(
                colored("How can I help you?", "blue", "on_light_green", attrs=["bold"])
            )
        elif command == "help":
            print(show_commands())
        # All
        elif command == "all":
            print(show_table(book))
        elif command == "contacts":
            print(show_all(book))
        elif command == "delete":
            print(delete(args, book))


# Find  c

        elif command == "find-contact":
            print(find(args, book))

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
        elif command == "change-email":
            print(change_email(args, book))
        elif command == "delete-email":
            print(delete_email(args, book))

        # Address
        elif command == "add-address":
            print(add_address(args, book))
        elif command == "change-address":
            print(edit_address(args, book))
        elif command == "show-address":
            print(show_address(args, book))
        elif command == "delete-address":
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

        # Money
        elif command == "deposit":
            print(deposit(args, book))
        elif command == "withdraw":
            print(withdraw(args, book))
        elif command == "money":
            print(get_money(args, book))
        elif command == "bank":
            print(f"{bank(book)} dollars in the bank right now.")

        else:
            print('Invalid command. Enter "help" for help')


if __name__ == "__main__":
    main()
