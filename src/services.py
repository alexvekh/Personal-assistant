from src.classes import Record, Birthday, AddressBook
from src.check import *
from datetime import datetime
from src.classes import Record

# Decorator
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return f"Error: {e}"
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
    if len(res) > 0:
        return ','.join(res)
    else:
        return "No phones"

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

def change_birthday(args, book):
    name, birthday = args
    if name in book:
        record = book[name]
        record.add_birthday(birthday)
        return f"{name}'s birthday changed"
    else:
        return f"Sorry, {name} isn't exist."



def birthdays(args, book):
    if args:
        days = args[0]
        book.get_birthdays_by_days(days)
    else:
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

def edit_address(args, book):
    name, street, house_number, city, postal_code, country = args
    if name in book.data:
        record = book.data[name]
        record.edit_address(street, house_number, city, postal_code, country)
        return "Address edited."
    else:
        return "Contact does not exist."

def remove_address(args, book):
    name, = args
    if name in book.data:
        record = book.data[name]
        record.remove_address()
        return "Address removed."
    else:
        return "Contact does not exist."
    







@input_error
def find(args, book):
    print(f"шукати {args}")
    arg = args[0]
    if is_looks_date(arg):    # якщо arg схожий на дату
        print(f"Функція буде шукати date {arg}")
        for record in book.values():
            print("record", record)
    #   record виводить 
            if record.birthday:
                print(record.birthday, record.birthday.value, arg, Birthday(arg))
                print(type(record.birthday), type(record.birthday.value), type(arg), type(Birthday(arg)))
                if Birthday(arg) == record.birthday:
                    print(True)
# Треба порівняти birthday з arg і вивести records де це співпадає



    elif is_looks_phone(arg):
        print(f"Функція буде шукати phone {arg}")
        #book.find_in_field("phone", arg)
    elif is_looks_email(arg):
        print(f"Функція буде шукати email {arg}")
        #book.find_in_field("email", arg)
    
    # Address not aveilable to check:
        
    # name
    else:
        try:
            record = book.find(arg)
            if record:
                print(record)
                print(f"Функція буде шукати name {arg}")
    # note
        except:
            print(f"Функція буде шукати note {arg}")


@input_error
def delete(args, book):
    if len(args) == 1:      # if in args 1 arg
       arg = args[0]        # get arg from []
       res = book.delete(arg)
       return res
    elif len(args) == 2:
        name, field = args
        record = book.find(name)
        if field == 'phones':
            res = record.remove_phones()
            return res
        elif field == 'birthday':
            res = record.remove_birthday()
            return res
        elif field == 'email':
            res = record.remove_email()
            return res
        elif field == 'address':
            res = record.remove_address()
            return res
        elif field == 'notes':
            res = record.remove_notes()
            return res

        
   
def show_commands():
    commands = {
        "help": "help",
        "hello": "just fo say 'Hi!'",
        "add [name] [phone]": "add new contact",
        "change [name] [phone]": "change person phone number",
        "phone [name]": "get person phone numbers",
        "add-birthday [name]": "add person birthday",
        "show-birthday [name]": "get person birthday",
        "change-birthday [name]": "change person birthday",
        "birthdays": "get persons with birtday next week ",
        "birthdays [days]": "get birtdays list for next custom amount of days",
        "delete [name]": "delete contact",
        "delete [name] phones": "delete person phones",
        "delete [name] birthday": "delete person birthday",
        "delete [name] email": "delete person email",
        "delete [name] address": "delete person address",
        "delete [name] notes": "delete person notes",       
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
        "all": "get all contact list",
        "exit": "exit",
    }

    res = []
    for command, desctiption in commands.items():
        res.append("    {:<23}  -->  {} ".format(command, desctiption))
    return "\n".join(res)