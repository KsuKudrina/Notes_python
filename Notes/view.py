import datetime


def get_mode() -> int:
    print("=" * 20)
    print("*Меню* \n ")
    print("1. Создать Заметку")
    print("2. Вывести список всех Заметок")
    print("3. Найти Заметки по датам")
    print("4. Найти и вывести Заметку на экран")
    print("5. Редактировать Заметку")
    print("6. Удалить Заметку")
    print("7. Выход")
    print("=" * 20 + "\n")
    return int(input("Выберите действие: "))


def get_add_new_note():
    new_note = []
    temp = {}
    temp["id_note"] = "temp"
    temp["title_note"] = input("Введите заголовок: ")
    temp["text_note"] = input("Введите текст: ")
    temp["date_note"] = datetime.datetime.now()
    new_note.append(temp)
    return new_note


def print_to_screen(notes_arr: list):
    sorted_notes_arr = sorted(notes_arr, key=lambda x: x["date_note"], reverse = True)
    for note in sorted_notes_arr[:]:
        print("ID    - " + note["id"])
        print("Title - " + note["title_note"])
        print("Text  - " + note["text_note"])
        print("Date  - " + note["date_note"])
        print()
