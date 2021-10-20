
def checkCifra(cifra):
    for i in range(len(cifra)):
        if not cifra[i].isalpha():
            return False
    if len(cifra.split("-")) >= 1 and cifra.islower():
        return True
    return False

def checkControl(control):
    if control[0] == "[" and control[-1] == "]" and len(control) == 7:
        for i in range(1,6):
            if not control[i].isalpha():
                return False
        if control.islower():
            return True
    return False

# def checkSecurity(security):
#     for i in range(len(security)):
#         if security[i].isinteger() and security[i] > 0:
#             return False
#     if len(security) >= 2:
#         return True
#     return False
    
# print(checkSecurity(("a",2,3)))

def eh_entrada(entry):
    if type(entry) == tuple and len(entry) == 3:
        cifra,control,security = entry[0], entry[1], entry[2]
        if type(cifra) == str and type(control) == str and type(security)==tuple:
            if checkCifra(cifra) and checkControl(control):
                return True
    #raise ValueError("Entry not supported.")
    return False

print(eh_entrada(("ola-a","[olaaa]",(1,2,3))))