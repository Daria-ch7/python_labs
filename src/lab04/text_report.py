import sys #чтобы использовать стандартный ввод
sys.path.append('c:/Users/daria/OneDrive/Рабочий стол/python_labs/src')
from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

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
