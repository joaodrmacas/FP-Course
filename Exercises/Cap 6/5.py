def filtra(lst,tst):
    l = []
    for el in lst:
        if tst(el):
            l.append(el)
    return l

def transforma(lst,fn):
    l = []
    for el in lst:
        l.append(fn(el))
    return l

def acumula(lst, fn):
    def acumula_aux(acc, lst, fn):
        if len(lst) == 0:
            return acc
        return acumula_aux(fn(acc, lst[0]), lst[1:], fn)

    return acumula_aux(0, lst, fn)

def soma_quadrados_impares(list):
    return acumula(transforma(filtra(list,lambda x: x%2 != 0),lambda x: x**2),lambda x,y: x+y)

print(soma_quadrados_impares([1,2,3,4,5,6]))