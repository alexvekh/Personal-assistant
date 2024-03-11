from collections import UserDict
from datetime import datetime
from birthdays import get_birthdays_per_week
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) > 0 and value[0].isalpha():
            self.value = value.title()
        else:
            raise NameError('Name should starts with letter')

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError('Phone should be 10 digits format')

class Birthday(Field):
    def __init__(self, value: str):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
        if re.match(pattern, value):
            dd, mm, yyyy = value.split('.')
            if int(dd) in range(31) and int(mm) in range(12):
                if int(yyyy) in range(1900, 2024):
                    try:
                        self.value = datetime.strptime(value, '%d.%m.%Y').date()
                    except ValueError as e:
                        raise ValueError('Invalid date value: ' + str(e))
                else:
                    raise ValueError('Looks like entered year is out of range. Expected in range 1900-2024')
            else:
                raise ValueError('Looks like entered day or month is out of range.')
        else:
            raise ValueError('Invalid date format. Please, use DD.MM.YYYY format')
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, value):
        self.phones.append(Phone(value))

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone, new_phone):
        found = False
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone
                print(f"Phone {phone} was changed to {new_phone}.")
                found = True
        if not found:
            raise IndexError(f'Phone {phone} wasn\'t found') 

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
    #
    def add_birthday(self, value):
        self.birthday = Birthday(value)
        return "birthday added"
    
    def __str__(self):
        if self.birthday == None:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.strftime('%d.%m.%Y')}"

class AddressBook(UserDict):
    # def __init__(self):
    #     self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record
        #print(f'Added new record: "{record}"')
        
    def find(self, value):
        for name, record in self.data.items():
            if name == value:
                return record
            else:
                raise IndexError(f"Record for {value} wasn't found")

    def delete(self, name):
        try:
            key_for_delete = None
            for key in self.data.keys():
                if key == name:
                    key_for_delete = key
            self.data.pop(key_for_delete)
            print(f'{name}\'s contact was deleted')
        except(KeyError):
            print(f'{name}\'s contact wasn\'t found')
    
    def get_birthdays_per_week(self):
        users = []
        for name, record in self.data.items():
            if record.birthday != None:
                users.append({'name': name, 'birthday': record.birthday.value})
        return get_birthdays_per_week(users)
    

# #Test
# book = AddressBook()

# #Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_birthday("08.03.1999")
# book.add_record(john_record)
# j_record = Record("J")
# j_record.add_phone("1111111111")
# j_record.add_birthday("09.03.1999")
# book.add_record(j_record)


# # # Додавання запису John до адресної книги

# # # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
# book.get_birthdays_per_week()
