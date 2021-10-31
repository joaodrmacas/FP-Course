#TAD posicao - Ultima funcao n funciona
#Construtor

def cria_posicao(x,y):
    if type(x) == int or type(y) == int:
        if x>=0 and y>=0:
            return [x,y]
    raise ValueError("cria_posicao: argumentos invalidos")

def cria_copia_posicao(p):
    return p.copy()

#Seletor

def obter_pos_x(p):
    return p[0]
def obter_pos_y(p):
    return p[1]

#Reconhecedor

def eh_posicao(arg):
    return type(arg) == list and len(arg) == 2 and arg[0]>=0 and arg[1]>= 0

#Teste

def posicoes_iguais(p1,p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#Transformador

def posicao_para_str(p):
    return "(" + str(obter_pos_x(p)) + "," + str(obter_pos_y(p)) + ")"

#Funcoes alto nivel

def obter_posicoes_adjacentes(p):
    tup = ()
    x,y = obter_pos_x(p), obter_pos_y(p)
    C,D,B,E = [x,y-1],[x+1,y],[x,y+1],[x-1,y]
    if eh_posicao(C):
        tup += (cria_posicao(x,y-1),)
    if eh_posicao(D):
        tup += (cria_posicao(x+1,y),)
    if eh_posicao(B):
        tup += (cria_posicao(x,y+1),)
    if eh_posicao(E):
        tup += (cria_posicao(x-1,y),)
    return tup
    
def ordenar_posicoes(t):
    lista = list(t)
    for i in range(len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if lista[j][1] > lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    for i in range(len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if lista[j][1]==lista[j+1][1] and lista[j][0]>lista[j+1][0]:
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return tuple(lista)

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
    return a

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
        return a["fome"] >= a["alimentacao"]
    return False

def reproduz_animal(a):
    novo = cria_copia_animal(a)
    novo = reset_idade(novo)
    novo = reset_fome(novo)
    a = reset_idade(a)
    return novo

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

def obter_posicao_animais(m): #ordem de leitura do prado
    return ordenar_posicoes(m["pos_anim"])

def obter_animal(m,p):
    index = m["pos_anim"].index(p)
    return m["animais"][index]

#Modificadores

def eliminar_animal(m,p): #(not working?)
    tup_pos = ()
    tup_anim = ()
    animal = obter_animal(m,p)
    for pos in m["pos_anim"]:
        if pos != p:
            tup_pos += (pos,)
    for animais in m["animais"]:
        if animais != animal:
            tup_anim += (animais,)
    m["pos_anim"] = tup_pos
    m["animais"] = tup_anim
    return m
        
def mover_animal(m,p1,p2):
    tup = ()
    for i in range(len(m["pos_anim"])):
        if m["pos_anim"][i] != p1:
            tup += (m["pos_anim"][i],)
        else:
            tup += (p2,)
    m["pos_anim"] = tup
    return m

def inserir_animal(m,a,p):
    m["animais"] += (a,)
    m["pos_anim"] += (p,)
    return m

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
        for i in range(obter_tamanho_x(m)):
            if p == cria_posicao(i,0):
                return True
            if p == cria_posicao(i,obter_tamanho_y(m)-1):
                return True
        for j in range(obter_tamanho_y(m)):
            if p == cria_posicao(0,j):
                return True
            if p == cria_posicao(obter_tamanho_x(m)-1,j):
                return True
        return False

    if eh_montanha(m,p):
        return True
    for pos in m["rochedos"]:
        if pos == p:
            return True
    return False

def eh_posicao_livre(m,p):
    if not eh_posicao_animal(m,p) and not eh_posicao_obstaculo(m,p):
        return True
    return False

def prados_iguais(p1,p2):
    return eh_prado(p1) and eh_prado(p2) and p1 == p2

def prado_para_str(m):
    str = ""
    for j in range(obter_tamanho_y(m)):
        for i in range(obter_tamanho_x(m)):
            coord = cria_posicao(i,j)
            if eh_posicao_animal(m,coord):
                animal = obter_animal(m,coord)
                str += animal_para_char(animal)
            elif eh_posicao_obstaculo(m,coord):
                if (coord[0]==0 and coord[1]==0) or (coord[0]==obter_tamanho_x(m)-1\
                    and coord[1]==0) or (coord[0]==obter_tamanho_x(m)-1 and\
                        coord[1]==obter_tamanho_y(m)-1) or (coord[0]==0 and\
                            coord[1]==obter_tamanho_y(m)-1):
                            str += "+"
                elif coord[0]==0 or coord[0]==obter_tamanho_x(m)-1:
                    str +="|"
                elif coord[1]==0 or coord[1]==obter_tamanho_y(m)-1:
                    str +="-"
                else:
                    str +="@"
            elif eh_posicao_livre(m,coord):
                str +="."
        str += "\n" #talvez tenha de tirar caso o mooshak tripe com o \n depois do tabuleiro
    return str

#funcoes de alto nivel

def obter_valor_numerico(m,p):
    l,c = obter_pos_y(p),obter_pos_x(p)
    Ncol = obter_tamanho_x(m)
    return l*Ncol + c

def obter_movimento(m,p):

    def remover_adj_ocupados(m,p):
        tup = ()
        adjacentes = obter_posicoes_adjacentes(p)
        for pos in adjacentes:
            if eh_posicao_livre(m,pos):
                tup += (pos,)
        return tup

    esp_possiveis = 0
    animal = obter_animal(m,p)
    adjacentes = remover_adj_ocupados(m,p)
    if eh_presa(animal):
        for i in range(len(adjacentes)):
            if eh_posicao_livre(m,adjacentes[i]):
                esp_possiveis+=1
        if esp_possiveis != 0:
            N = obter_valor_numerico(m,p)
            return adjacentes[N%esp_possiveis]
        return p
    if eh_predador(animal):
        for j in range(len(adjacentes)):
            if eh_posicao_animal(m,adjacentes[j]):
                a = obter_animal(m,adjacentes[j])
                if eh_presa(a):
                    return adjacentes[j]
        for k in range(len(adjacentes)):
            if eh_posicao_livre(m,adjacentes[k]):
                esp_possiveis+=1
        if esp_possiveis!=0:
            N=obter_valor_numerico(m,p)
            return adjacentes[N%esp_possiveis]
        return p

def geracao(m):
    pos = obter_posicao_animais(m)
    for i in range(len(pos)):
        animal = obter_animal(m,pos[i])
        animal = aumenta_idade(animal)
        animal = aumenta_fome(animal)
        if eh_animal_faminto(animal):
            m = eliminar_animal(m,pos[i])
        else:
            m = mover_animal(m,pos[i],obter_movimento(m,pos[i]))
            if eh_animal_fertil(animal): #condicao para caso nao se mexa nao se reproduza
                bebe = reproduz_animal(animal)
                m = inserir_animal(m,bebe,pos[i])
    return m

dim = cria_posicao(11, 4)
obs = (cria_posicao(4,2), cria_posicao(5,2))
an1 = tuple(cria_animal("sheep", 2, 0) for i in range(3))
an2 = (cria_animal("wolf", 10, 3),)
pos = tuple(cria_posicao(p[0],p[1]) \
for p in ((2,2),(4,3),(10,2),(3,2)))
prado = cria_prado(dim, obs, an1+an2, pos)
print(prado_para_str(prado))
print(prado_para_str(geracao(prado)))
print(prado_para_str(geracao(prado)))
print(prado_para_str(geracao(prado)))