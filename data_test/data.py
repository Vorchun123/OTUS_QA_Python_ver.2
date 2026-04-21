import csv
import json
from pathlib import Path
from typing import Union

CURRENT_DIR = Path(__file__).resolve().parent


def read_and_modify_csv(file_name: str):
    file_path = CURRENT_DIR / 'data' / file_name
    modify_csv = []
    with open(file_path, "r", encoding='utf-8', newline='') as f:
        default_csv = csv.DictReader(f)
        for books in default_csv:
            new_csv = {'Title': books['Title'], 'Author': books['Author'],
                       'Pages': books['Pages'], 'Genre': books['Genre']}
            modify_csv.append(new_csv)
        return modify_csv


def read_and_modify_json(file_name: str):
    file_path = CURRENT_DIR / 'data' / file_name
    modify_json = []
    with open(file_path, 'r', encoding='utf-8') as f:
        default_json = json.load(f)
        for i in default_json:
            new_json = {'name': i['name'], 'gender': i['gender'],
                        'address': i['address'], 'age': i['age'], 'books': []}
            modify_json.append(new_json)
        return modify_json


def distribution_books(user_json, book):
    a = 0
    b = 0
    while a < len(book):
        if b < len(user_json):
            user_json[b]['books'].append(book[a])
            b += 1
        else:
            b = 0
        a += 1
    return user_json


def write_json(file_name: str, file: Union[list, dict]):
    file_path = CURRENT_DIR / 'data' / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(file, f, indent=4)


data = distribution_books((read_and_modify_json('users.json')), (read_and_modify_csv('books.csv')))
write_json('result.json', data)

