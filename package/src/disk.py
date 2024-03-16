import json
from src.classes import AddressBook, Record, Name, Birthday, Phone, Email, Address, Note
from datetime import datetime

file = "package/src/data.json"


def convert_to_json(book, notes):
    data = {"records": [], "notes": []}
    for record in book.data.values():
        data["records"].append(
            {
                "name": record.name.value,
                "phones": [phone.value for phone in record.phones],
                "birthday": (
                    record.birthday.value.strftime("%d.%m.%Y")
                    if record.birthday
                    else None
                ),
                "emails": [email.value for email in record.emails],
                "addresses": [str(address) for address in record.addresses],
            }
        )
    for note in notes:
        data["notes"].append(
            {
                "title": note.data["title"],
                "text": note.data["text"],
                "tags": note.data["tags"],
            }
        )
    return data


def save_to_json(book, notes):
    with open(file, "w", encoding="utf-8") as fh:
        json.dump(convert_to_json(book, notes), fh)
    print("Don't worry, all data saved to file.")


def load_from_json():
    with open(file, "r") as fh:
        data = json.load(fh)
        book = AddressBook()

        # Convert to json format to book
        for contact in data["records"]:
            name = contact["name"]
            phone_list = []
            for phone in contact["phones"]:
                phone_list.append(Phone(phone))

            email_list = []
            for email in contact["emails"]:
                email_list.append(Email(email))

            addresses = [
                Address(*address_str.split(", "))
                for address_str in contact["addresses"]
            ]

            birthday = Birthday(contact["birthday"]) if contact["birthday"] else None

            record = Record(name)
            record.phones = phone_list
            record.birthday = birthday
            record.emails = email_list
            record.addresses = addresses

            book.add_record(record)

        notes = [
            Note(note["title"], note["text"], note["tags"]) for note in data["notes"]
        ]
    print("Data loaded from file.")
    return book, notes
