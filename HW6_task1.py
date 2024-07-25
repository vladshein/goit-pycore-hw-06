#HW6 task1

from collections import UserDict

# base class field
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# name class inherited from base class Field
class Name(Field):
    # реалізація класу
	pass

# phone class inherited from base class Field
class Phone(Field):
    # реалізація класу
    def check_phone(self, phone):
        if len(phone) != 10:
            return f"Incorrect phone length"
        elif phone.isnumeric() != True:
            return f"Length of phone is correct, but not only digits entered"
        else:
            return f"Phone number is correct and can be added to the book"


# record class to store and process phone records
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in range(len(self.phones)):
            if phone == self.phones[i].value:
                self.phones.remove(self.phones[i])
                break
        
    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if phone == self.phones[i].value:
                self.phones[i].value = new_phone
        
    def find_phone(self, phone):
        for i in range(len(self.phones)):
            if phone == self.phones[i].value:
                return phone
            else:
                return None

# create address book         
class AddressBook(UserDict):
    # реалізація класу
    
    def add_record(self, record):
        self.data[record.name] = record

    #need to check functionality
    def find(self, name):
        for key in self.data.keys():
              if key.value == name:
                    print("Here")
                    return self.data[key]

    
    def delete(self, name):
        for key in self.data.keys():
            if name == key.value:
                self.data.pop(key)
                break


#test data
# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)

# Створення запису для John
jhn_record = Record("Jhn")
jhn_record.add_phone("1234567890")
jhn_record.add_phone("5555555555")
jhn_record.add_phone("3333333333")
jhn_record.add_phone("7777777777")
print(jhn_record)

found_phone = jhn_record.find_phone("1234567890")
print(f"Found phone is {found_phone}")

jhn_record.edit_phone("1234567890", "2345678901")
print(jhn_record)

jhn_record.remove_phone("3333333333")
print(jhn_record)

book = AddressBook()
book.add_record(jhn_record)
jhn = book.find("Jhn")
print(jhn)

book.add_record(john_record)
john = book.find("John")
print(john)

for name, record in book.data.items():
    print(record)

book.delete("John")

for name, record in book.data.items():
    print(record)



