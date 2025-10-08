## Лабораторная работа 1
### 1 номер

```
name=input('Имя:')
age=int(input('Возраст:'))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```
![01_greeting](./images/lab1/лаб1.1.png)

### 2 номер

```
a=float(input('a:'))
b=float(input('b:'))
sum=a+b
avg=(a+b)/2
print(f'sum={sum:.2f}; avg={avg:.2f}')
```
![02_sum_avg](./images/lab1/lab1.2.png)

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
![03_discount_vat](./images/lab1/lab1.3.png)

### 4 номер

```
m=int(input('Минуты:'))
hours=m//60
minutes=m-(60*hours)
print(f'{hours}:{minutes:02d}')
```
![04_minutes_to_hhmm](./images/lab1/lab1.4.png)

### 5 номер 

```
name=input('ФИО:')
name=name.split()

initsial=[name[i][0] for i in range(len(name))]

initsial=''.join(initsial)

name=''.join(name)
long=len(name)+2


print(f'Инициалы: {initsial}')
print(f'Длина(символов): {long}')
```
![05_initials_and_len](./images/lab1/lab1.5.png)

## Лабораторная работа 2

### Задание 1
### 1

```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем кортеж из двух чисел (целых/с плав. точкой)'''

    if len(nums)==0:
        return ValueError

    maxi_el=-10**10
    mini_el=10**10

    for i in range(len(nums)):
        if nums[i] > maxi_el:
            maxi = nums[i]
        if nums[i] < mini_el:
            mini = nums[i]

    return (mini, maxi)

print(min_max([-5,-2,-9]))
```
![arrays.py](/images/lab2/lab2.1(1).png)

### 2

```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем список, содержащий числа (целые/с плав. точкой)'''

    if len(nums)==0:
        return ValueError
    
    return sorted(set(nums))
'''сначала создаем список уникальных значений, потом сортируем его'''

print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![arrays.py](/images/lab2/lab2.1(2).png)

### 3

```
def flatten(mat: list[list | tuple]) -> list:
    '''принимаем список, содержащий целые числа или числа с плавающей точкой; возвращаем список'''
    itog_list=[]
    for element in mat:
        if isinstance(element,(list,tuple)):
            '''проверяю, что эл-т из списка действительно является списком/кортежем''' 
            for member in element:     
                '''добавляю каждый эл-т списка/кортежа из принятого списка'''          
                itog_list.append(member)
        else:
            return TypeError 
        '''если у меня эл-т в исходном списке не список/кортеж, то выдаем ошибку'''               
    return itog_list
print(flatten(([1, 2], (3, 4, 5))))
```
![arrays.py](/images/lab2/lab2.1(3).png)


### Задание В

### 1

```
def transpose(mat: list[list[float | int]]) -> list[list]:
    '''принимаем список списков, содержащих числа (целые или с плав. точкой); возвращаем список списков'''
    if len(mat)==0:
        return []
    '''проверка на пустую матрицу'''
    
    if len(mat)>0:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]): return ValueError
            '''прохожусь по эл-ам матрицы и сравниваю их длины, если они разные, выводим ошибку'''
    transposed=[]
    num_rows=len(mat)
    num_cols=len(mat[0])
    '''пустая матрица для рузультата, где кол-во строк=длина первой строки исходной матрицы, а кол-во столбцов=кол-во строк исходной матрицы'''
    for i in range(num_cols):
        '''прохожусь по индексам столбцов исходной матрицы (это будут строки в новой)'''
        new_row=[]
        for j in range(num_rows):
            '''прохожусь по индексам строк исходной матрицы (столбцы в новой)''' 
            new_row.append(mat[j][i])
        transposed.append(new_row)
   
    return transposed
print(transpose([[1, 2], [3, 4]]))
```
![matrix.py](/images/lab2/lab2.B(1).png)

### 2

```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''принимаем список списков, содержащих числа (целые или с плав. точкой); возвращаем список чисел с плавающей точкой'''

    if len(mat)==0:
        return []
    
    if len(mat)>0:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]): return ValueError
  
    symma_stroki=[]
    for stroka in mat:
        symma_stroki.append(sum(stroka))
        '''беру строку из матрицы и добавляю в созданный список ее сумму'''
    return symma_stroki

print(row_sums([[-1,1],[10,-10]]))
```
![matrix.py](/images/lab2/lab2.B(2).png)

### 3

```
def col_sums(mat: list[list[float | int]]) -> list[list]:

    if len(mat)==0:
        return []

    if len(mat)>0:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]): return ValueError

    syms = [0]*len(mat[0])
    '''создаю список, в котором содержится количество нулей, равное длине строк в матрице'''

    for i in range(len(mat)): 
        for j in range(len(mat[i])): 
            syms[j]+=mat[i][j] 
    '''прохожусь по строкам в матрице'''
    '''выбираю строку из матрицы и прохожусь по ней'''
    '''прибавляю значеня столбцов к соответствующему значению в списке syms'''
    return syms
print(col_sums([[1, 2, 3], [4, 5, 6]]))
```
![matrix.py](/images/lab2/lab2.B(3).png)

### Задание C

```
def format_record(rec: tuple[str, str, float]) -> str:
    '''на вход подается кортеж, который инвертируется в строку'''

    if len(rec)!=3:
        return ValueError
    
    name=rec[0].strip()
    group=rec[1].strip()
    gpa=rec[2]

    
    

    if ( (len(name)>1) + ( (len(group)!=0) and isinstance(group, str) ) + (isinstance(gpa, float)) )!=3:
        return ValueError
    '''делаю проверку всех условий (если что-то неправильно, выводится ошибка)'''
    
    name=name.title().split()
    '''с помощью метода title() делаю каждый элемент имени с заглавной буквой и разделяю их по пробелу'''
    if len(name)==3:
        fio=f'{name[0]} {name[1][0]}.{name[2][0]}.'
        
    if len(name)==2:
        fio=f'{name[0]} {name[1][0]}.'

    GPA=round(gpa,2)
    '''округляю балл до двух знаков'''

    return f'{fio}, гр. {group}, GPA {GPA: .2f}'
print(format_record( ("  сидорова  анна   сергеевна ", "ABB-01", 3.999) ))
```
![tuples.py](/images/lab2/lab2.C.png)

