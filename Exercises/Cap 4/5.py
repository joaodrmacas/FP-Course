def explode(i):
    tup = ()
    while i > 0:
        tup = (i%10,) + tup
        i//=10
    return tup

def implode(tup):
    a = 0
    for i in range(len(tup)):
        a = a*10 + tup[i]
    return a

def filtra_pares(tup):
    t = ()
    if type(tup) != tuple:
        raise ValueError("erro")
    for i in range(len(tup)):
        if type(tup[i]) != int:
            raise ValueError("erro")
        if tup[i]%2 == 0:
            t += (tup[i],)
    return t

def algarismos_pares(i):
    return implode(filtra_pares(explode(i)))

print(algarismos_pares(664339976641))