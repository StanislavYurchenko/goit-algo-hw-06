from phone import Phone
from name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.phones = [ph for ph in self.phones if ph.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            phone_to_edit.value = new_phone

    def find_phone(self, phone: str) -> Phone | None:
        return next((ph for ph in self.phones if ph.value == phone), None)