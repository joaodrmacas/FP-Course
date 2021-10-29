def cria_animal(spec,rep,ali):
    if type(spec) == str and type(rep) == int and type(ali) == int:
        if len(spec)>0 and rep>0 and ali>=0:
            if ali>0:
                return {"especie":spec,"idade":0,"reproducao":rep,\
                    "alimentacao":ali,"tipo":"predador","fome":0}
            else:
                return {"especie":spec,"idade":0,"reproducao":rep,\
                    "alimentacao":ali,"tipo":"presa","fome":0}

def cria_copia_animal(a):
    return a.copy()

#Seletores

def obter_especie(a):
    return a["especie"]
def obter_freq_reproducao(a):
    return a["reproducao"]
def obter_freq_alimentacao(a):
    return a["alimentacao"]
def obter_idade(a):
    return a["idade"]
def obter_fome(a):
    return a["fome"]

#Modificadores

def aumenta_idade(a):
    a["idade"]+=1
    return a

def reset_idade(a):
    a["idade"]=0

def aumenta_fome(a):
    if a["tipo"] == "predador":
        a["fome"]+=1
    return a

def reset_fome(a):
    if a["tipo"] == "predador":
        a["fome"] = 0
    return a

#Reconhecedor

def eh_animal(arg):
    if type(arg) == dict:
        if "especie" in arg and "idade" in arg and "reproducao" in arg and \
            "alimentacao" in arg and "tipo" in arg and "fome" in arg and\
                len(arg) == 6:
                if type(arg["especie"]) == str and type(arg["idade"])==int and\
                    type(arg["reproducao"]) == int and type(arg["alimentacao"])\
                        ==int and type(arg["tipo"])==str and type(arg["fome"])==int:
                            return True
    return False

def eh_predador(arg):
    return arg["tipo"]=="predador"

def eh_presa(arg):
    return arg["tipo"]=="presa"

#Teste

def animais_iguais(a1,a2):
    return eh_animal(a1) and eh_animal(a2) and a1 == a2

#Transformadores

def animal_para_str(a):
    if eh_presa(a):
        return str(a["especie"]) + " [" + str(a["idade"]) + "/" + \
            str(a["reproducao"]) + "]"
    elif eh_predador(a):
        return str(a["especie"] + " [" + str(a["idade"]) + "/" + \
            str(a["reproducao"]) + ";" + str(a["fome"]) + "/" +\
                str(a["alimentacao"]) + "]")

cria_animal("rabbit", -5, 0)
r1 = cria_animal("rabbit", 5, 0)
f1 = cria_animal("fox", 20, 10)
f2 = cria_copia_animal(f1)
f2 = aumenta_idade(aumenta_idade(f2))
f2 = aumenta_fome(f2)
print(animal_para_str(f1))
print(animal_para_str(f2))
print(animais_iguais(f1,f2))
