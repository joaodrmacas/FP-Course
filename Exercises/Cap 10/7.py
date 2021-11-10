def ordena_ficheiro(nome):
    with open(nome,"r") as f:
        lines = sorted(f.readlines())
    print(lines)

ordena_ficheiro("a.txt")