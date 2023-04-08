# Импортируем модуль json для сохранения записной книжки в файл
import json

# Создаем класс для записной книжки
class Notebook:
    def _init_(self):
        # Создаем пустой список для хранения заметок
        self.notes = []

    def add_note(self, title, content):
        # Создаем словарь для заметки
        note = {"title": title, "content": content}
        # Добавляем заметку в список
        self.notes.append(note)

    def display_notes(self):
        # Выводим все заметки в консоль
        for note in self.notes:
            print("Title:", note["title"])
            print("Content:", note["content"])
            print("")

    def save_notes(self, filename):
        # Сохраняем все заметки в файл в формате json
        with open(filename, "w") as f:
            json.dump(self.notes, f)

    def load_notes(self, filename):
        # Загружаем заметки из файла в формате json
        with open(filename, "r") as f:
            self.notes = json.load(f)