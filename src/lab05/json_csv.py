import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:

    """
    Преобразовать JSON-файл в CSV.

    Подаётся:
        json_path: путь к JSON-файлу (строка или Path).
        csv_path: путь к создаваемому CSV-файлу (строка или Path).
        encoding: кодировка для чтения и записи файлов (по умолчанию "utf-8").

    Действие:
        - Читает JSON.
        - Определяет заголовки по ключам первого словаря.
        - Создаёт CSV с заголовком и строками из JSON.

    Ошибки:
        FileNotFoundError: Если JSON-файл отсутствует.
        ValueError: Если JSON пустой, не является списком словарей
                    или имеет неподдерживаемую структуру.
                    Если JSON-файл содержит синтаксические ошибки.
    """
   
    file_json=Path(json_path)

    if not file_json.exists():
        raise FileNotFoundError("файл не найден")
    
    try:
        with file_json.open('r',encoding='utf-8') as f:
            dano=json.load(f)
    except json.JSONDecodeError:
        raise ValueError("неподдерживаемая структура")

    except not isinstance(dano,list):
        raise ValueError("JSON должен быть быть в виде списка объектов")

    if len(dano)==0:
        raise ValueError("JSON файл пуст")

    if not all(isinstance(item, dict) for item in dano):
        raise ValueError("Каждый элемент JSON должны быть словарями")

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            header=tuple(dano[0].keys())
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(dano)


            

json_to_csv("data/samples/people.json","data/out/people_from_json.csv")