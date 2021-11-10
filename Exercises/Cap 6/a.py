def um_rl(n):
    if n==0:
        return 0
    return n+n-1 + um_rl(n-1)

def um_rc(n):
    def aux(n,acc):
        if n==0:
            return acc
        return aux(n-1,acc+n+n-1)
    return aux(n,0)

def um_il(n):
    res = 0
    while n>0:
        res += n+n-1
        n-=1
    return res

def dois_rl(n):
    if n//10:
        return 0
    return 1 + dois_rl(n-1)

def dois_rc(n):
    def aux(n,acc):
        if n==0:
            return acc
        return aux(n//10,acc+1)
    return aux(n,0)

print(dois_rc(1230))