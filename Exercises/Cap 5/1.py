def lista_codigos(str):
    list = []
    for i in str:
        list.append(ord(i))
    return list

print(lista_codigos("bom dia"))