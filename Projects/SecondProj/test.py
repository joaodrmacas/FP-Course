j,k=0,1
pos = list("abcedaariio")
while j<len(pos):
    k=0
    while k<len(pos):
        if k!=j:
            if pos[j]==pos[k]:
                del pos[k]
                k = k-1
        k += 1
    j += 1
print(pos)