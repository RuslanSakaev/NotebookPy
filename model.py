import json
import datetime

# ������� ��� �������� ����� �������


def create_note():
    id = input("������� ������������� �������: ")
    title = input("������� ��������� �������: ")
    body = input("������� ����� �������: ")
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

# ������ JSON-������ � ����


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=7)


def add_note():
    notes = read_notes()
    note_id = len(notes) + 1
    title = input("������� ��������� �������: ")
    body = input("������� ����� �������: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at,
    }
    notes.append(note)
    save_notes(notes)
    print("������� ���������.")


# ������� ��� ������ ���� ������� �� �����


def read_notes():
    try:
        with open("note.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


with open("note.json", "r") as file:
    notes = json.load(file)
# ������� ��� ������� � �������
if notes:
    for id, title, body in notes.items():
        print(f"���������: {id}")
        print(f"���������: {title}")
        print(f"����������: {body}")
else:
    print("������� ���� ���.")

# ������� ��� �������������� �������


def edit_note():
    id = input(
        "������� ������������� �������, ������� ���������� ���������������: ")
    with open("note.json", "r") as file:
        notes = json.load(file)
    for note in notes:
        if note["id"] == id:
            title = input("������� ����� ��������� �������: ")
            body = input("������� ����� ����� �������: ")
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            note["title"] = title
            note["body"] = body
            note["date_modified"] = date
            note["time_modified"] = time
    with open("note.json", "w") as file:
        json.dump(notes, file)

# ������� ��� �������� �������


def delete_note():
    id = input("������� ������������� �������, ������� ���������� �������: ")
    with open("note.json", "r") as file:
        notes = json.load(file)
    notes = [note for note in notes if note["id"] != id]
    with open("note.json", "w") as file:
        json.dump(notes, file)