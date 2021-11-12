def soma_fn(n,fn):
    soma = 0
    for i in range(n):
        soma += fn(i+1)
    return soma

def soma_fn2(n,fn):
    if n==0:
        return 0
    return fn(n) + soma_fn(n-1,fn)

print(soma_fn2(4,lambda x: x*x))