def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    cmd = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a name and phone number."
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_phone(args, contacts):
    if not args:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"{name}: {contacts[name]}"

@input_error
def list_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            response = add_contact(args, contacts)
            print(response)
        elif command == "change":
            response = change_contact(args, contacts)
            print(response)
        elif command == "phone":
            response = get_phone(args, contacts)
            print(response)
        elif command == "all":
            response = list_contacts(contacts)
            print(response)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
