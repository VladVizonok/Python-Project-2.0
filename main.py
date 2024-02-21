from collections import UserList
from datetime import datetime, timedelta
import pickle
from record import FirstName, LastName, Birthday, Address, Email, Record
from rich.console import Console
from rich.table import Table
from note import Note
from notes import Notes
from adressbook import AddressBook
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter



def main():
    notebook = Notes()
    notebook.open_from_file()
    book = AddressBook()
    book.open_from_file()

    while True:
        category_list = WordCompleter(['contacts', 'notes', 'sort', 'help', 'exit'])
        category_input = prompt('Choose category: ', completer=category_list)

        if category_input == 'contacts':
            contact_com_list = WordCompleter(['create_contact', 'find_contact', 'delete_contact', 
                                              'edit_contact', 'upcoming birthday', 'help', 'exit'])
        
            option_input = prompt('Choose option: ', completer=contact_com_list)

            if option_input == 'create_contact':
                while True:
                    try:
                        record_name = prompt('Enter contact`s name in format: First_name Last_name: ')
                        split_name = record_name.split()
                        new_record = Record(split_name[0], split_name[1])
                        try:
                            record_birthday = prompt('Enter contact`s birthday in format dd.mm.yyyy: ')
                            new_record.set_birthday(record_birthday)
                            try:
                                record_email = prompt('Enter contact`s email: ')
                                new_record.set_email(record_email)
                                book.add_record(new_record)
                                print('Successfully added')
                                break
                            except ValueError:
                                print('Invalid email format. Try again')
                                break
                        except ValueError:
                            print('Invalid birthday format. Enter birthday in format: dd.mm.yyyy')
                            break
                    except IndexError:
                        print('Invalid name. Try again.')
                        break  

            if option_input == 'edit_contact':
                edit_com_list = WordCompleter(['add_phone', 'set_birthday', 'set_email',
                                                'set_address', 'edit_phone', 'delete_phone', 
                                                'edit_name', 'help', 'exit'])
                
                edit_input = prompt('Choose option: ', completer=edit_com_list)
                while True:
                    try:
                        if edit_input == 'add_phone':
                            id = prompt('Enter contact`s ID: ')
                            phone = prompt('Enter phone, that you want to add: ')
                            book.add_phone(int(id), phone)
                            print('Successfully added.')
                            break

                        if edit_input == 'delete_phone':
                            id = prompt('Enter contact`s ID: ')
                            phone = prompt('Enter phone, that you want to delete: ')
                            book.delete_phone(int(id), phone)
                            print('Successfully deleted.')
                            break

                        if edit_input == 'edit_phone':
                            id = prompt('Enter contact`s ID: ')
                            old_phone = prompt('Enter phone, that you want to change: ')
                            new_phone = prompt('Enter new phone: ')
                            book.change_phone(int(id), old_phone, new_phone)
                            print('Successfully changed.')
                            break

                        if edit_input == 'set_birthday':
                            id = prompt('Enter contact`s ID: ')
                            birthday = prompt('Enter new birthday date: ')
                            book.edit_birthday(int(id), birthday)
                            print('Successfully add/change.')
                            break

                        if edit_input == 'set_email':
                            id = prompt('Enter contact`s ID: ')
                            email = prompt('Enter email that you want to add/change: ')
                            book.edit_email(int(id), email)
                            print('Successfully add/change.')
                            break

                        if edit_input == 'set_address':
                            id = prompt('Enter contact`s ID: ')
                            address = prompt('Enter address that you want to add/change: ')
                            book.edit_address(int(id), address)
                            print('Successfully add/change.')
                            break

                        if edit_input == 'edit_name':
                            id = prompt('Enter contact`s ID: ')
                            name_input = prompt('Enter new name in format: First_name Last_name: ')
                            split_name = name_input.split()
                            book.edit_name(int(id), split_name[0], split_name[1])
                            print('Successfully changed.')
                            break

                        if edit_input == 'help':
                            pass
                        
                        if edit_input == 'exit':
                            book.save_to_file()
                            notebook.save_to_file()
                            break
                    except ValueError:
                        print('Invalid enter. You enter wrong ID or invalid value.')
                        break
                    
            
            if option_input == 'find_contact':
                find_com_list = WordCompleter(['find_by_name', 'find_by_ID', 
                                               'show_all', 'find_all_matches', 'help', 'exit'])
                
                find_input = prompt('Choose option: ', completer=find_com_list)
                
                if find_input == 'show_all':
                    book.show_all()
                
                if find_input == 'find_by_name':
                    finder = prompt('Enter contact`s name that you want to find in format First_Name Last_Name: ')
                    book.find_by_name(finder)

                if find_input == 'find_by_ID':
                    finder = prompt('Enter contact`s ID, that you want to find: ')
                    book.find_by_id(int(finder))

                if find_input == 'find_all_matches':
                    finder = prompt('Enter contact`s name or phone, that you want to find: ')
                    book.find_all_match(finder)

                if find_input == 'help':
                    pass

                if find_input == 'exit':
                    book.save_to_file()
                    notebook.save_to_file()
                    break
      
            if option_input == 'delete_contact':
                try:
                    cleaner = prompt('Enter contact`s name or ID, that you want to delete: ')
                    if cleaner not in map(lambda record: record.ID, book.data):
                        raise ValueError
                    book.delete_record(int(cleaner))
                    print('Successfully deleted.')
                except ValueError:
                    print('You enter invalid ID or ID does`t exist.')
            
            if option_input == 'upcoming birthday':
                days_by_bth = prompt('Enter how many day`s to birthday: ')
                book.upcoming_birthdays(days_by_bth)

            if option_input == 'help':
                pass

            if option_input == 'exit':
                book.save_to_file()
                notebook.save_to_file()
                break
        
        if category_input == 'help':
            pass
        
        if category_input == 'exit':
            book.save_to_file()
            notebook.save_to_file()
            break

                    

        


    # 




    # while True:
    #     user_input = input('Enter comand:')
    #     if user_input == 'add':
    #         name = input('Enter contact`s name: ')
    #         new_record = Record(name)
    #         phone = input('Enter contact`s phone: ')
    #         new_record.add_phone(phone)
    #         birthday = input('Enter contact`s birthday(dd.mm.yyyy): ')
    #         new_record.birthday = Birthday(birthday)
    #         book.add_record(new_record)
    #         print('Contact saved')

    #     if user_input == 'delete':
    #         trash = input('Enter contact you want to delete: ')
    #         book.delete(trash)
    #         print('Cotact deleted')

    #     if user_input == 'show_all':
    #         print(book.show_all())

    #     if user_input == 'exit':
    #         book.save_to_file()
    #         print('Good Bye!')
    #         break
            

if __name__ == '__main__':
    main()