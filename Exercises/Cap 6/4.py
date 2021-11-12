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

def acumula(lst,fn):
    soma = 0
    i=0
    while i<len(lst):
        soma += fn(lst[i],lst[i+1])
        i+=2
    return soma
