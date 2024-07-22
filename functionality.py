from collections import UserDict
from entities import Name, Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        return ValueError

    def remove_phone(self, phone_str: str):
        for i, phone in enumerate(self.phones):
            if phone.value == phone_str:
                del self.phones[i]
                return
        return ValueError

    def find_phone(self, phone_str: str):
        for phone in self.phones:
            if phone.value == phone_str:
                return phone.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return record

    def find(self, value: str):
        return self.data.get(value, None)

    def delete(self, value: str):
        if value in self.data:
            del self.data[value]
