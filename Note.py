# Importing the time module
from datetime import datetime


# Add class
class Note:
    __id = 0
    __name = ""
    __date = ""
    __text = ""

    def set_id(self, value):
        self.__id = value

    def set_name(self, name):
        self.__name = name

    def set_text(self, text):
        self.__text = text

    def update_date(self):
        self.__date = datetime.now().strftime('%Y, %B %d, %A | %H:%M')

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_text(self):
        return self.__text

    def to_dict(self):
        return {'name': self.__name, 'text': self.__text, 'id': self.__id, 'date': self.__date}
