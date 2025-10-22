def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

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




import re

def tokenize(text: str) -> list[str]:

    pattern= r'\w+(?:-\w+)*'

    tokens=re.findall(pattern,text)

    return tokens
print(tokenize("emoji 😀 не слово"))




def count_freq(tokens: list[str]) -> dict[str, int]:

    word_count={}

    for word in tokens:
        word_count[word]=word_count.get(word,0)+1 #если слово есть в словаре, то get возвращает его количество, если нет, то 0

    return(word_count)




def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_word=sorted(freq.items(), key=lambda x: (x[0])) #сортирую по алфавиту
    sorted_word=sorted(freq.items(), key=lambda x: (x[1]),reverse=1) #сортирую количеству в обратном порядке


    return sorted_word[:n]

tokens=["bb","aa","bb","aa","cc"]

freq_dict = count_freq(tokens)

result = top_n(freq_dict, 2)

