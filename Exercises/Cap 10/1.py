def conta_linhas(name):
    file = open(name,'r')
    count = 0
    for line in file:
        if not line == "\n" or line == "":
            count+=1
    return count

print(conta_linhas("a.txt"))