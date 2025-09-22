name=input('ФИО:')
name=name.split()

initsial=[name[i][0] for i in range(len(name))]

initsial=''.join(initsial)

name=''.join(name)
long=len(name)+2


print(f'Инициалы: {initsial}')
print(f'Длина(символов): {long}')