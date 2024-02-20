from collections import UserDict
from datetime import datetime
import pickle


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
    

    