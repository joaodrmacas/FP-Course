def il(tuplo):
    new = ()
    i = len(tuplo)-1
    while i>=0:
        new += (tuplo[i],)
        i-=1
    return new

def rc(tuplo):
    def aux(tuplo,leng,acc):
        if leng<0:
            return acc
        acc += (tuplo[leng],)
        return aux(tuplo,leng-1,acc)
    acc = ()
    leng = len(tuplo)-1
    return aux(tuplo,leng,acc)

def rl(tuplo):
    if tuplo == ():
        return ()
    return (tuplo[-1],) + rl(tuplo[:-1])

print(rl((1,2,True)))