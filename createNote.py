import json
from Note import Note
from view import View


class ListOfNotes:
    __notes = []
    __view = View()
    __index = 0
    __index_stack = []

    def __init__(self):
        try:
            with open('notes.json', 'r') as file:
                notes_dict = json.load(file)
                for note_dict in notes_dict:
                    note = Note()
                    note.set_name(note_dict['name'])
                    note.set_text(note_dict['text'])
                    note.set_id(note_dict['id'])
                    note.update_date()
                    self.__notes.append(note)
                self.__index = len(self.__notes)
            with open('indexes.json', 'r') as file:
                self.__index_stack = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.__notes = []
            self.__view = View()
            self.__index = 0
            self.__index_stack = []

    def add_note(self):
        note = Note()
        note.set_name(self.__view.input_note_name())
        note.set_text(self.__view.input_note_text())
        note.update_date()
        if len(self.__index_stack) == 0:
            note.set_id(self.__index)
        else:
            note.set_id(self.__index_stack.pop())
        self.__notes.append(note)
        self.__index = len(self.__notes)
        self.__view.info_note_msg('add')

    def delete_note(self, note):
        self.__index_stack.append(note.get_id())
        for index, n in enumerate(self.__notes):
            if n['id'] == note.get_id():
                self.__notes.pop(index)
                break
        if len(self.__notes) == 0:
            self.__index_stack.clear()
        self.__view.info_note_msg('del')

    def read_all_notes(self):
        self.__view.show_read_all_banner(len(self.__notes))
        for note in self.__notes:
            self.__view.show_note(note)

    def manage_note_by_id(self):
        commands = {1: self.__view.show_note,
                    2: self.__view.edit_note,
                    3: self.delete_note}
        flag = False
        self.__view.show_manage_note_menu()
        choice = self.__view.input_number(len(commands.keys()), 'menu')
        value = self.__view.input_number(self.__index, 'id')
        for note in self.__notes:
            if note['id'] == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.__view.not_found()

    def save_notes_to_file(self):
        note_dicts = [note.to_dict() for note in self.__notes]
        with open('notes.json', 'w') as file:
            json.dump(note_dicts, file)
        with open('indexes.json', 'w') as file:
            json.dump(self.__index_stack, file)
        self.__view.saved_info()
