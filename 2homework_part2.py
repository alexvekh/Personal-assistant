from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    def __init__(self,phone):
        super().__init__(phone)
        if not self.is_valid_phone_number(phone):
            raise ValueError(f"Phone number should contain 10 digits: {phone}")
    def is_valid_phone_number(self, phone):
        return phone.isdigit() and len(phone) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        return f"{phone} was added to {self.name.value}."
    def find_phone(self,phone):
        for number in self.phones:
            if number.value == phone:
                return number
        return None
    def remove_phone(self,phone):
        number = self.find_phone(phone)
        if number:
            self.phones.remove(number)
            return f"{phone} was successfully deleted"
        else:
            return f"Couldn't find {phone}"
    def edit_phone(self, old_phone,new_phone):
        number = self.find_phone(old_phone)
        if number:
            number.value = new_phone
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value] = record
    def find(self,name):
        return self.data.get(name)
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"{name} was successfully deleted"
        else:
            return f"Couldn't find {name}."

        # Створення нової адресної книги
        # Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
 # Видалення запису Jane
book.delete("Jane")