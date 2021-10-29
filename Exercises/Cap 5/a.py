def remdup(lista):
    if type(lista) != list:
        raise ValueError("parametros errados")
    i,j = 0,1
    while i < len(lista):
        while j<len(lista):
            if lista[i] == lista[j]:
                del lista[j]
            j += 1
        i += 1
        j = 1 + i
    return lista

print(remdup([1,3,2,5,6,2,3,5,3,1]))