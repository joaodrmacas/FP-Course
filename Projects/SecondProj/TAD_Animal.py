def cria_animal(spec,rep,ali):
    if type(spec) == str and type(rep) == int and type(ali) == int:
        if len(spec)>0 and rep>0 and ali>=0:
            if ali>0:
                return {"especie":spec,"idade":0,"reproducao":rep,\
                    "alimentacao":ali,"tipo":"predador","fome":0}
            else:
                return {"especie":spec,"idade":0,"reproducao":rep,\
                    "alimentacao":ali,"tipo":"presa","fome":0}
    raise ValueError("cria_animal: argumentos invalidos")

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

def animal_para_char(a):
    if eh_presa(a):
        return a["especie"][0].lower()
    if eh_predador(a):
        return a["especie"][0].upper()

#Funcoes de alto nivel

def eh_animal_fertil(a):
    return a["idade"] == a["reproducao"]

def eh_animal_faminto(a):
    if eh_predador(a):
        return a["fome"] >= a["alimentação"]
    return False

def reproduz_animal(a):
    novo = cria_copia_animal(a)
    reset_idade(novo)
    reset_fome(novo)
    reset_idade(a)
    return novo

