#a)
def numero_dig_rl(n):
    if n==0:
        return 0
    return 1 + numero_dig_rl(n//10)

#b)

def numero_dig_rc(n):
    def aux(n,acc):
        if n==0:
            return acc
        return aux(n//10,acc+1)
    return aux(n,0)

#c)

def numero_dig_il(n):
    res = 0
    while n>0:
        n//=10
        res+=1
    return res

print(numero_dig_il(10))
