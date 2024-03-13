from collections import UserDict
from datetime import datetime
from src.birthdays import get_birthdays_by_days, get_birthdays_per_week
from src.validate import date_is_valid
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
        if date_is_valid(value):
            try:
                self.value = datetime.strptime(value, '%d.%m.%Y').date()
            except ValueError as e:
                raise ValueError('Invalid date value: ' + str(e))
        else:
            raise ValueError('We couldn\'t validate entered date. Please, try again')

        
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
    def __init__(self, name="contacts"):
        super().__init__()
        self.name = name

    def __dict__(self):
        return {'name': self.name, 'records': dict(self.data)}  # Restructure for JSON

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

    def get_birthdays_by_days(self, days):
        users = []
        for name, record in self.data.items():
            if record.birthday != None:
                users.append({'name': name, 'phones': record.phones,'birthday': record.birthday.value})
        return get_birthdays_by_days(users, days)