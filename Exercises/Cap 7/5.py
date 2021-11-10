def espelho(n):
    def aux(n,acc):
        a = n//10
        if n == 0:
            return acc
        return aux(a,acc*10 + n%10)
    return aux(n,0)
