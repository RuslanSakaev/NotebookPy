from createNote import *

# Основной цикл приложения
while True:
    print("Выберите действие:")
    print("1. Создать новую заметку")
    print("2. Просмотреть все заметки")
    print("3. Редактировать существующую заметку")
    print("4. Удалить существующую заметку")
    print("5. Выйти из приложения")
    choice = input("Выберите опцию: ")
    if choice == "1":
        create_note()
    elif choice == "2":
        print(read_notes())
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")