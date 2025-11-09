import json
import csv
from pathlib import Path


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразовать CSV-файл в JSON.

    Подаётся:
        csv_path: путь к CSV-файлу (строка или Path).
        json_path: путь к создаваемому JSON-файлу (строка или Path).
        encoding: кодировка для чтения и записи файлов (по умолчанию "utf-8").

    Действие:
        - Читает CSV с заголовком.
        - Преобразует строки CSV в список словарей.
        - Записывает JSON с отступами для удобного чтения.

    Ошибки:
        FileNotFoundError: Если CSV-файл отсутствует.
        ValueError: Если CSV не содержит заголовков или пуст.
                    Если структура CSV-файла некорректна.
    """
    file_csv=Path(csv_path)
    
    if not file_csv.exists():
        raise FileNotFoundError("Файл не найден")
    
    if file_csv.suffix != ".csv":
        raise ValueError("Неверный тип данных")
    
    with open(file_csv, "r", encoding='utf-8') as f:
        reader=csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("Отсутствуют заголовки в файле")
        dano=list(reader)
    if len(dano)==0:
        raise ValueError("Пустой файл")
    
    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(dano, f, ensure_ascii=False, indent=2)

csv_to_json("data/samples/my_test2.csv","data/out/my_test2.json")