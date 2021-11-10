def g(n):
    if n == 0:
        return 0
    return n-g(g(n-1))

print(g(3))