def numero_dig(n):
    res = 0
    while n>0:
        n//=10
        res+=1
    return res

def eh_capicua(n):
    def aux(n,len):
        if n//10 == 0 or len == 1:
            return True
        if n//10**(len-1) == n%10:
            return aux((n-(n//10**(len-1))*10**(len-1))//10,len-2)
        return False
    return aux(n,numero_dig(n))