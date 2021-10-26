def matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j],end=" ")
        print("")

m= [[1,2,3], [4,5,6]]
matriz(m)