import argparse

from src.lib.csv_xlsx import csv_to_xlsx
from src.lib.json_csv import csv_to_json, json_to_csv


def main():
    """
    Обернуть функции конвертации текста в CLI-оболочку с помощью argparse.

    Предоставляет возможность конвертировать файлы между форматами:
        JSON <-> CSV и CSV -> XLSX.

    Подкоманды:
        json_to_csv — конвертировать JSON в CSV
        csv_to_json — конвертировать CSV в JSON
        csv_to_xlsx — конвертировать CSV в XLSX

    Ошибки:
        FileNotFoundError — если указанный входной файл не существует.
        ValueError — если структура входных данных некорректна.
    """
    parser = argparse.ArgumentParser(description="Конвертер данных между форматами")
    subparsers = parser.add_subparsers(
        dest="command", help="Доступные команды конвертации"
    )

    json_to_csv_parser = subparsers.add_parser(
        "json_to_csv", help="Конвертировать JSON в CSV"
    )
    json_to_csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON файл"
    )
    json_to_csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV файл"
    )

    csv_to_json_parser = subparsers.add_parser(
        "csv_to_json", help="Конвертировать CSV в JSON"
    )
    csv_to_json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv_to_json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON файл"
    )

    csv_to_xlsx_parser = subparsers.add_parser(
        "csv_to_xlsx", help="Конвертировать CSV в XLSX"
    )
    csv_to_xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv_to_xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX файл"
    )

    args = parser.parse_args()

    if args.command == "json_to_csv":
        json_to_csv(json_path=args.input, csv_path=args.output)

    elif args.command == "csv_to_json":
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.command == "csv_to_xlsx":
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)


if __name__ == "__main__":
    main()
