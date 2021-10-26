def explode(i):
    tup = ()
    while i > 0:
        tup = (i%10,) + tup
        i//=10
    return tup
print(explode(34500))