from Projects.SecondProj.TAD_Animal import animal_para_char, eh_animal, eh_predador, eh_presa
from Projects.SecondProj.TAD_position import cria_posicao, eh_posicao, obter_pos_x, obter_pos_y

def cria_prado(d,r,a,p):
    if type(d) == list and eh_posicao(d) and type(r) == tuple and type(a) == tuple\
        and len(a) >= 1 and type(p) == tuple and len(p) == len(a):
        for posicoes in r:
            if not eh_posicao(posicoes):
                raise ValueError("cria_prado: argumentos invalidos")
        for animais in a:
            if not eh_animal(animais):
                raise ValueError("cria_prado: argumentos invalidos")
        for posicoes in p:
            if not eh_posicao(posicoes):
                raise ValueError("cria_prado: argumentos invalidos")
        return {"pos":d, "rochedos":r, "animais":a,"pos_anim":p}
    raise ValueError("cria_prado: argumentos invalidos")

def cria_copia_prado(m):
    return m.copy()

#Seletores

def obter_tamanho_x(m):
    return obter_pos_x(m["pos"]) + 1

def obter_tamanho_y(m):
    return obter_pos_y(m["pos"]) + 1

def obter_numero_predadores(m):
    num = 0
    for animais in m["animais"]:
        if eh_predador(animais):
            num += 1
    return num

def obter_numero_presas(m):
    num = 0
    for animais in m["animais"]:
        if eh_presa(animais):
            num += 1
    return num

def obter_posicao_animais(m): #ordem de leitura do prado ? temos de criar pos?
    tup = ()
    for pos in m["pos_anim"]:
        tup += pos
    return tup

def obter_animal(m,p):
    for pos in m["pos_anim"]:
        index = pos.index(p)
        return m["animais"][index]

#Reconhecedores

def eh_prado(arg): #preciso checkar se os tuplos sao inteiros/listas? 
    if type(arg) == dict:
        if "pos" in arg and "rochedos" in arg and "animais" in arg and "pos_anim"\
            in arg:
            if type(arg["pos"]) == list and type(arg["rochedos"]) == tuple and\
                type(arg["animais"] == tuple) and type(arg["pos_anim"]) == tuple:
                return True
    return False

def eh_posicao_animal(m,p):
    for pos in m["pos_anim"]:
        if pos == p:
            return True
    return False

def eh_posicao_obstaculo(m,p):

    def eh_montanha(m,p):
        for i in range(0,obter_tamanho_x(m)):
            if p == cria_posicao(i,0):
                return True
            if p == cria_posicao(i,obter_tamanho_y(m)):
                return True
        for j in range(0, obter_tamanho_y(m)):
            if p == cria_posicao(0,j):
                return True
            if p == cria_posicao(obter_tamanho_x(m),j):
                return True
        return False

    if eh_montanha(m,p):
        return True
    for pos in m["rochedos"]:
        if pos == p:
            return True
    return False

def eh_posicao_livre(m,p):
    if not eh_posicao_animal(m,p) or not eh_posicao_obstaculo(m,p):
        return True
    return False

def prados_iguais(p1,p2):
    return eh_prado(p1) and eh_prado(p2) and p1 == p2

def prado_para_str(m):
    for i in range(obter_tamanho_x):
        for j in range(obter_tamanho_y):
            coord = cria_posicao(i,j)
            if eh_posicao_livre(m,coord):
                print(".")
            elif eh_posicao_obstaculo(m,coord):
                print("-")
            elif eh_posicao_animal(m,coord):
                print("a")
    return
