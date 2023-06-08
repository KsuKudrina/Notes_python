import datetime
import view as v
import actions as act

def main():
    while True:
        mode = v.get_mode()
        if mode == 1:
            data_new_note = v.get_add_new_note()
            act.append_to_csv(act.get_last_id(), data_new_note)
            print("Заметка добавлена")

        elif mode == 2:
            data_notes = act.read_csv()
            print("\nСписок всех заметок: \n")
            v.print_to_screen(data_notes)

        elif mode == 3:
            start_date = datetime.datetime.strptime(input("\nВведите начальную дату (дд/мм/гггг )"), "%d/%m/%Y")
            end_date = datetime.datetime.strptime(input("\nВведите конечную дату (дд/мм/гггг )"), "%d/%m/%Y")
            print("\nНайденные по датам Заметки: \n")
            v.print_to_screen(find_notes_by_dates(start_date, end_date))

        elif mode == 4:
            print("\nИщем Заметку и выводим ее на экран:\n")
            find_note(input("Введите искомое"))

        elif mode == 5:
            old_id = input("Введите ID: ")
            new_note = v.get_add_new_note()
            act.replacement_note(new_note, old_id)
            print("Данные сохранены")

        elif mode  == 6:
            del_id = input("Введите ID: ")
            new_note = find_note_by_id(del_id)
            new_note[0]["title_note"] = "Note deleted"
            new_note[0]["text_note"] = "null"
            act.replacement_note(new_note, del_id)
            print("Данные удалены")

        elif mode == 7:
            print('Bye!\n')
            break
        print('\n')


def find_note(find_data):
    notes_data = act.read_csv_to_arr()
    found_list = []
    for line in notes_data:
        for elem in line:
            if find_data in elem:
                found_list.append(line)
                break
    if found_list > []:
        print('\n')
        v.print_to_screen(found_list)
    else:
        print('Заметка не найдена')
    return

def find_note_by_id(num_id) -> list:
    notes_data = act.read_csv()
    found_list = []
    for note in notes_data:
        if num_id == note["id"]:
            found_list.append(note)
    return found_list


def find_notes_by_dates(date1, date2) -> list:
    notes_data = act.read_csv()
    found_list = []
    for note in notes_data:
        date_note = datetime.datetime.strptime(note["date_note"], '%Y-%m-%d %H:%M:%S.%f')
        if (date1 < date_note < date2):
            found_list.append(note)
    return found_list
