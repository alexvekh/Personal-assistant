from classes import Record

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
        return "Sorry, {name} isn't exist. Use 'add' for append this contact."
    
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
    
def show_commands():
    commands = {
        "help": "for help",
        "hello": "just fo say 'Hi!'",
        "add name phone": "for add new contact",
        "change name phone": "for change exist contact",
        "phone name": "for get phone number",
        "add-birthday name": "for add birthday",
        "show_birthday name": "for get birthday",
        "birthdays": "for get birtdays next week ",
        "all": "for get all contact list",
        "exit": "for exit",
    }
    res = []
    for command, desctiption in commands.items():
        res.append("{:<19} {} ".format(command, desctiption))
    return "\n".join(res)