import pickle
from collections import UserList
from datetime import datetime, timedelta
from CLI_2_0.record import FirstName, LastName, Birthday, Address, Email, Record
from rich.console import Console
from rich.table import Table
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from abc import ABC, abstractmethod

class AddressView(ABC):
    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def find_all_match(self, word_to_find):
        pass

    @abstractmethod
    def find_by_id(self, ID):
        pass

    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def upcoming_birthdays(self, days):
        pass


class AddressBook(UserList, AddressView):
    __id = 1 
    def add_record(self, record):
        record.ID = self.__id
        self.data.append(record)
        self.__id += 1
    

    
    def add_phone(self, ID, phone):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if ID == record.ID:
                record.add_phone(phone)
                
    def change_phone(self, ID, old_phone, new_phone):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if ID == record.ID:
                record.edit_phone(old_phone, new_phone)

    def delete_phone(self, ID, phone):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if ID == record.ID:
                record.remove_phone(phone)
    
    def delete_record(self, name_or_id):
        #READY
        for record in self.data:
            full_name = record.first_name.value + ' ' + record.last_name.value
            if name_or_id == full_name or name_or_id == record.ID:
                self.data.remove(record)
                break

    def edit_name(self, ID, first_name, last_name):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if record.ID == ID:
                record.first_name = FirstName(first_name)
                record.last_name = LastName(last_name)
    
    def edit_address(self, ID, address):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if record.ID == ID:
                record.set_address(address)
    
    def edit_email(self, ID, email):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if record.ID == ID:
                record.set_email(email)

    def edit_birthday(self, ID, birthday):
        #READY
        for record in self.data:
            if ID not in map(lambda record: record.ID, self.data):
                raise ValueError
            if record.ID == ID:
                record.set_birthday(birthday)




    def find_by_name(self, name):
        #READY            
        record_table = Table(title='Find by name', show_lines=True, width=125)
        record_table.add_column('Name', style='cyan')
        record_table.add_column('ID', style='magenta')
        record_table.add_column('Birthday', style='yellow')
        record_table.add_column('Email', style='green')
        record_table.add_column('Address', style='green')
        record_table.add_column('Phones', style='green')

        for record in self.data:
            full_name = record.first_name.value + ' ' + record.last_name.value
            if name == full_name:
                record_table.add_row(record.full_name(), str(record.ID), record.birthday.value, 
                                     record.email.value, record.address, record.unit_phones())

        console = Console()
        console.print(record_table)      
    
    def find_all_match(self, word_to_find):
        #READY
        result = []
        for record in self.data:
            full_name = record.first_name.value + ' ' + record.last_name.value
            if word_to_find in full_name:
                result.append(record)
            for phone in record.phones:
                if word_to_find in phone:
                    result.append(record)

        record_table = Table(title='Find All Match', show_lines=True,width=125)
        record_table.add_column('ID', style='magenta')
        record_table.add_column('Name', style='cyan')
        record_table.add_column('Birthday', style='yellow')
        record_table.add_column('Email', style='green')
        record_table.add_column('Address', style='green')
        record_table.add_column('Phones', style='green')

        for record in result:
            record_table.add_row(str(record.ID), record.full_name(), record.birthday.value, record.email.value, record.address, record.unit_phones())

        console = Console()
        console.print(record_table)
    
    def find_by_id(self, ID):
        #READY
        record_table = Table(title='Find by ID', show_lines=True, width=125)
        record_table.add_column('ID', style='magenta')
        record_table.add_column('Name', style='cyan')
        record_table.add_column('Birthday', style='yellow')
        record_table.add_column('Email', style='green')
        record_table.add_column('Address', style='green')
        record_table.add_column('Phones', style='green')

        for record in self.data:
            if ID == record.ID:       
                record_table.add_row(str(record.ID), record.full_name(), record.birthday.value, record.email.value, record.address, record.unit_phones())

        console = Console()
        console.print(record_table)

    def show_all(self):
        if self.data == []:
            print('Adress Book have no contact`s to show. ')

        record_table = Table(title='Show All', show_lines=True, width=125)
        record_table.add_column('ID', style='magenta')
        record_table.add_column('Name', style='cyan')
        record_table.add_column('Birthday', style='yellow')
        record_table.add_column('Email', style='green')
        record_table.add_column('Address', style='green')
        record_table.add_column('Phones', style='green') 

        for record in self.data:
            record_table.add_row(str(record.ID), record.full_name(), record.birthday.value, record.email.value, record.address, record.unit_phones())

        console = Console()
        console.print(record_table)

    def upcoming_birthdays(self, days):
        #READY
        current_date = datetime.now().date()
        upcoming_date = current_date + timedelta(days=int(days))

        upcoming_birthdays_list = []

        for contact in self.data:
            birthday_date = contact.birthday
            if birthday_date:
                birth = datetime.strptime(birthday_date.value, '%d.%m.%Y')
                birthday_date = birth.replace(year=upcoming_date.year).date()
                
            if birthday_date == upcoming_date:
                upcoming_birthdays_list.append(contact)
        
        record_table = Table(title='Upcoming birthday', show_lines=True, width=125)
        record_table.add_column('ID', style='magenta')
        record_table.add_column('Name', style='cyan')
        record_table.add_column('Birthday', style='yellow')
        record_table.add_column('Email', style='green')
        record_table.add_column('Address', style='green')
        record_table.add_column('Phones', style='green')  

        for record in upcoming_birthdays_list:
            record_table.add_row(str(record.ID), record.full_name(), record.birthday.value, record.email.value, record.address, record.unit_phones())

        console = Console()
        console.print(record_table)




    def save_to_file(self, filename = 'address_cash.bin'):
        with open (filename, 'wb') as file:
            pickle.dump(self.data, file)
            pickle.dump(self.__id, file)

    def open_from_file(self, filename = 'address_cash.bin'):
        try: 
            with open (filename, 'rb') as file:
                self.data = pickle.load(file)
                self.__id = pickle.load(file)

        except FileNotFoundError:
            print('Cash not found. Create new Address Book')

    

