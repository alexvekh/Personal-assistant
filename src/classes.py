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
        
class Email(Field):
    def __init__(self, value):
        if self.validate_email(value):
            self.value = value
        else:
            raise ValueError('Invalid email format')

    @staticmethod
    def validate_email(value):
        pattern = r'^[\w\.-]+@[\w\.-]{2,}\.\w{2,}$'
        return re.match(pattern, value) is not None
    

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
    
    def remove_phones(self):
        self.phones = []
        return f"{self.name.value}'s phones deleted"

    def remove_birthday(self):
        self.birthday = None
        return f"{self.name.value}'s birthday deleted"
    
    def remove_email(self):
        self.email = None
        return f"{self.name.value}'s email deleted"

    def remove_address(self):
        self.address = None
        return f"{self.name.value}'s address deleted"

    def remove_notes(self):
        self.notes = None
        return f"{self.name.value}'s notes deleted"

    def __str__(self):
        if self.birthday == None:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.strftime('%d.%m.%Y')}"

class AddressBook(UserDict):
    # def __init__(self, name="contacts"):
    #     super().__init__()
    #     self.name = name

    def __dict__(self):
        return {'name': self.name, 'records': dict(self.data)}  # Restructure for JSON

    def add_record(self, record):
        self.data[record.name.value] = record
        #print(f'Added new record: "{record}"')
        
    def find(self, value):
        if value in self:
            return self[value]      # record
        else:
            raise IndexError(f"Record for {value} wasn't found")
        
        #### Code for delete
        # for name, record in self.items():
        #     if name == value:
        #         return record
        #     else:
        #         raise IndexError(f"Record for {value} wasn't found")

    # def find_in_field(self, field, value):
    #     print(field, value)
    #     field_value = self.data.get(field).value
    #     print(field_value)
    #     for record in self.values():
    #         print("record", record)
    #         field_value = record.get(field)
    #         print(field_value)
    #         if field == field_value:
    #                 print("FIND RECORD", record)
    #         else:
    #             print(f'{field} {value} not found' )

    def delete(self, name):
        try:
            self.data.pop(name)
            return f'{name}\'s contact was deleted'
        except(KeyError):
            return f'{name}\'s contact wasn\'t found'
        
        ##### Code for delete
        # try:
        #     key_for_delete = None
        #     for key in self.data.keys():
        #         if key == name:
        #             key_for_delete = key
        #     self.data.pop(key_for_delete)
        #     print(f'{name}\'s contact was deleted')
        # except(KeyError):
        #     print(f'{name}\'s contact wasn\'t found')
    
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