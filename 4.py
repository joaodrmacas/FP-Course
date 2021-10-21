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


def somar_casas(letra,casas_a_andar):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    casa_letra = abc.index(letra)
    casa_letra += casas_a_andar
    if(casa_letra) > 25:
        casa_letra -= 26
    return abc[casa_letra]

def decifrar_texto(cifra,security):
    casas = (security/26)
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
    return str(cifra)

print(decifrar_texto('qgfo-qutdo-s-egoes-wzegsnfmjqz', 325))