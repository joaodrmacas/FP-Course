#-----------------------------------------------------------------1.1--------------------------------------------------------------------------

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

def convertTuple(tup):
    str = ""
    for i in tup:
        str = str + i
    return str

def corrigir_palavra(string):
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


print(corrigir_doc("BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga \
eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn \
LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza data tada"))
