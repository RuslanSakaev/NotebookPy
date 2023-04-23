import json
from createNote import create_note

# �������������� ������� � JSON-������
note_json = json.dumps(create_note(), indent=7, ensure_ascii=False)

# ������ JSON-������ � ����
with open("note.json", "w") as file:
    file.write(note_json)