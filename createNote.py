import json
import datetime

# Функция для создания новой заметки
def create_note():
    id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    note = {
        "id": id,
        "title": title,
        "body": body,
        "date_created": date,
        "time_created": time,
        "date_modified": date,
        "time_modified": time
    }
    return note

# Функция для чтения всех заметок из файла
def read_notes():
    with open("note.json", "r") as file:
        notes = json.load(file)

        # Выводим все заметки в консоль
    if notes:
        for id, title, body in notes.items():
            print(f"Заголовок: {id}")            
            print(f"Заголовок: {title}")
            print(f"Содержание: {body}")
    else:
        print("Заметок пока нет.")

# Функция для редактирования заметки
def edit_note():
    id = input("Введите идентификатор заметки, которую необходимо отредактировать: ")
    with open("note.json", "r") as file:
        notes = json.load(file)
    for note in notes:
        if note["id"] == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            note["title"] = title
            note["body"] = body
            note["date_modified"] = date
            note["time_modified"] = time
    with open("note.json", "w") as file:
        json.dump(notes, file)

# Функция для удаления заметки
def delete_note():
    id = input("Введите идентификатор заметки, которую необходимо удалить: ")
    with open("note.json", "r") as file:
        notes = json.load(file)
    notes = [note for note in notes if note["id"] != id]
    with open("note.json", "w") as file:
        json.dump(notes, file)



