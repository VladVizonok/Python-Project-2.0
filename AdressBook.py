from collections import UserList
from datetime import datetime, timedelta
import pickle
from record import FirstName, LastName, Birthday, Address, Email, Record


class AddressBook(UserList):
    __id = 1 
    def add_record(self, record):
        record.ID = self.__id
        self.data.append(record)
        self.__id += 1
    
    def find_by_name(self, name):
        #READY, BUT NEED TO FORMAT
        for record in self.data:
            full_name = record.first_name.value + ' ' + record.last_name.value
            if name == full_name:
                return record
        raise ValueError ('Contact doesn`t exist or you enter invalid name')
    
    def find_by_id(self, ID):
        #READY, BUT NEED TO FORMAT
        for record in self.data:
            if ID == record.ID:
                return record
        raise ValueError ('Contact doesn`t exist or you enter invalid ID')
    
    def add_phone(self, ID, phone):
        #READY
        for record in self.data:
            if ID == record.ID:
                record.add_phone(phone)
    
    def change_phone(self, ID, old_phone, new_phone):
        #READY
        for record in self.data:
            if ID == record.ID:
                record.edit_phone(old_phone, new_phone)

    def delete_phone(self, ID, phone):
        #READY
        for record in self.data:
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
            if record.ID == ID:
                record.first_name = FirstName(first_name)
                record.last_name = LastName(last_name)
    
    def edit_address(self, ID, address):
        #READY
        for record in self.data:
            if record.ID == ID:
                record.set_address(address)
    
    def edit_email(self, ID, email):
        #READY
        for record in self.data:
            if record.ID == ID:
                record.set_email(email)

    def edit_birthday(self, ID, birthday):
        #READY
        for record in self.data:
            if record.ID == ID:
                record.set_birthday(birthday)
    
    def find_all_match(self, word_to_find):
        #READY
        result = []
        for record in self.data:
            full_name = record.first_name.value + ' ' + record.last_name.value
            if word_to_find in full_name:
                result.append(record.__str__())
            for phone in record.phones:
                if word_to_find in phone:
                    result.append(record.__str__())
        return result
    
    def upcoming_birthdays(self, days):
        #READY
        current_date = datetime.now().date()
        upcoming_date = current_date + timedelta(days=days)

        upcoming_birthdays_list = []

        for contact in self.data:
            birthday_date = contact.birthday
            if birthday_date:
                birth = datetime.strptime(birthday_date.value, '%d.%m.%Y')
                birthday_date = birth.replace(year=upcoming_date.year).date()
                
            if birthday_date == upcoming_date:
                upcoming_birthdays_list.append(contact.__str__())
        return upcoming_birthdays_list

    
    def show_all(self):
        record_values = [record.__str__() for record in self.data.values()]
        return record_values
    


book = AddressBook()
john = Record('John', 'Marston')
book.add_record(john)
book.edit_name(1, 'Artur', 'Morgan')
book.edit_address(1, 'Shevchenka 54')
book.edit_email(1, 'vlad.vizonok@gmail.com')
book.edit_birthday(1, '01.03.1988')
book.add_phone(1, '1234567890')
book.add_phone(1, '1234567899')
book.change_phone(1,'1234567899', '1234567891')
book.delete_phone(1, '1234567891')
print(book.upcoming_birthdays(10))

# print(book.find_all_match('Artur'))


