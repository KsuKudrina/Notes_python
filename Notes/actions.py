import csv
import datetime

def get_last_id() -> int:
    with open('notes.csv', 'r') as file:
        count_notes = 0
        csv_reader = csv.reader(file)
        for row in csv_reader:
            count_notes += 1           
    return count_notes

def append_to_csv(last_id, data_new_note):
    notes = read_csv()
    temp={}
    temp["id"] = last_id + 1
    temp["title_note"] = data_new_note[0]["title_note"]
    temp["text_note"] = data_new_note[0]["text_note"]
    temp["date_note"] = datetime.datetime.now()
    notes.append(temp)
    write_csv(notes)

def read_csv() -> list[dict]:
    notes = []
    with open('notes.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = row[0]
            temp["title_note"] = row[1]
            temp["text_note"] = row[2]
            temp["date_note"] = row[3]
            notes.append(temp)
    return notes

def write_csv(notes: list):
    with open('notes.csv', 'w', encoding='utf-8', newline="") as fout:
        csv_writer = csv.writer(fout, delimiter= ';')
        for note in notes:
            csv_writer.writerow(note.values())

def read_csv_to_arr() -> list:
    notes_arr = []
    with open('notes.csv', 'r', encoding='utf-8') as fin:
        csv_converter = fin.readlines()
        for line in csv_converter:
            line_arr = line.split(';')
            notes_arr.append(line_arr)      
    return notes_arr

def replacement_note(new_note, id_note):
    full_data = read_csv()
    for note in full_data:
        if note["id"] == id_note:
            note["title_note"] = new_note[0]["title_note"]
            note["text_note"] = new_note[0]["text_note"]
            note["date_note"] = datetime.datetime.now()
            break
    write_csv(full_data)