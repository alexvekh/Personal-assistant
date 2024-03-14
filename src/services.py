from src.classes import Record, Note
from re import fullmatch

# Decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Give me a name please."
        except IndexError as e:
            return f"Error: {e}"
        except NameError as e:
            return f"Error: {e}"
        except TypeError as e:
            return f"Error: {e}"
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, book):
    name, phone = args
    if name in book:
        record = book[name]
        record.phones = []
        record.add_phone(phone)  #Phone(phone)
        return "Contact updated."
    else:
        return "Sorry, " + name + " isn't exist."

@input_error
def show_phone(args, book):
    name, = args
    if name in book:
        record = book[name]
        # Out         print(record)
        res = []
        for phone in record.phones:
            res.append(phone.value)
        return f"{name}: {','.join(res)}"
    else:
        return "Sorry, {name} doesn't exist. Use 'add' for append this contact."
    
def get_phones(record):   # Service for get phones from record
    res = []
    for phone in record.phones:
        res.append(phone.value)
    if res[0]:
        return ','.join(res)
    else:
        return "No phone"

def show_all(book):
    res = []
    res.append("{:^20}".format("CONTACTS"))
    res.append("{:^20}".format("-"*10))
    for name, record in book.items():
        res.append("{:<8} {} ".format(name+":", get_phones(record)))
    res.append("{:^20}".format("="*20))
    return "\n".join(res)

@input_error
def add_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return f"{name}'s birthday added"
    else:
        return f"Sorry, {name} isn't exist. Use 'add' for add this contact."

@input_error
def show_birthday(args, book):
    name, = args
    if name in book:
        record = book[name]
        if record.birthday != None:
            birthday = record.birthday.value.strftime("%d.%m.%Y")
            return f"{name}'s birthday is {birthday}"
        else:
            return f"{name}'s birthday isn't recorded"
    else:
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
