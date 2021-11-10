#rl

def apenas_digitos_impares(n):
    res = 0
    i = 0
    while n!=0:
        dig = n%10
        if dig%2 != 0:
            res = res + dig*(10**i)
            i+=1
        n = n//10
    return res


def linear(n):
    if n == 0:
        return 0
    digito = n % 10

    if digito % 2 == 0:
        return linear(n // 10)
    else:
        return linear(n // 10) * 10 + digito

def misterio(x,n):
    def aux(x,n,acc):
        if n==0:
            return acc
        return aux(x,n-1,acc+ x*n)
    return aux(x,n,0)

def m1(x,n):
    if n==0:
        return 0
    else:
        return x*n + m1(x,n-1)

print(m1(2,3))