m=int(input('Минуты:'))
hours=m//60
minutes=m-(60*hours)
print(f'{hours}:{minutes:02d}')
