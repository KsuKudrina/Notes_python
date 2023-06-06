import csv
import datetime

def get_id() -> int:
    with open('notes.csv', 'r') as file:
        count_ = 0
        csv_reader = csv.reader(file)
        for row in csv_reader:
            count_ += 1           
    return count_

def add_to_file(last_id, new_note):
    notes = read_note()
    temp={}
    temp["id"] = last_id + 1
    temp["title_note"] = new_note[0]["title_note"]
    temp["text_note"] = new_note[0]["text_note"]
    temp["date_note"] = datetime.datetime.now()
    notes.append(temp)
    write_csv(notes)

def read_note() -> list[dict]:
    notes = []
    with open('notes.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
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
        csv_writer = csv.writer(fout)
        for note in notes:
            csv_writer.writerow(note.values())

