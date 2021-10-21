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

