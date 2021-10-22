#-------------------------------------------------------------------------------4.1----------------------------------------------------------------------------------

def obter_num_seguranca(security):
    lowest_dif = 2**31-1
    for i in security:
        for j in security:
            dif = i-j
            if dif > 0 and dif<lowest_dif:
                lowest_dif = dif
    return lowest_dif

#-------------------------------------------------------------------------------4.2----------------------------------------------------------------------------------

def convertTuple(tup):
    str = ""
    for i in tup:
        str = str + i
    return str

def decifrar_texto(cifra,security):
    def somar_casas(letra,casas_a_andar):
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        casa_letra = abc.index(letra)
        casa_letra += casas_a_andar
        if(casa_letra) > 25:
            casa_letra -= 26
        return abc[casa_letra]
    casas = security
    while casas > 26:
        casas -= 26
    casas = int(-(-casas // 1)) #arrendondar para cima
    cifra = list(cifra)
    for i in range(len(cifra)):
        casas_a_somar = casas
        if i%2 == 0:
            casas_a_somar += 1
        else:
            casas_a_somar -= 1
        
        if cifra[i] == "-":
            cifra[i] = " "
        else:
            cifra[i] = somar_casas(cifra[i],casas_a_somar)
    return convertTuple(cifra)

#-------------------------------------------------------------------------------4.3-----------------------------------------------------------------------------------

def decifrar_bdb(lista_bdb):
    if type(lista_bdb) != list or len(lista_bdb) < 1:
        raise ValueError("decifrar bdb: argumento invalido")
    new_list = list(range(len(lista_bdb)))
    security_list = list(range(len(lista_bdb)))
    for i in range(len(lista_bdb)):
        if not eh_entrada(lista_bdb[i]):
            raise ValueError("decifrar bdb: argumento invalido")
        security_list[i] = obter_num_seguranca(lista_bdb[i][2])
        new_list[i] = decifrar_texto(lista_bdb[i][0],security_list[i])
    return new_list
