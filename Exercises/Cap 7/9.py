def soma_divisores(n):
    def aux(n,d,acc):
        if d>n:
            return acc
        if n%d == 0:
            return aux(n,d+1,acc+d)
        return aux(n,d+1,acc)
    return aux(n,1,0)

print(soma_divisores(210))

