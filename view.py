class View:
    def greeting(self):
        print("���������� �������. ")

    def show_main_menu(self):
        print("�������� ��������:\n"
              "\t1. �������� �������\n"
              "\t2. ���������, �������� ��� ������� �������\n"
              "\t3. �������� ������ �������\n"
              "\t4. ��������� �������\n"
              "\t0. ����� �� ����������")

    def show_manage_note_menu(self):
        print("�������� ��������:\n"
              "\t1. ��������� \n"
              "\t2. �������� \n"
              "\t3. ������� \n")

    def error(self):
        print("����� ������� �� ���������! ���������� �����:")

    def not_found(self):
        print("�������� �� �������. ���������� �����: ")

    def saved_info(self):
        print("������� ������� ��������� � ����")

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)

    def show_read_all_banner(self, count):
        result = f"\t������ �������. \n" \
                 f"����� ������� �������: {count}\n"
        print(result)

    def info_note_msg(self, key):
        info = {'add': '���������', 'del': '�������', 'edit': '��������'}
        print(f"������� ������� {info[key]}!")

    def input_note_name(self):
        return input(f"������� �������� �������:")

    def input_note_text(self):
        return input(f"������� ���������� �������:")

    def edit_note(self, note):
        note.set_text(self.input_note_text())
        note.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': '�������', 'menu': '������ ����'}
        value = 0
        while True:
            try:
                value = int(input(f"������� ����� {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("������� �� ������������� ������ �������!")