def elemento_matriz(mat,l,c):
    if l >= len(mat):
        raise ValueError('elemento_matriz: indice invalido, linha {}'.format(l))
    if c >= len(mat[0]):
        raise ValueError('elemento_matriz: indice invalido, coluna {}'.format(c))
    return mat[l][c]

m= [[1,2,3], [4,5,6]]
print(elemento_matriz(m,0,3))