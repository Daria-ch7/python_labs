import sys
sys.path.append('c:/Users/daria/OneDrive/Рабочий стол/python_labs')
from io_txt_csv import read_text, write_csv
from lib.text import normalize, tokenize, count_freq, top_n

'''
Анализ текста и сохранение отчёта в CSV.
Действия:
    1. Чтение входного текстового файла (data/input.txt).
    2. Нормализация и токенизация текста (функции из src/lib/text.py).
    3. Подсчёт частоты слов.
    4. Сохранение результата в CSV (data/report.csv)
        с заголовком: word,count (отсортировано по убыванию частоты, затем по слову).
    5. Вывод в консоле:
        - количество всех слов
        - количество уникальных слов
        - топ-5 слов (в табличной форме или в виде списка).
'''

p=read_text("data/input.txt")
norm_p=normalize(p)
tokens=tokenize(norm_p)
count_word=count_freq(tokens)
top=top_n(count_word)

write_csv(top, "data/report.csv", ["word", "count"])

print("Всего слов:", len(tokens))
print("Уникальных слов:", len(count_word))
print("Топ-5:")
for x,y in top[:5]:
    print(f'{x}:{y}')
