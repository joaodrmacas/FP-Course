
#a)

def perfeito(n):
    def aux(n,d,acc):
        if n==d:
            if acc == n:
                return True
            return False
        if n%d == 0:
            return aux(n,d+1,acc+d)
        else:
            return aux(n,d+1,acc)
    return aux(n,1,0)

#b)

def perfeitos_entre(a,b):
    if a == b:
        return []
    if perfeito(a):
        return [a,] + perfeitos_entre(a+1,b)
    return perfeitos_entre(a+1,b)
