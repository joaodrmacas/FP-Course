# -------------------------------------------------------------------
# "Buggy Data Base" : Primeiro Projeto de "Fundamentos de Programação" 25/10
#
#  
# Made by: João Maçãs 99970 Leic-A -> joaomacas02@tecnico.ulisboa.pt
# -------------------------------------------------------------------

#Tabuleiro utilizado para a resolução do capitulo 2 do enunciado
board = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]

def convertTupleList(tup):
    # -------------------------------------------   
    #    converTupleList: Converte uma Lista/Tuplo para string
    #
    #   Parameters:
    #       tup: Tuple/List
    #   Return:
    #       str:String final feita pelos elementos de "tup"
    # -------------------------------------------

    str = ""
    for i in tup:
        str = str + i
    return str

def corrigir_palavra(string):
    # -------------------------------------------   
    #    corrigir_palavra: dada uma palavra "string", a funcao procura por
    #   surtos e corrige-os
    #
    #   Parameters:
    #       string: Palavra potencialmente com surto
    #   Return:
    #       tuplex: string da palavra sem surtos
    # -------------------------------------------
    def has_surto (string):
        # -------------------------------------------   
        #    has_surto: Dado uma palavra, verifica se existe algum surto
        #   (ter uma letra minuscula e imediatamente a seguir a mesma letra
        #   maiuscula). Retorna o booleano e o indice da 1a letra caso tenha
        # -------------------------------------------
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
        tuplex =  convertTupleList(tuplex)
        loop,i = has_surto(tuplex)
    return tuplex

def eh_anagrama(string1,string2):
    # -------------------------------------------   
    #    eh_anagrama: Verifica se "string1" e "string2" sao anagramas.
    #   Caso sejam a mesma palavra não é considerado anagrama.
    #
    #   Parameters:
    #       string1: 1a palavra
    #       string2: 2a palavra
    #   Return:
    #       True -> Se forem anagramas
    #       False -> Se nao forem
    # -------------------------------------------
    string1 = string1.upper()
    string2 = string2.upper()
    if(string1 == string2):
        return False
    return sorted(string1) == sorted(string2)

def corrigir_doc(text):
    # -------------------------------------------   
    #    corrigir_doc: Recebe o texto com erros da documentacao da BDB 
    #   e devolve a cadeia de carateres filtrada com as palavras corrigidas
    #   e os anagramas retirados, ficando apenas a sua primeira ocorrencia.
    #
    #   Parameters:
    #       text: String com potencial erros e anagramas
    #   Return:
    #       final_doc: String com todos os erros resolvidos e anagramas
    #   retirados
    # -------------------------------------------
    def isDoubleSpace(string):
        # -------------------------------------------   
        #    isDoubleSpace: Percorre uma string e verifica se tem
        #   duplo espaco "  ".
        # -------------------------------------------
        for i in range(len(string)-1):
            if string[i] == " " and string[i+1] == " ":
                return True
        return False

    if type(text) != str or len(text) < 1 or isDoubleSpace(text):
        raise ValueError("corrigir_doc: argumento invalido")

    for letter in text:
        if letter != " ":
            if not letter.isalpha():
                raise ValueError("corrigir_doc: argumento invalido")

    final_doc = ""
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
    iteracoes = 0
    for word in doc:
        if iteracoes == 0:
            final_doc = word
        else:
            final_doc += " " + word
        iteracoes += 1
    return final_doc

def obter_posicao (direction, position):
    # -------------------------------------------   
    #    obter_posicao: Calcula a nova posicão do tabuleiro dado uma posicao
    #   inicial e uma direcao
    #
    #   Parameters:
    #       direction: Direcao do movimento
    #       position: Posicao inicial
    #   Return:
    #       new_pos: Nova posicao apos o movimento
    #       position: Caso o movimento seja invalido (fora do board), mantem
    #   posicao
    # -------------------------------------------
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

def obter_digito (sequence, position):
    # -------------------------------------------   
    #    obter_digito: Calcula a nova posicao apos uma serie de movimentos
    #
    #   Parameters:
    #       sequence: Serie de movimentos
    #       position: Posicao inicial
    #   Return:
    #       position: Posicao final
    # -------------------------------------------
    t_sequence = tuple(sequence)
    for i in range(len(t_sequence)):
        position = obter_posicao(t_sequence[i], position)
    return position

def obter_pin(sequence_list):
    # -------------------------------------------   
    #    obter_pin: Calcula o pin codificado através do tuplo
    #  "sequence_list". Valida os argumentos
    #
    #   Parameters:
    #       sequence_list: Tuplo que contem diferentes sequencias de direcoes
    #   Return:
    #       pin: Pin Final
    # -------------------------------------------
    if type(sequence_list) != tuple or not( 4 <= len(sequence_list) <= 10 ):
        raise ValueError("obter_pin: argumento invalido")
    for sequence in sequence_list:
        if not sequence.isalpha() or len(sequence) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for letter in sequence:
            if letter != "C" and letter != "B" and letter != "D" and letter != "E":
                raise ValueError("obter_pin: argumento invalido")
    pin = ()
    pin += (obter_digito(sequence_list[0],5),)
    for i in range(1,len(sequence_list)):
        pin += (obter_digito(sequence_list[i],pin[i-1]),)
    return pin

def eh_entrada(entry):
    # -------------------------------------------   
    #    eh_entrada: Verifica se o argumento "entry" corresponde a uma
    #   entrada BDB, corrupta ou não.
    #
    #   Parameters:
    #       entry: Parametro Universal
    #   Return:
    #       True -> Se a "entry" for uma entrada BDB
    #       False -> Se nao for
    # -------------------------------------------
    def checkCifra(cifra):
        # -------------------------------------------   
        #    checkCifra: Verifica se cumpre todos os requerimentos
        #   para ser uma cifra
        # -------------------------------------------
        cifra_array = cifra.split("-")
        for j in range(len(cifra_array)):
            for i in range(len(cifra_array[j])):
                if not cifra_array[j][i].isalpha():
                    return False
            if len(cifra_array[j]) < 1 or not cifra_array[j].islower():
                return False
        return True

    def checkControl(control):
        # -------------------------------------------   
        #    checkControl: Verifica se cumpre todos os requerimentos
        #   para ser uma sequencia de controlo
        # -------------------------------------------
        if len(control) != 7:
            return False
        if control[0] == "[" and control[-1] == "]":
            for i in range(1,6):
                if not control[i].isalpha():
                    return False
            if control.islower():
                return True
        return False

    def checkSecurity(security):
        # -------------------------------------------   
        #    checkSecurity: Verifica se cumpre todas os requerimentos
        #   para ser um numero de controlo
        # -------------------------------------------
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

def validar_cifra(cifra, control):
    # -------------------------------------------   
    #    validar_cifra: Verifica se a sequencia de controlo é coerente com a
    #   cifra
    #
    #   Parameters:
    #       cifra: Cifra
    #       control: Sequencia de controlo
    #   Return:
    #       True -> Se a seq. de controlo é coerente com a cifra
    #       False -> Se nao for
    # -------------------------------------------
    def count_letters(word):
        # -------------------------------------------   
        #    count_letters: Conta quantas letras unicas uma palavra tem
        # -------------------------------------------
        delete = 0
        letter_list = list(dict.fromkeys(word))
        letter_number = list(range(0,len(letter_list)))
        #Listas associadas em que a letter_list contem a letra num indiice i
        #e a letter_number contem o numero de vezes que essa letra ha numa
        #palavra no mesmo indice
        if "-" in word:
            delete = letter_list.index("-")
            del letter_list[delete]
            del letter_number[delete]
        for i in range(len(letter_list)):
            letter_number[i] = word.count(letter_list[i])
        
        return letter_list, letter_number

    def fiveLetters_bubbleSort(letter_list,number_list): 
        # -------------------------------------------   
        #    checkCifra: Cria uma lista organizado pela letra mais vezes
        #   repetida. Em caso de empate ordena alfabeticamente
        # -------------------------------------------
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

def filtrar_bdb(entry_list):
    # -------------------------------------------   
    #    filtrar_bdb: Verifica uma lista de entradas BDB, criando uma nova
    #   apenas com as entradas cujo checksum nao e coerente com a cifra.
    #   verifica parametros
    #
    #   Parameters:
    #       entry_list: Lista de supostas entradas BDB
    #   Return:
    #       not_valid: Lista de entradas nao coerentes
    # -------------------------------------------
    not_valid = []
    if type(entry_list) != list or len(entry_list) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")
    for bdb in entry_list:
        if not eh_entrada(bdb):
            raise ValueError("filtrar_bdb: argumento invalido")
        if not validar_cifra(bdb[0],bdb[1]):
            not_valid.append(bdb)
    return not_valid
    
def obter_num_seguranca(security):
    # -------------------------------------------   
    #    obter_num_seguranca: Calcula a menor diferenca positiva entre qualquer par de numeros
    #
    #   Parameters:
    #       security: Tuplo de numeros
    #   Return:
    #       lowest_dif: Retorna o numero de segurança
    # -------------------------------------------
    lowest_dif = 2**31-1
    for i in security:
        for j in security:
            dif = i-j
            if dif > 0 and dif<lowest_dif:
                lowest_dif = dif
    return lowest_dif

def decifrar_texto(cifra,security):
    # -------------------------------------------   
    #    decifrar_texto: Decifra a cifra através do algoritmo descrito no enunciado
    #
    #   Parameters:
    #       cifra: String nao decifrada 
    #       security: Numero de segurança
    #   Return:
    #       cifra: Retorna a cifra convertida de lista para string 
    # -------------------------------------------
    def somar_casas(letra,casas_a_andar):
        # -------------------------------------------   
        #    somar_casas: Dado uma letra e um numero de "casas" a avançar
        #   no alfabeto (sendo cada letra uma casa), esta função retorna a
        #   nova letra.
        # -------------------------------------------
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',\
                'z']
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
        if i%2 == 0:            #verificacao de inidice par ou impar
            casas_a_somar += 1
        else:
            casas_a_somar -= 1
        
        if cifra[i] == "-":
            cifra[i] = " "
        else:
            cifra[i] = somar_casas(cifra[i],casas_a_somar)
    return convertTupleList(cifra)

def decifrar_bdb(lista_bdb):
    # -------------------------------------------   
    #    decifrar_bdb: Cria uma lista com as entradas decifradas na mesma
    #   ordem que as recebeu. Valida os argumentos.
    #
    #   Parameters:
    #       lista_bdb: Lista de entradas BDB
    #   Return:
    #       new_list: Retorna lista com as entradas decifradas
    # -------------------------------------------
    if type(lista_bdb) != list or len(lista_bdb) < 1:
        raise ValueError("decifrar_bdb: argumento invalido")
    new_list = list(range(len(lista_bdb)))
    security_list = list(range(len(lista_bdb)))
    for i in range(len(lista_bdb)):
        if not eh_entrada(lista_bdb[i]):
            raise ValueError("decifrar_bdb: argumento invalido")
        security_list[i] = obter_num_seguranca(lista_bdb[i][2])
        new_list[i] = decifrar_texto(lista_bdb[i][0],security_list[i])
    return new_list

def eh_utilizador(universal):
    # -------------------------------------------   
    #    eh_utilizador: Verifica se um dicionario contem a informacao de 
    # utilizador relevante da BDB
    #
    #   Parameters:
    #       universal: Parametro Universal
    #   Return:
    #       True -> Se a "entry" corresponder ao dicionario com informacao
    #  correta
    #       False -> Se nao corresponder
    # -------------------------------------------
    dict_keys = ["name","pass","rule"]
    rule_keys = ["vals", "char"]
    if type(universal) == dict:
        for key in dict_keys:
            if not key in universal:#Verifica se as keys corretas estao na "entry"
                return False 
        for keys in universal:
            if not keys in dict_keys:#Verifica se nao ha keys a mais na "entry"
                return False
        if type(universal["name"]) != str or type(universal["pass"]) != str or type(universal["rule"]) != dict:
            return False
        if len(universal["name"]) < 1 or len(universal["pass"]) < 1:
            return False
        for key_rule in rule_keys:
            if not key_rule in universal["rule"]:
                return False
            if type(universal["rule"]["vals"]) == tuple and type(universal["rule"]["char"] == str):
                if len(universal["rule"]["vals"]) != 2 or len(universal["rule"]["char"])!=1 or universal["rule"]["vals"][0] > universal["rule"]["vals"][1] or universal["rule"]["vals"][0]<1:
                    return False
                return True
        return False
    return False

def eh_senha_valida(password,dic):
    # -------------------------------------------   
    #    eh_senha_valida: Verifica se senha cumpre com todas as regras de 
    # definicao (gerais e individual)
    #
    #   Parameters:
    #       password: string correspondente a pass do utilizador
    #       dic: dicionario que contem as regras individuais da pass
    #   Return:
    #       True -> Se a senha cumprir com as regras gerais e individuais
    #       False -> Se nao cumprir
    # -------------------------------------------
    # regra individual
    if not dic["vals"][0] <= password.count(dic["char"]) <= dic["vals"][1]:
        return False
    #regras gerais
    repeated_letter_flag = 0
    vowel_count = password.count("a") + password.count("e") + password.count("i") + password.count("o") + password.count("u")
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            repeated_letter_flag = 1
    if vowel_count < 3 or repeated_letter_flag == 0:
        return False
    return True

def filtrar_senhas(dic_list):
    #  --------------------------------------------
    #    filtrar_senhas: Recebe uma lista de dicionarios com as informacoes dos
    #    utilizadores cuja pass está errada. Verifica a validade do parametros
    #
    #   Parameters:
    #       dic_list: Lista de dicionarios com informacao dos utilizadores
    #   Return:
    #       wrong_password: Lista ordenada dos nomes dos utilizadores cujas
    # pass estao erradas
    # -------------------------------------------
    wrong_password = []
    if type(dic_list) != list or len(dic_list) < 1:
        raise ValueError("filtrar_senhas: argumento invalido")
    for dictionary in dic_list:
        if not eh_utilizador(dictionary):
            raise ValueError("filtrar_senhas: argumento invalido")
        if not eh_senha_valida(dictionary["pass"],dictionary["rule"]):
            wrong_password.append(dictionary["name"])
    return sorted(wrong_password)
