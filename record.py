import re
from datetime import datetime


class FirstName:

    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value):
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise IndexError
        self.value = value.title()

class LastName:

    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Zа-яА-Я]{2,}', value):
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise IndexError
        self.value = value.title()


class Email:
        
    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        if not re.fullmatch(r'[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', value):
            return False
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value


class Birthday:
    #READY
    def __init__(self, value):
        self.set_value(value)

    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        datetime.strptime(value, '%d.%m.%Y')
        return True

    def set_value(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

   

class Address:
    #READY
    def __init__(self, address_string):
        self.address_str = address_string

    @property
    def address_string(self):
        return self.address_str

    @address_string.setter
    def address_string(self, new_address):
        self.address_str = new_address

    def __str__(self):
        return self.address_str


class Record:
    
    def __init__(self, first_name, last_name, birthday=None, address=None, email=None):
        self.first_name = FirstName(first_name)
        self.last_name = LastName(last_name)
        self.birthday = Birthday(birthday) if birthday else None
        self.address = Address(address) if address else None
        self.email = Email(email) if email else None
        self.phones = []
        self.ID = None
        


    def add_phone(self, phone):
        #READY
        new_number = phone
        if not len(phone) == 10 and not len(list(filter(lambda num: num.isnumeric(), phone))) == 10:
            raise ValueError
        if phone not in self.phones:
            self.phones.append(new_number)
        else: 
            print('Phone is allready exist')

    def remove_phone(self, phone):
        #READY
        if phone not in self.phones:
            raise ValueError
        for elem in self.phones:
            if elem == phone:
                self.phones.remove(elem)

    def edit_phone(self, old_number, new_number):
        #READY
        if not len(new_number) == 10 and not len(list(filter(lambda num: num.isnumeric(), new_number))) == 10:
            raise ValueError
        found = False
        for phone in self.phones:
            if phone == old_number:
                self.phones.remove(old_number)
                self.phones.append(new_number)
                found = True
                break
        if not found:
            print(
                f"Phone number '{old_number}' not found in the record."
                )
     
    def set_email(self, email):
        #READY
        if not Email(email).is_valid(email):
            raise ValueError
        self.email = Email(email)

    def set_birthday(self, birthday):
        #READY
        if not Birthday(birthday).is_valid(birthday):
            raise ValueError
        self.birthday = Birthday(birthday)

    def set_address(self, address):
        #READY
        self.address = address

    def __str__(self):
        return (
            f"Contact name: {self.first_name.value} {self.last_name.value}, "
            f"phones: {self.phones}, "
            f"Birthday: {self.birthday}, Email: {self.email}, Address: {self.address}"
        )
    def unit_phones(self):
        full_phones = ''
        for phone in self.phones:
                full_phones = full_phones + ', ' + phone
                full_phones = full_phones.removeprefix(', ')
        return full_phones
    
    def full_name(self):
        full_names = self.first_name.value + ' ' + self.last_name.value
        return full_names
    

record = Record('John', 'Smith', '30.08.1999', '123 Main St', 'johnsmith@gmail.com')
record.add_phone('1234567890')
record.set_email('vlad.vizonok@gmail.com')
record.set_birthday('30.09.1999')
print(record.phones)
