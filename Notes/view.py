import datetime

def menu() -> int:
    print("Выберите необходимое действие: ")
    print("1. Создать Заметку")
    print("2. Вывести список всех Заметок")
    print("3. Найти Заметки по дате")
    print("4. Найти и вывести Заметку на экран")
    print("5. Редактировать Заметку")
    print("6. Удалить Заметку")
    print("7. Выход")
    print("\n")
    return int(input("Выберите действие: "))

def add_note():
    new_note = []
    temp = {}
    temp["id_note"] = "temp"
    temp["title_note"] = input("Введите заголовок: ")
    temp["text_note"] = input("Введите текст: ")
    temp["date_note"] = datetime.datetime.now()
    new_note.append(temp)
    return new_note
