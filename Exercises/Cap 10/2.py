def a(name):
    vogais = {"a":0,"e":0,"i":0,"o":0,"u":0}
    a = open(name,"r")
    for line in a:
        for letra in line:
            for key in vogais:
                if key == letra:
                    vogais[key]+=1
    return vogais

print(a("a.txt"))