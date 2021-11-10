def rl(tuplo):
    if tuplo == ():
        return 0
    if tuplo[-1]%2 == 0:
        return 1 + rl(tuplo[:-1])
    return rl(tuplo[:-1])

print(rl((1,2,3,4,5,6)))