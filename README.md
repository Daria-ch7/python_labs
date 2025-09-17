<<<<<<< HEAD
# python_lab
### 1 номер

```
name=input('Имя:')
age=int(input('Возраст:'))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![01_greeting](/images/лаб1.1.png)

### 2 номер

```
a=float(input('a:'))
b=float(input('b:'))
sum=a+b
avg=(a+b)/2
print(f'sum={sum:.2f}; avg={avg:.2f}')
```
![02_sum_avg](/images/lab1.2.png)

### 3 номер

```
price=float(input())
discount=float(input())
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
```
![03_discount_vat](/images/lab1.3.png)

### 4 номер

```
m=int(input('Минуты:'))
hours=m//60
minutes=m-(60*hours)
print(f'{hours}:{minutes:02d}')
```
![04_minutes_to_hhmm](/images/lab1.4.png)

### 5 номер 

```
name=input()
short_name=''
for i in name.split():
    short_name+=i[:1]
long=len(name)
print(f'ФИО: {name}')
print(f'Инициалы: {short_name}')
print(f'Длина: {long}')
```
![05_initials_and_len](/images/lab1.5.png)

=======
"# ��1" 
>>>>>>> 80db6462813fd2797bb34e012e1242b84cc4643e
