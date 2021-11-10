def maior_inteiro(lim):
    def aux(lim,acc,i):
        i+=1
        if lim <= acc+i:
            return i-1
        return aux(lim,acc+i,i)
    return aux(lim,0,1)

print(maior_inteiro(6))
print(maior_inteiro(20))