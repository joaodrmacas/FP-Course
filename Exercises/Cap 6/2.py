def piatorio(l_inf,l_sup,produto):
    res = 0
    while l_inf<=l_sup:
        res += produto(l_inf,l_sup)
        l_inf += 1
    return res

print(piatorio(2,4,lambda x,y: x*y))

