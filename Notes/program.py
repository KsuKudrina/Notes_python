import view as v
import actions as act

def main():
    while True:
        menu = v.menu()
        if menu == 1:
            print("\n")
            new_note = v.add_note()
            act.add_to_file(act.get_id, new_note)
            print("Заметка добавлена")

