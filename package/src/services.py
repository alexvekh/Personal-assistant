from .classes import Record, Birthday, Email, Phone, Note, Note
from .check import *
from .classes import Record
from .validate import email_is_valid
from termcolor import colored
from re import fullmatch


def input_error(func):
    """Decorator for catching typos and wrong command formats"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return "Wrong format. Use 'help' for additional imformation."

    return inner


@input_error
def parse_input(user_input):
    """Splits input to command and arguments"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Phone -----------------------------------------------------------------------------
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
    name, phone = args
    if len(phone) != 10 or not phone.isdigit():
        return colored(
            "Error: Invalid phone number format. Please enter a 10-digit number.",
            "red",
            attrs=["bold"],
        )

    record = Record(name)
    record.add_phone(phone)
    book[name] = record
    return colored("✅ Contact added.", "green", attrs=["bold"])


def show_phone(args, book):
    """Shows contact`s phone number"""
    (name,) = args
    if name in book:
        record = book[name]

        res = []
        for phone in record.phones:
            res.append(phone.value)
        return f"{name}: {','.join(res)}"
    else:
        return colored(
            "Sorry, {name} doesn't exist. Use 'add' to append this contact.",
            "red",
            attrs=["bold"],
        )


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
        return colored(f"\U0001F4DD Contact {name} updated.", "cyan", attrs=["bold"])
    else:
        return colored(f"\U000026D4 Sorry, {name} not found.", "red", attrs=["bold"])


def get_phones(record):  # Service for get phones from record
    res = []
    for phone in record.phones:
        res.append(phone.value)
    if res[0]:
        return ",".join(res)
    else:
        return colored("📵 No phone", "yellow", attrs=["bold"])


@input_error
def show_all(book):
    """Shows all information about every contact"""
    res = ["{:^60}".format("CONTACTS"), "{:-^60}".format("")]
    for name, record in book.items():
        emails = ", ".join(email.value for email in record.emails) or "No Email"
        phones = ", ".join(phone.value for phone in record.phones) or "No Phone"
        birthday = (
            record.birthday.value.strftime("%d.%m.%Y")
            if record.birthday
            else "No Birthday"
        )
        addresses = (
            "; ".join(
                f"{address.street}, {address.house_number}, {address.city}, {address.postal_code if address.postal_code else ''}, {address.country if address.country else ''}"
                for address in record.addresses
            )
            or "No Address"
        )
        money = book[name].money

        contact_info = f"👤 Name: {name}\n📞 Phone: {phones}\n📧 Email: {emails}\n🎂 Birthday: {birthday}\n🏠 Address: {addresses}\n💰 Money: {money} dollars"
        res.append(contact_info)
        res.append("{:-^60}".format(""))  # Додав розділювач між контактами
    return "\n".join(res)


@input_error
def show_table(book):
    """Shows the address book in a table format"""
    res = ["{:^125}".format("CONTACTS"), "{:-^142}".format("")]

    for name, record in book.items():
        emails = ", ".join(email.value for email in record.emails) or "No Email"
        phones = ", ".join(phone.value for phone in record.phones) or "No Phone"
        birthday = (
            record.birthday.value.strftime("%d.%m.%Y")
            if record.birthday
            else "No Birthday"
        )
        addresses = (
            "; ".join(
                f"{address.street}, {address.house_number}, {address.city}, {address.postal_code if address.postal_code else ''}, {address.country if address.country else ''}"
                for address in record.addresses
            )
            or "No Address"
        )
        money = book[name].money
        contact_info = "👤 {:<12} 📞 {:<16} 📧 {:<27} 🎂 {:<15} 🏠 {:<45} 💰 {:<6}".format(name, phones, emails, birthday, addresses, money)
        res.append(contact_info)
        res.append("{:-^142}".format(""))  # Додав розділювач між контактами
    return "\n".join(res)


# Find contact info by name ------------------------------------------------
@input_error
def find(args, book):
    """Finds a contact in the address book"""
    name = args[0]
    if name in book:
        emails = ", ".join(email.value for email in book[name].emails) or "No Email"
        phones = ", ".join(phone.value for phone in book[name].phones) or "No Phone"
        birthday = (
            book[name].birthday.value.strftime("%d.%m.%Y")
            if book[name].birthday
            else "No Birthday"
        )
        addresses = (
            "; ".join(
                f"{address.street}, {address.house_number}, {address.city}, {address.postal_code if address.postal_code else ''}, {address.country if address.country else ''}"
                for address in book[name].addresses
            )
            or "No Address"
        )
        money = book[name].money

        
        contact_info = f"👤 Name: {name}\n📞 Phone: {phones}\n📧 Email: {emails}\n🎂 Birthday: {birthday}\n🏠 Address: {addresses}\n💰 Money: {money} dollars"

        return contact_info
    else:
        return colored(f"\U000026D4 Contact {name}  not found.", "red", attrs=["bold"])


# Birthday ----------------------------------------------------------------
@input_error
def add_birthday(args, book):
    """Adds birthday to contact info"""
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return colored(f"🎉 {name}'s birthday added", "green", attrs=["bold"])
    else:
        return colored(
            f"❌ Sorry, {name} doesn't exist. Use 'add' to add this contact.",
            "red",
            attrs=["bold"],
        )


@input_error
def show_birthday(args, book):
    """Shows contact`s birthday"""
    (name,) = args
    if name in book:
        record = book[name]
        if record.birthday != None:
            birthday = record.birthday.value.strftime("%d.%m.%Y")
            return colored(
                f"🎂 {name}'s birthday is {birthday}", "cyan", attrs=["bold"]
            )
        else:
            return colored(
                f"❓ {name}'s birthday isn't recorded", "yellow", attrs=["bold"]
            )
    else:
        return colored(
            f"❌ Sorry, {name} doesn't exist. \nUse 'add' to add this contact to the book.",
            "red",
            attrs=["bold"],
        )


@input_error
def change_birthday(args, book):
    """Changes contact`s birthday"""
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return colored(f"🔄 {name}'s birthday changed", "green", attrs=["bold"])
    else:
        return colored(f"❌ Sorry, {name} doesn't exist.", "red", attrs=["bold"])


@input_error
def delete_birthday(args, book):
    """Deletes contact`s birthday"""
    (name,) = args
    if name in book:
        record = book[name]
        if record.birthday != None:
            res = record.remove_birthday()
            return res
        else:
            return colored(f"🚫 No birthday for {name}", "yellow", attrs=["bold"])
    else:
        return colored(
            f"❌ Sorry, {name} doesn't exist. \nUse 'add' to add this contact to book.",
            "red",
            attrs=["bold"],
        )


@input_error
def birthdays(args, book):
    """Returns all birthdays in a certain amount of days"""
    if args:
        days = args[0]
        book.get_birthdays_by_days(days)
    else:
        book.get_birthdays_per_week()


# Email  ----------------------------------------------------------------------
@input_error
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
        return ",".join(res)
    else:
        return "Sorry, {name} doesn't exist. Use 'add' to append this contact."


# "add-email name email": "adding email to existing contact"
@input_error
def add_email(args, book):
    """
    Function to add an email to a contact record.

    Args:
        args (tuple): A tuple containing the name (str) and email (str) to add.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A confirmation message of adding the email.
    """
    name, email = args
    if name in book:
        record = book[name]
        record.emails.append(Email(email))
        return colored(f"✅ {name}'s email added successfully", "green", attrs=["bold"])
    else:
        return colored(
            f"❌ Sorry, {name} doesn't exist. \nUse 'add' to add this contact to the book.",
            "red",
            attrs=["bold"],
        )


# "email name": "get email of specific contact"
@input_error
def show_email(args, book):
    """
    Function to get the email of a specific contact.

    Args:
        args (tuple): A tuple containing the name (str) of the contact.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A string containing the contact's name and their email(s).

    """

    name = args[0]

    if name in book:
        record = book[name]
        res = []
        for email in record.emails:
            res.append(email.value)
        return f"{name}: {','.join(res)}"
    else:

        return colored(
            f"❌ Sorry, {name} doesn't exist. \nUse 'add' to add this contact to the book.",
            "red",
            attrs=["bold"],
        )


@input_error
def change_email(args, book):
    """Changes contact`s email"""
    name = args[0]
    if name in book:
        if book[name].emails:
            for number, email in enumerate(book[name].emails, 1):
                print(f"{number}: {email}")
            while True:
                answer = input("Type the number of email you want to change ===>  ")
                if answer.isdigit() and 1 <= int(answer) <= len(book[name].emails):
                    while True:
                        new_email = input("Enter new email ==>  ")
                        if email_is_valid(new_email):
                            book[name].emails[int(answer) - 1] = Email(new_email)
                            return colored(
                                "Email has been changed.", "green", attrs=["bold"]
                            )
                        else:
                            print(
                                colored(
                                    "Seems like this email is incorrect. Try again.",
                                    "red",
                                )
                            )
                else:
                    print(
                        colored(
                            f"Must be the number between 1 and {len(book[name].emails)}",
                            "red",
                        )
                    )
        else:
            return colored("Contact has no emails.", "red")
    else:
        return colored("No such contact.", "red")


# "change-email name email": "changing email of existing contact"
@input_error
def delete_email(args, book):
    """
    Function to delete an email from an existing contact.

    Args:
        args (tuple): A tuple containing the name (str) of the contact and the email (str) to delete.
        book (dict): A dictionary representing the address book.

    Returns:
        str: A confirmation message of deleting the email.

    Raises:
        ValueError: If the input arguments are not in the correct format.
    """
    name, email_to_delete = args
    if name in book:
        record = book[name]
        for email in record.emails:
            if email.value == email_to_delete:
                record.emails.remove(email)
                return colored(
                    f"🗑️ Email {email_to_delete} deleted from {name}'s contacts.",
                    "green",
                    attrs=["bold"],
                )
        return colored(
            f"🔍 Email {email_to_delete} not found in {name}'s contacts.",
            "yellow",
            attrs=["bold"],
        )
    else:
        print(
            colored(
                f"🚫 Sorry, {name} doesn't exist. Use 'add' to append this contact.",
                "red",
                attrs=["bold"],
            )
        )


# Address -----------------------------------------------------------------
@input_error
def add_address(args, book):
    """Adds contact`s address"""
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.add_address(street, house_number, city, postal_code, country)
        return colored("🏠 Address added.", "green", attrs=["bold"])
    else:
        return colored("🚫 Contact does not exist.", "red", attrs=["bold"])


@input_error
def show_address(args, book):
    """Shows contact`s address"""
    name = args[0]
    if name in book.data:
        record = book.data[name]
        addresses = record.addresses
        if addresses:
            address_str = "\n".join([f"{address}" for address in addresses])
            return colored(
                f"🏠 Addresses for {name}:\n{address_str}", "blue", attrs=["bold"]
            )
        else:
            return colored(f"❌ No addresses found for {name}.", "red")

    else:
        return colored("❌ Contact does not exist.", "red")


def edit_address(args, book):
    """Changes contact`s address"""
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.edit_address(street, house_number, city, postal_code, country)
        return colored("Address edited.", "green", attrs=["bold"])
    else:
        return colored("❌ Contact does not exist.", "red")


def remove_address(args, book):
    """Deletes contact`s address"""
    (name,) = args
    if name in book.data:
        record = book.data[name]
        record.remove_address()
        return colored("🗑️ Address removed.", "yellow", attrs=["bold"])
    else:
        return colored("❌ Contact does not exist.", "red")


# Note --------------------------------------------------------------------


def new_note(notes):
    """Adds new note with title, text and tag(s)"""
    while True:
        title = input("Type the title here ===>  ")
        if title:
            break
        else:
            print("Title cannot be empty.")
            continue
    text = input("Type the text here ===>  ")
    while True:
        tags = input(
            "Type tag(s) here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
        ).split()
        if all(fullmatch(r"\#\w+", tag) for tag in tags):
            notes.append(Note(title, text, tags))
            return "Note has been added"
        else:
            print("Wrong format.")


def edit_note(notes):
    """Allows user to edit any part of his note"""
    if notes:
        note = find_note(notes)
        answer = input(
            "Type <y> if you want to change the title or any else key to continue ===>  "
        )
        if answer == "y":
            while True:
                answer = input("Type the new title here ===>  ")
                if answer:
                    note.data["title"] = input("Type the new title here ===>  ")
                else:
                    "Title cannot be empty."
        answer = input(
            "Type <y> if you want to change the text or any else key to continue ===>  "
        )
        if answer == "y":
            note.data["text"] = input("Type the new text here ===>  ")
        answer = input(
            "Type <y> if you want to change tag(s) or any else key to continue ===>  "
        )
        if answer == "y":
            while True:
                tags = input(
                    "Type tag(s) here (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
                ).split()
                if all(fullmatch(r"\#\w+", tag) for tag in tags):
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
    """Finds a certain note in list"""
    note_dict = dict(zip(range(1, len(notes) + 1), notes))
    for number, note in note_dict.items():
        print(str(number) + ": " + note.data["title"])
    while True:
        answer = input("Type the number of note ===>  ")
        if answer.isdigit() and 1 <= int(answer) <= len(notes):
            return notes[int(answer) - 1]
        else:
            print(f"Must be the number between 1 and {len(notes)}")
            continue


def show_notes(notes):
    """Shows ceratin notes from all"""
    if notes:
        while True:
            answer = input(
                "What are we looking for? (a for all notes and s for specific) a/s ===>  "
            )
            if answer == "a":
                notes_to_print = notes
                return "\n".join(str(note) for note in notes_to_print)
            elif answer == "s":
                while True:
                    key = input(
                        "What element do you want to search by? (title/text/tags) ===>  "
                    )
                    if key in ("title", "text"):
                        element = input(f"Type the {key} you want to look for ===>  ")
                        notes_to_print = tuple(
                            filter(lambda note: element in note.data[key], notes)
                        )
                        return (
                            "\n".join(str(note) for note in notes_to_print)
                            if notes_to_print
                            else "No such notes."
                        )
                    elif key == "tags":
                        while True:
                            tags = input(
                                "Type the tag(s) you want to look for (for example: <#tag1> <#multiple_word_tag_2> <#tag3>)  ===>  "
                            ).split()
                            if all(fullmatch(r"\#\w+", tag) for tag in tags):
                                break
                            else:
                                print("Wrong format.")
                                continue
                        notes_to_print = tuple(
                            filter(
                                lambda note: all(
                                    tag in note.data["tags"] for tag in tags
                                ),
                                notes,
                            )
                        )
                        return (
                            "\n".join(str(note) for note in notes_to_print)
                            if notes_to_print
                            else "No such notes."
                        )
                    else:
                        print("Wrong format.")
                        continue
            else:
                print("Wrong format.")
                continue
    else:
        return "No notes added."


# Money -----------------------------------------------------------------------------
@input_error
def deposit(args, book):
    """Adds a specific amount of money to person`s wallet"""
    name, amount = args
    if name in book:
        if amount.isdigit() and int(amount) > 0:
            amount = int(amount)
            record = book[name]
            record.deposit(amount)
            return "Deposit successful."
        else:
            return "Invalid amount."
    else:
        return "No such contact."


@input_error
def withdraw(args, book):
    """Substracts a specific amount of money from person`s wallet"""
    name, amount = args
    if name in book:
        if amount.isdigit() and int(amount) > 0:
            amount = int(amount)
            record = book[name]
            if record.money >= amount:
                record.withdraw(amount)
                return "Withdraw successful."
            else:
                return "You cannot withdraw more than you have."
        else:
            return "Invalid amount."
    else:
        return "No such contact."


@input_error
def get_money(args, book):
    """Returns the amount of money in contact`s wallet"""
    name = args[0]
    if name in book:
        return f"{name} has {book[name].money} dollars."
    else:
        return "No such contact."


def bank(book):
    """Returns the sum of all contacts` money"""
    return sum(book[name].money for name in book)


def show_commands():
    groups = {
        "General Commands": {
            "help": "Display all available commands.",
            "exit": "Exit the program.",
        },
        "Contact Management": {
            "add [name] [phone]": "Add a new contact.",
            "delete [name]": "Delete an existing contact.",
            "change [name] [existing phone][new phone]": "Change the phone number of an existing contact.",
            "all": "Display all contacts.",
        },
        "Phone Management": {
            "phone [name]": "Display the phone number of a specific contact."
        },
        "Birthday Management": {
            "add-birthday [name] [birthday]": "Add a birthday for a contact.",
            "show-birthday [name]": "Show the birthday of a specific contact.",
            "change-birthday [name] [new birthday]": "Change birthday for your contact",
            "delete-birthday [name]": "Delete a contact's birthday.",
            "birthdays": "Displays all the birthdays for upcoming week",
            "birtdays [number of days]": "Displays all upcoming birthdays within the specified number of days."

        },
        "Email Management": {
            "add-email [name] [email]": "Add an email to a contact.",
            "email [name]": "Show the email of a specific contact.",
            "change-email [name]": "Update your contact's email.",
            "delete-email [name]": "Remove an email from a contact.",
        },
        "Address Management": {
            "add-address [name] [street] [house_number] [city] [postal_code] [country]": "Add an address to a contact.",
            "change-address [name] [new details]": "Edit an existing address.",
            "show-address [name]": "Display the address of a specific contact.",
            "delete-address [name]": "Delete an address from a contact.",
        },
        "Note Management": {
            "add-note": "Add a note to a contact.",
            "show-notes": "Display notes all or specific note.",
            "edit-note": "Edit an already existing note.",
            "delete-note": "Remove a note.",
        },
        "Money Management": {
            "deposit [name] [amount]": "deposit to person`s wallet",
            "withdraw [name] [amount]": "withdraw from person`s wallet",
            "money [name]": "show current person`s wallet balance",
            "bank": "show sum of all wallets",
        },
    }

    for group_name, commands in groups.items():
        print(f"\n{group_name}:")
        for command, description in commands.items():
            print(f"  {command:40} - {description}")
    return ""


@input_error
def delete(args, book):
    if len(args) == 1:  # if in args 1 arg
        arg = args[0]  # get arg from []
        res = book.delete(arg)
        return res
    elif len(args) == 2:
        name, field = args
        record = book.find(name)
        if field == "phones":
            res = record.remove_phones()
            return res
        elif field == "birthday":
            res = record.remove_birthday()
            return res
        elif field == "email":
            res = record.remove_email()
            return res
        elif field == "address":
            res = record.remove_address()
            return res
        elif field == "notes":
            res = record.remove_notes()
            return res


def national_symbol():
    """Glory to Ukraine"""
    print('                                                        $$             ')
    print('                                                       $$$$           ')
    print('                                           $$$         $$$$         $$$')
    print('                                           $$$$$       $$$$       $$$$$')
    print('                                           $$$ $$      $$$$      $$$$$$')
    print('                                           $$$  $$     $$$$     $$  $$$')
    print('                                           $$$   $$     $$     $$   $$$')
    print('                                           $$$   $$     $$     $$   $$$')
    print('                                           $$$   $$     $$     $$   $$$')
    print('                                           $$$   $$    $$$$    $$   $$$')
    print('                                           $$$   $$    $$$$    $$   $$$')
    print('                                           $$$  $$    $$$$$$    $$  $$$')
    print('                                           $$$$$$     $$  $$     $$$$$$')
    print('                                           $$$ $$$   $$    $$   $$$ $$$')
    print('                                           $$$  $$$$$$$    $$$$$$$  $$$')
    print('                                           $$$     $$ $$$$$$ $$     $$$')
    print('                                           $$$     $$   $$   $$     $$$')
    print('                                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('                                                   $$$  $$  $$$        ')
    print('                                                    $$$ $$ $$$         ')
    print('                                                     $$$$$$$$          ')
    print('                                                       $$$$            ')


