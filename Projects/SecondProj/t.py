#TAD POSICAO
#Construtores
def cria_posicao(x,y):
    if not eh_posicao([x,y]):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [x,y]
def cria_copia_posicao(p):
    if eh_posicao(p):
        return p.copy()
    raise ValueError("cria_copia_posicao: argumentos invalidos")

#Seletores
def obter_pos_x(p):
    return p[0]
def obter_pos_y(p):
    return p[1]

#Reconhecedores
def eh_posicao(arg):
    return type(arg) == list and len(arg)==2 and type(arg[0])==int and \
        type(arg[1])==int and arg[0]>=0 and arg[1]>= 0
def eh_positivo(a1,a2):
    return a1>=0 and a2>=0
#Teste
def posicoes_iguais(p1,p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#Transformador
def posicao_para_str(p):
    return "(" + str(obter_pos_x(p)) + ", " + str(obter_pos_y(p)) + ")"

#Funcoes de alto nivel
def obter_posicoes_adjacentes(p):
    tup = ()
    x,y = obter_pos_x(p), obter_pos_y(p)
    if eh_positivo(x,y-1):
        if eh_posicao(cria_posicao(x,y-1)):
            tup += (cria_posicao(x,y-1),)
    if eh_positivo(x+1,y):
        if eh_posicao(cria_posicao(x+1,y)):
            tup += (cria_posicao(x+1,y),)
    if eh_positivo(x,y+1):
        if eh_posicao(cria_posicao(x,y+1)):
            tup += (cria_posicao(x,y+1),)
    if eh_positivo(x-1,y):
        if eh_posicao(cria_posicao(x-1,y)):
            tup += (cria_posicao(x-1,y),)
    return tup
def ordenar_posicoes(t):
    lista = list(t)
    for i in range(len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if obter_pos_y(lista[j]) > obter_pos_y(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1],lista[j]
    for i in range(len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if obter_pos_y(lista[j])==obter_pos_y(lista[j+1]) and\
                obter_pos_x(lista[j])>obter_pos_x(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1],lista[j]
    return tuple(lista)

#TAD ANIMAL
#Construtores
def cria_animal(s,r,a):
    if type(a) == int:
        if a>0:
            animal = {"especie":s,"idade":0,"reproducao":r,\
                "alimentacao":a,"tipo":"predador","fome":0,"move":False,\
                    "del":False}
        else:
            animal = {"especie":s,"idade":0,"reproducao":r,\
                "alimentacao":a,"tipo":"presa","fome":0,"move":False,\
                    "del":False}
        if eh_animal(animal):
            return animal
    raise ValueError("cria_animal: argumentos invalidos")
def cria_copia_animal(a):
    if eh_animal(a):
        return a.copy()
    raise ValueError("cria_copia_animal: argumentos invalidos")

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
def diminui_idade(a):
    a["idade"]-=1
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
def move(a):
    a["move"] = True
    return a
def eliminar(a):
    a["del"] = True
    return a
def nao_eliminar(a):
    a["del"] = False
    return a
def reset_move(a):
    a["move"]=False
    return a

#Reconhecedores
def eh_animal(arg):
    if type(arg) == dict and len(arg) == 8:
        if type(arg["especie"]) == str and type(arg["idade"])==int and\
            type(arg["reproducao"]) == int and type(arg["alimentacao"])\
                ==int and type(arg["tipo"])==str and \
                    type(arg["fome"])==int and type(arg["move"])==bool\
                        and type(arg["del"]) == bool and len(arg\
                            ["especie"]) > 0 and arg["reproducao"]\
                                >0 and arg["alimentacao"]>=0:
                    return True
    return False
def eh_predador(arg):
    if eh_animal(arg) and arg["tipo"]=="predador":
        return True
    return False
def eh_presa(arg):
    if eh_animal(arg) and arg["tipo"]=="presa":
        return True
    return False
def ja_moveu(arg):
    return arg["move"]
def eh_eliminado(arg):
    return arg["del"]

#Teste
def animais_iguais(a1,a2):
    return eh_animal(a1) and eh_animal(a2) and a1 == a2

#Transformadores
def animal_para_char(a):
    if eh_presa(a):
        return a["especie"][0].lower()
    if eh_predador(a):
        return a["especie"][0].upper()
def animal_para_str(a):
    if eh_presa(a):
        return str(obter_especie(a)) + " [" + str(obter_idade(a)) + "/" + \
            str(obter_freq_reproducao(a)) + "]"
    elif eh_predador(a):
        return str(obter_especie(a)) + " [" + str(obter_idade(a)) + "/" + \
            str(obter_freq_reproducao(a)) + ";" + str(obter_fome(a)) + "/" +\
                str(obter_freq_alimentacao(a)) + "]"

#Alto Nivel
def eh_animal_fertil(a):
    return obter_idade(a) == obter_freq_reproducao(a)
def eh_animal_faminto(a):
    if eh_predador(a):
        return obter_fome(a) >= obter_freq_alimentacao(a)
    return False
def reproduz_animal(a):
    novo = cria_copia_animal(a) #Pode estar a gerar runtime no TAD animal
    novo = reset_idade(novo)
    novo = nao_eliminar(novo)
    novo = reset_fome(novo)
    a = reset_idade(a)
    return novo

#TAD PRADO
#Construtores
def cria_prado(d,r,a,p):
    prado = [d,r,a,p]
    if eh_prado(prado):
        return prado
    raise ValueError("cria_prado: argumentos invalidos")
def cria_copia_prado(m):
    if eh_prado(m):
        return m.copy()
    raise ValueError("cria_copia_prado: argumentos invalidos")

#Seletores
def ver_index(m,p):
    for i in range(len(m[3])):
        if m[3][i]==p:
            return i
def obter_tamanho_x(m):
    return obter_pos_x(m[0])+1
def obter_tamanho_y(m):
    return obter_pos_y(m[0])+1
def obter_numero_predadores(m):
    n = 0
    for animais in m[2]:
        if eh_predador(animais):
            n += 1
    return n
def obter_numero_predadores(m):
    n = 0
    for animais in m[2]:
        if eh_presa(animais):
            n += 1
    return n
def obter_posicao_animais(m):
    return ordenar_posicoes(m[3])
def obter_animal(m,p):
    index = ver_index(m,p)
    return m[2][index]

#Modificadores
def eliminar_animal(m,p):
    tup_anim = ()
    tup_pos = ()
    for i in range(len(m[3])):
        if m[3][i] != p:
            tup_pos += (m[3][i],)
        else:
            index=ver_index(m,p)
    for j in range(len(m[2])):
        if not eh_eliminado(m[2][j]) and j!=index:
            tup_anim += (m[2][j],)
    m[3] = tup_pos
    m[2] = tup_anim
    return m
def mover_animal(m,p1,p2):
    tup = ()
    for pos in m[3]:
        if pos != p1:
            tup += (pos,)
        else:
            tup += (p2,)
    m[3] = tup
    return m
def inserir_animal(m,a,p):
    m[2] += (a,)
    m[3] += (p,)
    return m
def reset_moves(m):
    for animais in m[2]:
        animais = reset_move(animais)
    return m

#Reconhecedores
def eh_prado(arg):
    if type(arg)==list and len(arg)==4 and eh_posicao(arg[0]) and type\
        (arg[1])==tuple and len(arg[1])>=0 and type(arg\
            [2])==tuple and len(arg[2])>=1 and type(arg\
                [3])==tuple and len(arg[3])==len(arg\
                    [2]):
                for posicoes in arg[1]:
                    if not eh_posicao(posicoes):
                        return False
                    if obter_pos_x(posicoes)>=obter_pos_x(arg[0]) or \
                        obter_pos_y(posicoes)>=obter_pos_y(arg[0]):
                        return False
                for animal in arg[2]:
                    if not eh_animal(animal):
                        return False
                for posicao in arg[3]:
                    if not eh_posicao(posicao):
                        return False
                    if obter_pos_x(posicao)>=obter_pos_x(arg[0]) or \
                        obter_pos_y(posicao)>=obter_pos_y(arg[0]):
                        return False
                return True
    return False
def eh_posicao_animal(m,p):
    for pos in m[3]:
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
    for pos in m[1]:
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
                if (obter_pos_x(coord)==0 and obter_pos_y(coord)==0) or (obter_pos_x(coord)==\
                    obter_tamanho_x(m)-1 and obter_pos_y(coord)==0) or (obter_pos_x(coord)==\
                        obter_tamanho_x(m)-1 and obter_pos_y(coord)==\
                            obter_tamanho_y(m)-1) or (obter_pos_x(coord)==0 and obter_pos_y(coord)\
                                ==obter_tamanho_y(m)-1):
                            str += "+"
                elif obter_pos_x(coord)==0 or obter_pos_x(coord)==obter_tamanho_x(m)-1:
                    str +="|"
                elif obter_pos_y(coord)==0 or obter_pos_y(coord)==obter_tamanho_y(m)-1:
                    str +="-"
                else:
                    str +="@"
            elif eh_posicao_livre(m,coord):
                str +="."
        str += "\n"
    return str[:-1]

def obter_valor_numerico(m,p):
    l,c = obter_pos_y(p),obter_pos_x(p)
    Ncol = obter_tamanho_x(m)
    return l*Ncol + c
def obter_movimento(m,p):
    adjacentes = obter_posicoes_adjacentes(p)
    animal = obter_animal(m,p)
    posicoes_presas,adjacentes_livres = (),()
    N = obter_valor_numerico(m,p)
    if eh_predador(animal):
        for i in range(len(adjacentes)):
            if eh_posicao_animal(m,adjacentes[i]) and \
                eh_presa(obter_animal(m,adjacentes[i])):
                posicoes_presas += (adjacentes[i],)
        for j in range(len(adjacentes)):
            if eh_posicao_livre(m,adjacentes[j]):
                adjacentes_livres += (adjacentes[j],)
        if len(posicoes_presas)>0:
            return posicoes_presas[N%len(posicoes_presas)]
        if len(adjacentes_livres)>0:
            return adjacentes_livres[N%len(adjacentes_livres)]
    elif eh_presa(animal):
        for k in range(len(adjacentes)):
            if eh_posicao_livre(m,adjacentes[k]):
                adjacentes_livres += (adjacentes[k],)
        if len(adjacentes_livres)>0:
            return adjacentes_livres[N%len(adjacentes_livres)]
    return p

dim = cria_posicao(11, 4)
obs = (cria_posicao(4,2), cria_posicao(5,2))
an1 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an2 = (cria_animal('lynx', 20, 15),)
pos = tuple(cria_posicao(p[0],p[1]) \
for p in ((5,1),(7,2),(10,1),(6,1)))
prado = cria_prado(dim, obs, an1+an2, pos)
print(obter_tamanho_x(prado), obter_tamanho_y(prado))
print(prado_para_str(prado))
p1 = cria_posicao(7,2)
p2 = cria_posicao(9,3)
prado = mover_animal(prado, p1, p2)
print(prado_para_str(prado))
print(obter_valor_numerico(prado, cria_posicao(9,3)))
print(posicao_para_str(obter_movimento(prado, cria_posicao(5,1))))
print(posicao_para_str(obter_movimento(prado, cria_posicao(6,1))))
print(posicao_para_str(obter_movimento(prado, cria_posicao(10,1))))