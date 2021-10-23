#To do: Substituir o "converTuple" pelo .append() se der; rebustar o programa; 

board = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]

def convertTuple(tup):
    str = ""
    for i in tup:
        str = str + i
    return str

#-----------------------------------------------------------------1.1--------------------------------------------------------------------------

def corrigir_palavra(string):

    def has_surto (string):
        if len(string)>1:
            for i in range(0,len(string)-1):
                if string[i].islower() and string[i+1].isupper():
                    if string[i] == string[i+1].lower():
                        return True,i
                elif string[i].isupper() and string[i+1].islower():
                    if string[i] == string[i+1].upper():
                        return True,i
            else:
                return False,i
        else:
            return False,1

    tuplex = string
    t = tuple(string)
    loop,i = has_surto(string)
    while(loop):
        t = tuple(tuplex)
        tuplex = t[:i] + t[i+2:]
        tuplex = convertTuple(tuplex)
        loop,i = has_surto(tuplex)
    return tuplex

#-----------------------------------------------------------------1.2--------------------------------------------------------------------------

def eh_anagrama(string1,string2):
    string1 = string1.upper()
    string2 = string2.upper()
    if(string1 == string2):
        return False
    return sorted(string1) == sorted(string2)

#-----------------------------------------------------------------1.3--------------------------------------------------------------------------

def corrigir_doc(text):
    doc = text.split(" ")
    for i in range(len(doc)):
        doc[i] = corrigir_palavra(doc[i])
    j,k= 0,0
    while j < len(doc):
        while k < len(doc):
            if eh_anagrama(doc[j],doc[k]):
                doc.remove(doc[k])
            k += 1
        k=0
        j+=1
    return doc

#-----------------------------------------------------------------2.1--------------------------------------------------------------------------

def obter_posicao (direction, position):
    
    if direction == "C":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i-1][j]!=0:
                    new_pos = board[i-1][j]
                    return new_pos
    
    elif direction == "B":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i+1][j]!=0:
                    new_pos = board[i+1][j]
                    return new_pos
    
    elif direction == "D":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i][j+1]!=0:
                    new_pos = board[i][j+1]
                    return new_pos

    elif direction == "E":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i][j-1]!=0:
                    new_pos = board[i][j-1]
                    return new_pos
    
    return position

#-----------------------------------------------------------------2.2--------------------------------------------------------------------------

def obter_digito (sequence, position):
    t_sequence = tuple(sequence)
    for i in range(len(t_sequence)):
        position = obter_posicao(t_sequence[i], position)
    return position

#-----------------------------------------------------------------2.3--------------------------------------------------------------------------

def obter_pin(sequence_list):
    pin = ()
    pin += (obter_digito(sequence_list[0],5),)
    for i in range(1,len(sequence_list)):
        pin += (obter_digito(sequence_list[i],pin[i-1]),)
    return pin

#-------------------------------------------------------------------------------3.1-----------------------------------------------------------------------------------

def eh_entrada(entry):

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

    if type(entry) == tuple and len(entry) == 3:
        cifra,control,security = entry[0], entry[1], entry[2]
        if type(cifra) == str and type(control) == str and type(security)==tuple:
            if checkCifra(cifra) and checkControl(control) and checkSecurity(security):
                return True
    return False

#-------------------------------------------------------------------------------3.2----------------------------------------------------------------------------------

def validar_cifra(cifra, control):

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

    five_letters, numbers = count_letters(cifra)
    five_letters = fiveLetters_bubbleSort(five_letters,numbers)
    string = ""
    for letter in five_letters:
        string += letter
    if string == control[1:6]:
        return True
    return False

#-------------------------------------------------------------------------------3.3----------------------------------------------------------------------------------

def filtrar_bdb(entry_list):
    not_valid = []
    if type(entry_list) != list or len(entry_list) < 1:
        raise ValueError("filtrar bdb: argumento invalido")
    for bdb in entry_list:
        if not eh_entrada(bdb):
            raise ValueError("filtrar bdb: argumento invalido")
        if not validar_cifra(bdb[0],bdb[1]):
            not_valid.append(bdb)
    return not_valid
    
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

#-------------------------------------------------------------------------------5.1----------------------------------------------------------------------------------

def eh_utilizador(entry):
    dict_keys = ["name","pass","rule"]
    rule_keys = ["vals", "char"]
    if type(entry) == dict:
        for key in dict_keys:
            if not key in entry:
                return False
        if type(entry["name"]) == str and type(entry["pass"]) == str and type(entry["rule"]) == dict:
            for key_rule in rule_keys:
                if not key_rule in entry["rule"]:
                    return False
                if type(entry["rule"]["vals"]) == tuple and type(entry["rule"]["char"] == str):
                    if len(entry["rule"]["vals"]) != 2 or len(entry["rule"]["char"])!=1 or entry["rule"]["vals"][0] > entry["rule"]["vals"][1] :
                        return False
                    return True
        return False
    return False

#-------------------------------------------------------------------------------5.2----------------------------------------------------------------------------------

def eh_senha_valida(password,entry):
    # regra individual
    if not entry["vals"][0] < password.count(entry["char"]) < entry["vals"][1]:
        return False
    #regras gerais
    repeated_letter_flag = 0
    vowel_count = password.count("a") + password.count("e") + password.count("i") + password.count("o") + password.count("u")
    for letter in password:
        if password.count(letter) >= 2:
            repeated_letter_flag = 1
    if vowel_count < 3 or repeated_letter_flag == 0:
        return False
    return True

#-------------------------------------------------------------------------------5.3----------------------------------------------------------------------------------

def filtrar_senhas(entry):
    wrong_password = []
    if type(entry) != list or len(entry) < 1:
        raise ValueError("filtrar senhas:argumento invalido")
    for dictionary in entry:
        if not eh_utilizador(dictionary):
            raise ValueError("filtrar senhas:argumento invalido")
        if not eh_senha_valida(dictionary["pass"],dictionary["rule"]):
            wrong_password.append(dictionary["name"])
    return sorted(wrong_password)
