class View:
    def greeting(self):
        print("Приложение Заметки. ")

    def show_main_menu(self):
        print("Выберите действие:\n"
              "\t1. Добавить заметку\n"
              "\t2. Прочитать, изменить или удалить заметку\n"
              "\t3. Показать список заметок\n"
              "\t4. Сохранить заметку\n"
              "\t0. Выйти из приложения")

    def show_manage_note_menu(self):
        print("Выберите действие:\n"
              "\t1. Прочитать \n"
              "\t2. Изменить \n"
              "\t3. Удалить \n")

    def error(self):
        print("Число введено не правильно! Попробуйте снова:")

    def not_found(self):
        print("Значение не найдено. Попробуйте снова: ")

    def saved_info(self):
        print("Заметки успешно сохранены в файл")

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)

    def show_read_all_banner(self, count):
        result = f"\tСписок заметок. \n" \
                 f"Всего Найдено заметок: {count}\n"
        print(result)

    def info_note_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def input_note_name(self):
        return input(f"Введите НАЗВАНИЕ заметки:")

    def input_note_text(self):
        return input(f"Введите СОДЕЖРАНИЕ заметки:")

    def edit_note(self, note):
        note.set_text(self.input_note_text())
        note.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("Спасибо за использование данной утилиты!")