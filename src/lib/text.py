def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Если casefold=True — привести к casefold
    Если yo2e=True — заменить все ё/Ё на е/Е.
    Убрать невидимые управляющие символы (например, \t, \r) → заменить на пробелы, схлопнуть повторяющиеся пробелы в один.
    '''

    if casefold==True:
        text=text.casefold()
        #привожу к нижнему регистру
        
    if yo2e==True:
        text=text.replace('ё','е').replace('Ё','Е')
        #заменяю ё/Ё

    text=text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    #заменяю управляющие символы
    
    text=text.split() #разбиваю по пробелу (получу список слов)

    text=' '.join(text) #соединяю эдементы в списке(слова) через пробел

    return text
#print(normalize("Hello\r\nWorld"))



import re

def tokenize(text: str) -> list[str]:

    '''
    Разбить на «слова» по небуквенно-цифровым разделителям.
    В качестве слова считаем последовательности символов \w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
    Числа (например, 2025) считаем словами.
    '''
    pattern= r'\b\w+(?:-\w+)*\b'

    tokens=re.findall(pattern,text)

    return tokens
#print(tokenize("emoji 😀 не слово"))


def count_freq(tokens: list[str]) -> dict[str, int]:

    '''
    Подсчитать частоты, вернуть словарь слово → количество
    '''
    word_count={}

    for word in tokens:
        word_count[word]=word_count.get(word,0)+1 #если слово есть в словаре, то get возвращает его количество, если нет, то 0

    return(word_count)
#print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_word=sorted(freq.items(), key=lambda x: (x[1]),reverse=1)
    sorted_word=sorted(freq.items(), key=lambda x: (x[0]))

    return sorted_word[:n]

tokens=["bb","aa","bb","aa","cc"]

freq_dict = count_freq(tokens)

result = top_n(freq_dict, 2)

print(result)



