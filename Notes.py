from collections import UserList
from rich.console import Console
from rich.table import Table
import pickle
from abc import ABC, abstractmethod

class NotesView(ABC):
    @abstractmethod
    def find_by_tag(self, tag):
        pass

    @abstractmethod
    def sort_by_tag(self):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_by_title(self, title):
        pass

    @abstractmethod
    def show_all_notes(self):
        pass



class Notes(UserList, NotesView):
    __id = 1
    def add_note(self, note):
        note.ID = self.__id
        self.data.append(note)
        self.__id += 1


    def find_by_tag(self, tag):
        result = []
        for note in self.data:
            if tag in note.tag:
                result.append(note)

        notes_table = Table(title='Find by tag', show_lines=True, width=125)
        notes_table.add_column('Tag', style='magenta')
        notes_table.add_column('ID', style='cyan')
        notes_table.add_column('Title', style='yellow')
        notes_table.add_column('Text', style='green')           

        for note in result:
            notes_table.add_row(tag, str(note.ID), note.title, note.text)

        console = Console()
        console.print(notes_table)
    

    def sort_by_tag(self):
        result = {}
        for note in self:
            for tag in note.tag:
                if tag not in result.keys():
                    result[tag] = [note]
                else:
                    result[tag].append(note)

        notes_table = Table(title='Sort by tag', show_lines=True, width=125)
        notes_table.add_column('Tag', style='magenta')
        notes_table.add_column('ID', style='cyan')
        notes_table.add_column('Title', style='yellow')
        notes_table.add_column('Text', style='green')           

        for key, value in result.items():
            for elem in value:
                notes_table.add_row(key, str(elem.ID), elem.title, elem.text)

        console = Console()
        console.print(notes_table)
         

    def find_by_id(self, id):
        for note in self.data:
            if note.ID == id:
                all_tag = ''
                for tag in note.tag:
                    all_tag = all_tag + ', ' + tag
                    all_tag = all_tag.removeprefix(', ')
                notes_table = Table(title='Find by ID', show_lines=True, width=125)
                notes_table.add_column('ID', style='cyan')
                notes_table.add_column('Tag', style='magenta')
                notes_table.add_column('Title', style='yellow')
                notes_table.add_column('Text', style='green')           

                notes_table.add_row(str(note.ID), all_tag, note.title, note.text)

                console = Console()
                console.print(notes_table)
            

    def find_by_title(self, title):
        result = []
        for note in self.data:
            if title == note.title:
                result.append(note)
            all_tag = ''
            for tag in note.tag:
                all_tag = all_tag + ', ' + tag
                all_tag = all_tag.removeprefix(', ')       

        notes_table = Table(title='Find by title', show_lines=True, width=125)
        notes_table.add_column('ID', style='cyan')
        notes_table.add_column('Tag', style='magenta')
        notes_table.add_column('Title', style='yellow')
        notes_table.add_column('Text', style='green')           

        for note in result:
            notes_table.add_row(str(note.ID), all_tag, note.title, note.text)

        console = Console()
        console.print(notes_table)
    
    
    def delete(self, id):
        for note in self.data:
            if note.ID == id:
                self.data.remove(note)
    
    
    def show_all_notes(self):
        notes_table = Table(title='All notes', show_lines=True, width=125)
        notes_table.add_column('ID', style='cyan')
        notes_table.add_column('Tag', style='magenta')
        notes_table.add_column('Title', style='yellow')
        notes_table.add_column('Text', style='green')           

        for note in self.data:
            all_tag = ''
            for tag in note.tag:
                all_tag = all_tag + ', ' + tag
                all_tag = all_tag.removeprefix(', ')
            notes_table.add_row(str(note.ID), all_tag, note.title, note.text)

        console = Console()
        console.print(notes_table)
    
    def save_to_file(self, filename = 'notes_cash.bin'):
        with open (filename, 'wb') as file:
            pickle.dump(self.data, file)
            pickle.dump(self.__id, file)

    def open_from_file(self, filename = 'notes_cash.bin'):
        try: 
            with open (filename, 'rb') as file:
                self.data = pickle.load(file)
                self.__id = pickle.load(file)
        except FileNotFoundError:
            print('Cash not found. Create new Note Book')