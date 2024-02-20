from collections import UserList
from datetime import datetime, timedelta
import pickle
from record import FirstName, LastName, Birthday, Address, Email, Record
from rich.console import Console
from rich.table import Table
from 



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