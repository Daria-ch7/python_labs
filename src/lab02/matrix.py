
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

#print(row_sums([[-1,1],[10,-10]]))

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

#print(col_sums([[1, 2, 3], [4, 5, 6]]))