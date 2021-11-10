#a)
def quadrado_rl(n):
    if n<=1:
        return 1
    else:
        return n+n-1 + quadrado_rl(n-1)

#b)

def quadrado_rc(n):
    def quadrado_aux(n,acc):
        if n<=0:
            return acc
        return quadrado_aux(n-1,acc+n+n-1)
    return quadrado_aux(n,0)

#c)

def quadrado_il(n):
    res = 0
    while n>0:
        res += n+n-1
        n-=1
    return res
