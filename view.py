class View:
    def greeting(self):
        print("This is the Notes app ")

    def show_main_menu(self):
        print("Choose an action:\n"
              "\t1. Add note\n"
              "\t2. Read, edit or delete a note\n"
              "\t3. Show list of notes\n"
              "\t4. Save note\n"
              "\t0. Exit the application")

    def show_manage_note_menu(self):
        print("Choose an action:\n"
              "\t1. Read \n"
              "\t2. Change \n"
              "\t3. Delete \n")

    def error(self):
        print("The number entered is incorrect! Try again:")

    def not_found(self):
        print("Value not found. Try again: ")

    def saved_info(self):
        print("Notes successfully saved to file")

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)

    def show_read_all_banner(self, count):
        result = f"\tList of notes. \n" \
                 f"Total Notes Found: {count}\n"
        print(result)

    def info_note_msg(self, key):
        info = {'add': '1', 'del': '3', 'edit': '2'}
        print(f"Note successfully {info[key]}!")

    def input_note_name(self):
        return input(f"Enter note TITLE:")

    def input_note_text(self):
        return input(f"Enter note CONTENT:")

    def edit_note(self, note):
        note.set_text(self.input_note_text())
        note.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': 'note', 'menu': 'menu item'}
        value = 0
        while True:
            try:
                value = int(input(f"Enter number {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= 4:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("Thank you for using this program!")