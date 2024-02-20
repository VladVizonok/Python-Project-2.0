from collections import UserDict
from datetime import datetime
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        super().__init__(value)

    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        try:
            value_date = datetime.strptime(value, '%d.%m.%Y').date()
            self.__value = value_date
        except ValueError:
            raise ValueError ('Enter date in this format: dd.mm.yyyy')

class Phone(Field):
    def __init__(self, value):
        self.__value = None
        super().__init__(value)
        
    @property
    def value(self):
        return self.__value
        
    @value.setter
    def value(self, value):
        if len(value) == 10 and len(list(filter(lambda num: num.isnumeric(), value))) == 10:
            self.__value = value
        else:
            raise ValueError ('Phone can only contains 10 digits.')
        
class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        if birthday == None:
            self.birthday = None
        else:
            self.birthday = Birthday(birthday)

    def add_phone(self, value):
        self.phones.append(Phone(value))
    
    def remove_phone(self, value):
        for elem in self.phones:
            if elem.value == value:
                self.phones.remove(elem)
    
    def edit_phone(self, old_phone, new_phone):
        if old_phone not in map(lambda phone: phone.value, self.phones):
            raise ValueError
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.phones.append(Phone(new_phone))
    
    def find_phone(self, value):
        for elem in self.phones:
            if elem.value == value:
                return elem

    def days_to_birthday(self):
        birthday_this_year = datetime(datetime.now().year, self.birthday.value.month, self.birthday.value.day)
        if datetime.now() > birthday_this_year:
            birthday_this_year = datetime(datetime.now().year + 1, self.birthday.value.month, self.birthday.value.day)
        remaining_days = (birthday_this_year - datetime.now())
        return f'To {self.name.value}`s birthday remains {remaining_days.days} days.'
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        for record in self.data:
            if name == record:
                return self.data[name]
    
    def delete(self, name):
        for record in self.data:
            if name == record:
                self.data.pop(record)
                break
    
    def iterator(self, records_per_time=1):
        current_index = 0
        record_values = [record.__str__() for record in self.data.values()]
        while current_index < len(record_values):
            result = record_values[current_index:current_index + records_per_time]
            yield result
            current_index += records_per_time
    
    def save_to_file(self, filename = 'cash.bin'):
        with open (filename, 'wb') as file:
            pickle.dump(self.data, file)

    def open_from_file(self, filename = 'cash.bin'):
        try: 
            with open (filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print('Cash not found. Create new Address Book')
    
    def find_all_match(self, word_to_find):
        result = []
        for record in self.data.values():
            if word_to_find in record.name.value:
                result.append(record.__str__())
            for phone in record.phones:
                if word_to_find in phone.value:
                    result.append(record.__str__())
        return result
    
    def show_all(self):
        record_values = [record.__str__() for record in self.data.values()]
        return record_values
    

    

def main():
    book = AddressBook()
    book.open_from_file()

    print('List of comand:\n', 'add\n', 'delete\n', 'show_all\n', 'exit')

    while True:
        user_input = input('Enter comand:')
        if user_input == 'add':
            name = input('Enter contact`s name: ')
            new_record = Record(name)
            phone = input('Enter contact`s phone: ')
            new_record.add_phone(phone)
            birthday = input('Enter contact`s birthday(dd.mm.yyyy): ')
            new_record.birthday = Birthday(birthday)
            book.add_record(new_record)
            print('Contact saved')

        if user_input == 'delete':
            trash = input('Enter contact you want to delete: ')
            book.delete(trash)
            print('Cotact deleted')

        if user_input == 'show_all':
            print(book.show_all())

        if user_input == 'exit':
            book.save_to_file()
            print('Good Bye!')
            break
            

if __name__ == '__main__':
    main()

       
    




