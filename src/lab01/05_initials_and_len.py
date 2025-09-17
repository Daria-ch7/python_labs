name=input()
short_name=''
for i in name.split():
    short_name+=i[:1]
long=len(name)
print(f'ФИО: {name}')
print(f'Инициалы: {short_name}')
print(f'Длина: {long}')