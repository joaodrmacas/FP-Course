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

print(filtra_pares((2,5,6,7,9,1,8,8)))