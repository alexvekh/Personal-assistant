from src.classes import Record, Phone, Birthday, Email
from datetime import datetime
from collections import defaultdict

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
        return f"{name} not found."

def get_phones(record):
    """
    Function to retrieve phones from a record.

    Args:
        record: Record object.

    Returns:
        String with phone numbers.
    """
    res = [phone.value for phone in record.phones]
    if res:
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
        return "No email"

if __name__ == "__main__":
    contacts_book = {}

    while True:
        user_input = input("Enter command: ")
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        command, *arguments = parse_input(user_input)

        if command == "add":
            result = add_contact(arguments, contacts_book)
            print(result)
        elif command == "change":
            result = change_contact(arguments, contacts_book)
            print(result)
        elif command == "find":
            result = find_contact_by_field(arguments, contacts_book)
            print(result)
        elif command == "change_field":
            result = change_contact_field(arguments, contacts_book)
            print(result)
        else:
            print("Unknown command. Please try again or type 'exit' to quit.")
