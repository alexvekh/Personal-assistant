
from src.classes import Record, Phone, Birthday, Email
from datetime import datetime
from collections import defaultdict

from re import fullmatch


def input_error(func):
    """
    Decorator to handle input errors gracefully.

    Args:
        func: Function to be decorated.

    Returns:
        Decorated function.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Please provide a name."
        except IndexError as e:
            return f"Error: {e}"
        except NameError as e:
            return f"Error: {e}"
        except TypeError as e:
            return f"Error: {e}"
    return inner

@input_error
def parse_input(user_input):
    """
    Function to parse user input into command and arguments.

    Args:
        user_input: String entered by the user.

    Returns:
        Tuple where the first element is the command and the rest are arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def find_contacts(book, field, value):
    """
    Function to search for contacts by a given field and value.

    Args:
        book: Dictionary with contacts.
        field: Field to search by (name, phone, birthday, email).
        value: Value to search for.

    Returns:
        List of found contacts.
    """
    if field == "name":
        return [book[value]] if value in book else []
    elif field == "phone":
        return [record for record in book.values() if value in [phone.value for phone in record.phones]]
    elif field == "birthday":
        return [record for record in book.values() if record.birthday and record.birthday.value.strftime("%d.%m.%Y") == value]
    elif field == "email":
        return [record for record in book.values() if value in [email.value for email in record.emails]]
    else:
        return []

def show_found_contacts(contacts):
    """
    Function to display information about found contacts.

    Args:
        contacts: List of found contacts.

    Returns:
        String with information about found contacts.
    """
    res = []
    for record in contacts:
        res.append(f"{record.name}:")
        res.append(f"  Phones: {get_phones(record)}")
        res.append(f"  Emails: {get_emails(record)}")
        res.append(f"  Birthday: {record.birthday.value.strftime('%d.%m.%Y') if record.birthday else 'Not set'}")
        res.append(f"  Note: {record.note if record.note else 'No note'}")
    return "\n".join(res)

@input_error
def add_contact(args, book):
    """
    Function to add a new contact.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the addition result.
    """
    name, phone, email = args
    if len(phone) != 10 or not phone.isdigit():
        return "Error: Invalid phone number format. Please enter a 10-digit number."
    record = Record(name)
    record.add_phone(phone)
    record.add_email(email)
    book[name] = record
    return "Contact added."

@input_error
def change_contact(args, book):
    """
    Function to change an existing contact.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the change result.
    """
    name, field, new_value = args
    if name in book:
        record = book[name]
        if field == "phone":
            record.phones = [Phone(new_value)]
        elif field == "birthday":
            record.birthday = Birthday(new_value)
        elif field == "email":
            record.emails = [Email(new_value)]
        elif field == "note":
            record.note = new_value
        return f"Contact {name} updated."
    else:
        return f"Sorry, {name} not found."

@input_error
def find_contact_by_field(args, book):
    """
    Function to find a contact by a specified field and value.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the found contact.
    """
    field, value = args
    found_contacts = find_contacts(book, field, value)
    if found_contacts:
        return show_found_contacts(found_contacts)
    else:
        return f"No contacts found by {field} with value {value}."

@input_error
def change_contact_field(args, book):
    """
    Function to change a specified field of a contact.

    Args:
        args: Command line arguments.
        book: Dictionary with contacts.

    Returns:
        String with information about the change result.
    """
    name, field, new_value = args
    if name in book:
        record = book[name]
        if field == "phone":
            record.phones = [Phone(new_value)]
        elif field == "birthday":
            record.birthday = Birthday(new_value)
        elif field == "email":
            record.emails = [Email(new_value)]
        elif field == "note":
            record.note = new_value
        return f"Contact {name} updated."
    else:
# <<<<<<< find_edit_contact#                        ADDED Maricka. I WANT TO CHECK
#         return f"{name} not found."

# def get_phones(record):
#     """
#     Function to retrieve phones from a record.

#     Args:
#         record: Record object.

#     Returns:
#         String with phone numbers.
#     """
#     res = [phone.value for phone in record.phones]
#     if res:
##############################################################=======
        return "Sorry, {name} doesn't exist. Use 'add' for append this contact."
    
def get_phones(record):   # Service for get phones from record
    res = []
    for phone in record.phones:
        res.append(phone.value)
    if res[0]:
#################################################################>>>>>>> main
        return ','.join(res)
    else:
        return "No phone"

def get_emails(record):
    """
    Function to retrieve emails from a record.

    Args:
        record: Record object.

    Returns:
        String with email addresses.
    """
    res = [email.value for email in record.emails]
    if res:
        return ','.join(res)
    else:
# ######################################<<<<<<< find_edit_contact       ADDED Maricka. I WANT TO CHECK
#         return "No email"

# if __name__ == "__main__":
#     contacts_book = {}

#     while True:
#         user_input = input("Enter command: ")
#         if user_input.lower() == "exit":
#             print("Exiting...")
#             break

#         command, *arguments = parse_input(user_input)

#         if command == "add":
#             result = add_contact(arguments, contacts_book)
#             print(result)
#         elif command == "change":
#             result = change_contact(arguments, contacts_book)
#             print(result)
#         elif command == "find":
#             result = find_contact_by_field(arguments, contacts_book)
#             print(result)
#         elif command == "change_field":
#             result = change_contact_field(arguments, contacts_book)
#             print(result)
#         else:
#             print("Unknown command. Please try again or type 'exit' to quit.")
# =======##################################################################
        return "Sorry, {name} isn't exist. \nUse 'add' for add this contact to book."
    
def birthdays(book):
    book.get_birthdays_per_week()

@input_error
def add_address(args, book):
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.add_address(street, house_number, city, postal_code, country)
        return "Address added."
    else:
        return "Contact does not exist."

@input_error
def show_address(args, book):
    name = args[0]
    if name in book.data:
        record = book.data[name]
        addresses = record.addresses
        if addresses:
            address_str = "\n".join([f"{address}" for address in addresses])
            return f"Addresses for {name}:\n{address_str}"
        else:
            return f"No addresses found for {name}."
    else:
        return "Contact does not exist."

@input_error
def edit_address(args, book):
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.edit_address(street, house_number, city, postal_code, country)
        return "Address edited."
    else:
        return "Contact does not exist."

@input_error
def remove_address(args, book):
    name, = args
    if name in book.data:
        record = book.data[name]
        record.remove_address()
        return "Address removed."
    else:
        return "Contact does not exist."

   
def show_commands():
    commands = {
        "help": "for help",
        "hello": "just fo say 'Hi!'",
        "add name phone": "for add new contact",
        "change name phone": "for change exist contact",
        "phone name": "for get phone number",
        "add-birthday name": "for add birthday",
        "show_birthday name": "for get birthday",
        "add-address name street house_number city postal_code country": "for add an address to a contact",
        "remove-address name index": "for remove an address from a contact by its index",
        "edit-address name index [street] [house_number] [city] [postal_code] [country]": "for edit an address of a contact",
        "remove-address name index": "for remove an address from a contact by its index",
        "birthdays": "for get birtdays next week ",
        "all": "for get all contact list",
        "exit": "for exit",
    }
    res = []
    for command, desctiption in commands.items():
        res.append("{:<19} {} ".format(command, desctiption))
    return "\n".join(res)

def new_note(notes):
    while True:
        title = input("Type the title here ===>  ")
        if title:
            break
        else:
            print("Title cannot be empty.")
            continue
    text = input("Type the text here ===>  ")
    while True:
        tags = input("Type tags here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  ").split()
        if all(fullmatch(r'\#\w+', tag) for tag in tags):
            notes.append(Note(title, text, tags))
            return "Note has been added"
        else:
            print("Wrong format.")

def edit_note(notes):
    if notes:
        note = find_note(notes)
        answer = input("Type <y> if you want to change the title or any else key to continue ===>  ")
        if answer == 'y':
            note.data["title"] = input("Type the new title here ===>  ")
        answer = input("Type <y> if you want to change the text or any else key to continue ===>  ")
        if answer == 'y':
            note.data["text"] = input("Type the new text here ===>  ")
        answer = input("Type <y> if you want to change tags or any else key to continue ===>  ")
        if answer == 'y':
            while True:
                tags = input("Type tags here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  ").split()
                if all(fullmatch(r'\#\w+', tag) for tag in tags):
                    note.data["tags"] = tags
                    break
                else:
                    print("Wrong format.")
        return "Note has been edited."
    return "No notes added."

def delete_note(notes):
    if notes:
        note = find_note(notes)
        del notes[notes.index(note)]
        return "Note has been deleted."
    return "No notes added."

def find_note(notes):
    note_dict = dict(zip(range(1, len(notes) + 1), notes))
    for number, note in note_dict.items():
        print(str(number) + ': ' + note.data["title"])
    while True:
        answer = input("Type the number of note ===>  ")
        if answer.isdigit() and 1 <= int(answer) <= len(notes):
            return notes[int(answer) - 1]
        else:
            print(f"Must be the number between 1 and {len(notes)}")
            continue

def show_notes(notes):
    if notes:
        while True:
            answer = input("What are we looking for? (a for all notes and s for specific) a/s ===>  ")
            if answer == 'a':
                notes_to_print = notes
                return '\n'.join(str(note) for note in notes_to_print)
            elif answer == 's':
                while True:
                    key = input("What element do you want to search by? (title/text/tags) ===>  ")
                    if key in ('title', 'text'):
                        element = input(f"Type the {key} you want to look for ===>  ")
                        notes_to_print = tuple(filter(lambda note: element in note.data[key], notes))
                        return '\n'.join(str(note) for note in notes_to_print) if notes_to_print else "No such notes."
                    elif key == 'tags':
                        while True:
                            tags = input("Type the tag(s) you want to look for (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  ").split()
                            if all(fullmatch(r'\#\w+', tag) for tag in tags):
                                break
                            else:
                                print("Wrong format.")
                                continue
                        notes_to_print = tuple(filter(lambda note: all(tag in note.data["tags"] for tag in tags), notes))
                        return '\n'.join(str(note) for note in notes_to_print) if notes_to_print else "No such notes."
                    else:
                        print("Wrong format.")
                        continue
            else:
                print("Wrong format.")
                continue
    else:
        return "No notes added."

