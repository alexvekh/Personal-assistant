import json
from src.classes import AddressBook, Record, Name, Birthday, Phone
from datetime import datetime

file = 'src/data.json'

def convert_to_json(book):
    records = []
    for record in book.data.values():
            records.append(
                {
                    "name": record.name.value,
                    "phones": [phone.value for phone in record.phones],
                    "birthday": (
                        record.birthday.value.strftime("%d.%m.%Y")
                        if record.birthday
                        else None
                    ),
                }
            )
    return records

def save_to_json(book):    
    with open(file, "w", encoding="utf-8") as fh:
        json.dump(convert_to_json(book), fh)



def load_from_json():
    with open(file, "r") as fh:
        data = json.load(fh)
        book = AddressBook()

        # Convert to json format to book
        for contact in data:
            name = contact['name']
            phone_list = []
            for phone in contact['phones']:
                phone_list.append(Phone(phone))
            birthday = Birthday(contact['birthday']) if contact['birthday'] else None

            record = Record(name)
            record.phones = phone_list
            record.birthday = birthday

            book.add_record(record)

    return book

