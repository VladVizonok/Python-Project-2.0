import pickle
from note import Note
from notes import Notes
from rich.table import Table
from collections import UserList
from rich.console import Console
from prompt_toolkit import prompt
from adressbook import AddressBook
from datetime import datetime, timedelta
from prompt_toolkit.completion import WordCompleter
from record import FirstName, LastName, Birthday, Address, Email, Record


def main():
    notebook = Notes()
    notebook.open_from_file()
    book = AddressBook()
    book.open_from_file()

    while True:
        category_list = WordCompleter(['contacts', 'notes', 'help', 'exit'])

        print('CATEGORY\n contacts\n notes\n help\n exit')

        category_input = prompt('Choose category: ', completer=category_list)

        if category_input == 'contacts':
            contact_com_list = WordCompleter(['create_contact', 'find_contact', 'delete_contact', 
                                              'edit_contact', 'upcoming birthday', 'help', 'exit'])
            
            print('LIST OF COMMAND:\n create_contact\n find_contact\n delete_contact\n edit_contact\n upcoming birthday\n help\n exit')
        
            option_input = prompt('Choose contact`s option: ', completer=contact_com_list)

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
                
                print('LIST OF COMMAND\n add_phone\n set_birthday\n set_email\n set_address\n edit_phone\n delete_phone\n edit_name\n help\n exit')
                
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
                
                print('LIST OF COMMAND\n find_by_name\n find_by_ID\n show_all\n find_all_matches\n help\n exit')
                
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
        


        if category_input == 'notes':
            notes_com_list = WordCompleter(['create_note', 'edit_note', 
                                            'find_note', 'delete_note', 
                                            'help', 'exit'])
            
            print('LIST OF COMMAND\n create_note\n edit_note\n find_note\n delete_note\n help\n exit')
            
            n_options_input = prompt('Choose note`s options: ', completer=notes_com_list)

            if n_options_input == 'create_note':
                title_input = prompt('Enter your note title: ')
                text_input = prompt('Enter text of your note: ')
                new_note = Note(title_input, text_input)
                notebook.add_note(new_note)
                print('Successfully added.')

            if n_options_input == 'edit_note':
                edit_list = WordCompleter(['edit_title', 'edit_text', 
                                           'set_tags', 'help', 'exit'])
                ID_input = prompt('Enter your note`s ID: ')

                print('LIST OF COMMAND\n edit_title\n edit_text\n set_tags\n help\n exit')

                edit_input = prompt('Choose option: ', completer=edit_list)
                while True:
                    try: 
                        for note in notebook:
                            if int(ID_input) not in map(lambda note: note.ID, notebook):
                                raise ValueError
                
                        if edit_input == 'edit_title':
                            new_title_input = prompt('Enter new title: ')
                            for note in notebook:
                                if int(ID_input) == note.ID:
                                    note.edit_title(new_title_input)
                                    print('Successfully changed.')
                            break

                        if edit_input == 'edit_text':
                            new_text_input = prompt('Enter new text: ')
                            for note in notebook:
                                if int(ID_input) == note.ID:
                                    note.edit_text(new_text_input)
                                    print('Successfully changed.')
                            break

                        if edit_input == 'set_tags':
                            tags_input = prompt('Enter tags, that you want to add/change in format #tag #tag: ')
                            for note in notebook:
                                if int(ID_input) == note.ID:
                                    if note.tag == ['No tag`s']:
                                        note.add_tag(tags_input)
                                        print('Successfully added.')
                                    else:
                                        note.edit_tag(tags_input)
                                        print('Successfully changed.')
                            break
                            
                        if edit_input == 'help':
                                pass

                        if edit_input == 'exit':
                            book.save_to_file()
                            notebook.save_to_file()
                            break
                        
                    except ValueError:
                        print('Note with this ID is not exist. ')
                        break


            if n_options_input == 'find_note':
                find_list = WordCompleter(['find_by_title', 'find_by_tag',
                                            'find_by_ID', 'sort_by_tags', 'show_all',
                                            'help', 'exit'])
                
                print('LIST OF COMMAND\n find_by_title\n find_by_tag\n find_by_ID\n sort_by_tags\n show_all\n help\n exit')
                
                find_input = prompt('Choose option: ', completer=find_list)
                
                if find_input == 'find_by_title':
                    title_input = prompt('Enter note`s title, that you want to find: ')
                    notebook.find_by_title(title_input)
                
                if find_input == 'find_by_tag':
                    tag_input = prompt('Enter note`s tag, that you want to find: ')
                    notebook.find_by_tag(tag_input)
                
                if find_input == 'find_by_ID': 
                    id_input = prompt('Enter note`s ID, that you want to find: ')
                    try:
                        for note in notebook:
                            if int(id_input) not in map(lambda note: note.ID, notebook):
                                raise ValueError
                            notebook.find_by_id(int(id_input))
                    except ValueError:
                        print('Note with this ID is not exist. ')

                if find_input == 'sort_by_tags':
                    notebook.sort_by_tag()

                if find_input == 'show_all':
                    notebook.show_all_notes()
                
                if find_input == 'help':
                    pass

                if find_input == 'exit':
                    book.save_to_file()
                    notebook.save_to_file()
                    break

                
            if n_options_input == 'delete_note':
                delete_input = prompt('Enter note`s ID, that you want to delete: ')
                for note in notebook:
                    if note.ID == int(delete_input):
                        notebook.delete(int(delete_input))
                        print('Successfully deleted.')

            if n_options_input == 'help':
                pass

            if n_options_input == 'exit':
                book.save_to_file()
                notebook.save_to_file()
                break

        if category_input == 'help':
            pass
        
        if category_input == 'exit':
            book.save_to_file()
            notebook.save_to_file()
            break

                    

        
if __name__ == '__main__':
    main()