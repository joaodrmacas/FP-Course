def implode(tup):
    a = 0
    for i in range(len(tup)):
        a = a*10 + tup[i]
    return a

print(implode((3,4,0,0,4)))