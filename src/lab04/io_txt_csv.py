import sys

sys.path.append("c:/Users/daria/OneDrive/Рабочий стол/python_labs/src")

import csv
from collections import Counter
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое в виде одной строку.

    Что подаётся (аргументы):
        path: Путь к файлу (строка или объект Path)
        encoding: Кодировка файла. По умолчанию 'utf-8'

    Что возвращается:
        str: Данные файла как строку

    Падает с ошибками:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если указанная кодировка не подходит для файла

    Пример выбора кодировки:
        read_text("file.txt")  # Чтение в UTF-8
        read_text("file.txt", encoding="cp1251")  # Чтение в Windows-1251
    """

    p = Path(path)
    # преобразовывает в "умный" объект, если подана строка, чтобы было легче работать

    if not p.exists():
        raise FileNotFoundError
    # проверка на существование файла

    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создать/перезаписать CSV с разделителем ",".

    аргументы:
        rows - принимает строки, каждая из которых - список/кортеж
        path - куда сохранить файл (строка или объект Path)
        header - заголовки столбцов (можно не указывать)

    Падает с ошибкой:
        ValueError: если строки имеют разную длину.

    Вывод:
        None - ничего не возвращает, просто сохраняет файл
    """
    p = Path(path)
    rows = list(
        rows
    )  # создаю список из полученных строк(которые представлены как список/кортеж)

    # проверка на одинаковую длину:
    for i in range(1, len(rows)):
        if len(rows[i - 1]) != len(rows[i]):
            raise ValueError

    with p.open("w", newline="", encoding="utf-8") as f:  # открываю файл для записи
        w = csv.writer(f)  # специальный объект для записи СSV
        if header is not None:
            w.writerow(
                header
            )  # если указаны заголовки, то они записываются первой строкой
        for r in rows:  # записываю далее остальные строки
            w.writerow(r)


def frecquencies_from_text(text: str) -> dict[str, int]:
    """
    Посчитать частоты слов в тексте, используя функции из ЛР3

    Подается:
        text - исходный текст (тип строковой)

    Выводится:
        dict[str, int] - словарь {слово: частота}
    """
    from lib.text import normalize, tokenize

    text = normalize(text)
    tokens = tokenize(text)

    return Counter(
        tokens
    )  # это специальный счётчик, который сам подсчитывает элементы (замена ручного подсчёта через словарь)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Сортировка пар (слова, частота):
        - по убыванию частоты
        - по алфавиту

    Подаётся:
        freq - словарь {слово: частота}

    Выыодится:
        отсортированный список
    """
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))
