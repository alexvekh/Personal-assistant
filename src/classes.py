from collections import UserDict
from datetime import datetime
from src.birthdays import get_birthdays_per_week, get_birthdays_by_days
from src.validate import name_is_valid, phone_is_valid, date_is_valid, email_is_valid
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if name_is_valid(value):
            self.value = value.title()
        else:
            raise NameError('Name should starts with letter')


class Phone(Field):
    def __init__(self, value):
        if phone_is_valid(value):
            self.value = value
        else:
            raise ValueError('Phone should be 10 digits format')

class Email(Field):
    def __init__(self, value):
        if email_is_valid(value):
            self.value = value
        else:
            raise ValueError('Invalid email format')

    # @staticmethod
    # def validate_email(value):
    #     pattern = r'^[\w\.-]+@[\w\.-]{2,}\.\w{2,}$'
    #     return re.match(pattern, value) is not None
    
class Birthday(Field):
    def __init__(self, value: str):
        if date_is_valid(value):
            try:
                self.value = datetime.strptime(value, '%d.%m.%Y').date()
            except ValueError as e:
                raise ValueError('Invalid date value: ' + str(e))
        else:
            raise ValueError('We couldn\'t validate entered date. Please, try again')

class Address(Field):
    def __init__(self, street, house_number, city, postal_code=None, country=None):
        self.street = street
        self.house_number = house_number
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def __str__(self):
        address_parts = [self.street, self.house_number, self.city]
        if self.postal_code:
            address_parts.append(self.postal_code)
        if self.country:
            address_parts.append(self.country)
        return ", ".join(address_parts)


class Note(UserDict):
    def __init__(self, title, text, tags):
        super().__init__()
        self.data["title"] = title
        self.data["text"] = text
        self.data["tags"] = tags

        
    def __str__(self):
        return f"{'=' * 50}\nTitle: {self.data['title']}\nText: {self.data['text']}\nTags: {' '.join(self.data['tags'])}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = [] 
        self.birthday = None
        self.addresses = [] 
    
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
        
    def add_address(self, street, house_number, city, postal_code=None, country=None):
        self.addresses.append(Address(street, house_number, city, postal_code, country))
    
    def edit_address(self, street, house_number, city, postal_code=None, country=None):
        if self.addresses:    # варіанти: ?  if self.addresses[0]  # if len(self.addresses) > 0 
            address = self.addresses[0]
            if street:
                address.street = street
            if house_number:
                address.house_number = house_number
            if city:
                address.city = city
            if postal_code:
                address.postal_code = postal_code
            if country:
                address.country = country
            return "Address edited."
        else:
            return "No address to edit."
        
        
    def remove_address(self):
        self.addresses = []

    def add_address(self, street, house_number, city, postal_code=None, country=None):
        self.addresses.append(Address(street, house_number, city, postal_code, country))

    def edit_address(self, street, house_number, city, postal_code=None, country=None):
        if self.addresses:
            address = self.addresses[0]
            if street:
                address.street = street
            if house_number:
                address.house_number = house_number
            if city:
                address.city = city
            if postal_code:
                address.postal_code = postal_code
            if country:
                address.country = country
            return "Address edited."
        else:
            return "No address to edit."

    def remove_address(self):
        self.addresses = []



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
    
class Note(UserDict):
    def __init__(self, title, text, tags):
        super().__init__()
        self.data["title"] = title
        self.data["text"] = text
        self.data["tags"] = tags
        
    def __str__(self):
        return f"{'=' * 50}\nTitle: {self.data['title']}\nText: {self.data['text']}\nTags: {' '.join(self.data['tags'])}"