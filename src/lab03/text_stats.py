import sys  #чтобы использовать стандартный ввод

sys.path.append('c:/Users/daria/OneDrive/Рабочий стол/python_labs/src')
from lib.text import count_freq, normalize, tokenize, top_n


def main():

    text=sys.stdin.read()#читаю весь ввод до EOF (ctr+Z+En)
    if not text: #если нет ничего на входе
        return "текста нет"

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    count_word = count_freq(tokens)
    top_words = top_n(count_word, 5)
    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(count_word))
    print('Топ-5:')
    for word, count in top_words:
        print(f'{word}:{count}')
main()

