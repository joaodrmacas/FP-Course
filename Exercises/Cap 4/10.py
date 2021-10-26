from math import ceil
def codifica(str):
    par = ""
    impar = ""
    for i in range(len(str)):
        if i%2 != 0:
            impar += str[i]
        else:
            par += str[i]
    return par + impar

def descodifica(str):
    palavra = ""
    middle = ceil(len(str)/2)
    for i in range(middle):
        palavra += str[i]
        if i + middle < len(str):
            palavra += str[i+middle]
    return palavra
