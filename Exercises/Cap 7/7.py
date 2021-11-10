def calc_soma(x,n):
    def aux(x,n,i,acc,prev):
        if i>n:
            return acc
        return aux(x,i+1,n,acc + prev*(x/i),prev*(x/i))
    return aux(x,1,n,1,1)