#-------------------------------------------------------------------------------3.1-----------------------------------------------------------------------------------

def checkCifra(cifra):
    cifra_array = cifra.split("-")
    for j in range(len(cifra_array)):
        for i in range(len(cifra_array[j])):
            if not cifra_array[j][i].isalpha():
                return False
        if len(cifra_array[j]) < 1 and not cifra_array[j].islower():
            return False
    return True

def checkControl(control):
    if control[0] == "[" and control[-1] == "]" and len(control) == 7:
        for i in range(1,6):
            if not control[i].isalpha():
                return False
        if control.islower():
            return True
    return False

def checkSecurity(security):
    for i in range(len(security)):
        if not isinstance(security[i], int):
            return False
        if security[i] <= 0:
            return False
    if len(security) >= 2:
        return True
    return False

def eh_entrada(entry):
    if type(entry) == tuple and len(entry) == 3:
        cifra,control,security = entry[0], entry[1], entry[2]
        if type(cifra) == str and type(control) == str and type(security)==tuple:
            if checkCifra(cifra) and checkControl(control) and checkSecurity(security):
                return True
    return False

#-------------------------------------------------------------------------------3.2----------------------------------------------------------------------------------

def count_letters(word): #count how many letters a word has
    delete = 0
    letter_list = list(dict.fromkeys(word))
    letter_number = list(range(0,len(letter_list)))
    if "-" in word:
        delete = letter_list.index("-")
        del letter_list[delete]
        del letter_number[delete]
    for i in range(len(letter_list)):
        letter_number[i] = word.count(letter_list[i])
    
    return letter_list, letter_number

def fiveLetters_bubbleSort(letter_list,number_list): #sorts the 5 most repeated letters and in case of tie, sorts alphabetically
    leng = len(number_list)
    for i in range(leng-1):
        for j in range(leng-i-1):
            if number_list[j] < number_list[j+1] or (number_list[j] == number_list[j+1] and letter_list[j] > letter_list[j+1]):
                number_list[j],number_list[j+1] = number_list[j+1],number_list[j]
                letter_list[j],letter_list[j+1] = letter_list[j+1],letter_list[j]
                
    return letter_list[:5]

def validar_cifra(cifra, control):
    five_letters, numbers = count_letters(cifra)
    five_letters = fiveLetters_bubbleSort(five_letters,numbers)
    string = ""
    for letter in five_letters:
        string += letter
    if string == control[1:6]:
        return True
    return False

#-------------------------------------------------------------------------------3.3----------------------------------------------------------------------------------

def filtrar_bdb(entry_list): #devia retornar uma lista de tuplos
    not_valid = []
    if type(entry_list) != list or len(entry_list) < 1:
        raise ValueError("filtrar bdb: argumento invalido")
    for bdb in entry_list:
        if not eh_entrada(bdb): #e suposto verificar se a lista tem entradas corretaas?
            raise ValueError("filtrar bdb: argumento invalido")
        if not validar_cifra(bdb[0],bdb[1]):
            not_valid += bdb
    return not_valid

# bdb = [("aaaaa-bbb-zx-yz-xy", "[abxyz]", (950,300)),
# ("a-b-c-d-e-f-g-h", "[abcde]", (124,325,7)),
# ("entrada-muito-errada", "[abcde]", (50,404)),
# ("eu-sou-muito-gay", "[asdef]",(50,44))]

# print(filtrar_bdb(bdb))

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

def somar_casas(letra,casas_a_andar):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    casa_letra = abc.index(letra)
    casa_letra += casas_a_andar
    if(casa_letra) > 25:
        casa_letra -= 26
    return abc[casa_letra]

def decifrar_texto(cifra,security):
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

bdb = [('qgfo-qutdo-s-egoes-wzegsnfmjqz', '[abcde]', (2223,424,1316,99)), ('lctlgukvzwy-ji-xxwmzgugkgw', '[abxyz]', (2388, 367, 5999)), ('nyccjoj-vfrex-ncalml', '[xxxxx]', (50, 404))]
print(decifrar_bdb(bdb))