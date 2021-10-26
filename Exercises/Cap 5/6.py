def matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],end=" ")
        print("")

def soma_mat(mat1, mat2):
    if len(mat1) != len(mat2):
        raise ValueError("Matrices not same size")
    result = mat1 + []
    for rowI in range(len(mat1)):
        if len(mat1[rowI]) != len(mat2[rowI]):
            raise ValueError("Matrices not same size")
        resultRow = mat1[rowI] + []
        for colI in range(len(mat1[rowI])):
            resultRow[colI] = mat1[rowI][colI] + mat2[rowI][colI]
        result[rowI] = resultRow
    return result

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz(soma_mat(m1,m2))