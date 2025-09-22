
def row_sums(mat: list[list[float | int]]) -> list[list]:
    
    if len(mat)>0:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]): return ValueError
    symma=[]
    for stroka in mat:
        symma.append(sum(stroka))
    return symma

#print(row_sums([[-1,1],[10,-10]]))

def col_sums(mat: list[list[float | int]]) -> list[list]:
    if len(mat)>0:
        for i in range(len(mat)-1):
            if len(mat[i])!=len(mat[i+1]): return ValueError

    syms = list(0 for x in range(len(mat[0])))

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            syms[j]+=mat[i][j]

    return syms
print(col_sums([[1, 2, 3], [4, 5, 6]]))