from collections import UserDict
from record import Record


class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        return "\n".join(str(record) for record in self.data.values())