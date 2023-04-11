import json
from createNote import create_note

# Преобразование словаря в JSON-строку
note_json = json.dumps(create_note(), indent=7, ensure_ascii=False)

# Запись JSON-строки в файл
with open("note.json", "w") as file:
    file.write(note_json)
