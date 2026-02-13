
# goit-algo-hw-06

## Address Book Project

This project implements a simple address book in Python, allowing users to store, edit, and manage contacts with phone numbers.

### Features
- Add new contacts with multiple phone numbers
- Edit phone numbers for existing contacts
- Find contacts by name
- Delete contacts
- Validate phone numbers (must be 10 digits)

### Project Structure
- **main.py**: Example usage and entry point
- **addres_book.py**: `AddressBook` class for managing records
- **record.py**: `Record` class for individual contacts
- **field.py**: Base `Field` class
- **name.py**: `Name` class (inherits from `Field`)
- **phone.py**: `Phone` class (inherits from `Field`, validates phone numbers)

### Usage Example
```python
from record import Record
from addres_book import AddressBook

book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
book.add_record(john_record)
print(book)
```

### Requirements
No external dependencies. Requires Python 3.10+.

### Author
Stanislav Yurchenko
