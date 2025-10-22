import sys #чтобы использовать стандартный ввод 
from src.lib.text import normalize, tokenize, count_freq, top_n

def main():

    text=sys.stdin.read().strip()#читаю весь ввод до EOF (ctr+Z+En)
    if not text: #если нет ничего на входе
        return "текст не виден"

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    count_word = count_freq(tokens)
    top_words = top_n(count_word, 5)
    print("Всего слов:", len(tokens))
    print("Уникальных слов:", len(count_word))
    print('Топ-5:')
    for word, count in top:
        print(f'{word}:{count}')
if __name__ == "__main__":
    main()



