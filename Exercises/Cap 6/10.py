from functools import reduce

def lista_digitos(n):
    return list(map(lambda x: int(x), str(n)))

def apenas_digitos_impares(n):
    return filter(lambda x: x%2 != 0,lista_digitos(n))