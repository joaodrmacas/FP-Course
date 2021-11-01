#TAD POSICAO
#Construtores
def cria_posicao(x,y):
    if type(x) == int or type(y) == int:
        if x>=0 and y>=0:
            return [x,y]
    raise ValueError("cria_posicao: argumentos invalidos")
def cria_copia_posicao(p):
    x,y = p[0],p[1]
    if type(x) == int or type(y) == int:
        if x>=0 and y>=0:
            return p.copy()
    raise ValueError("cria_copia_posicao: argumentos invalidos")

#Seletores
def obter_pos_x(p):
    return p[0]
def obter_pos_y(p):
    return p[1]

#Reconhecedores
def eh_posicao(arg):
    return type(arg) == list and len(arg)==2 and arg[0]>=0 and arg[1]>= 0

#Teste
def posicoes_iguais(p1,p2): #usar isto para quando 2 animais se comerem
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#Transformador
def posicao_para_str(p):
    return "(" + str(obter_pos_x(p)) + ", " + str(obter_pos_y(p)) + ")"

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


#TAD ANIMAIS
#Construtores
def cria_animal(s,r,a):
    if type(s) == str and type(r) == int and type(a) == int:
        if len(s)>0 and r>0 and a>=0:
            if a>0:
                return {"especie":s,"idade":0,"reproducao":r,\
                    "alimentacao":a,"tipo":"predador","fome":0,"move":False}
            else:
                return {"especie":s,"idade":0,"reproducao":r,\
                    "alimentacao":a,"tipo":"presa","fome":0,"move":False}
    raise ValueError("cria_animal: argumentos invalidos")
def cria_copia_animal(a):
    s = a["especie"]
    r = a["reproducao"]
    al = a["alimentacao"]
    if type(s) == str and type(r) == int and type(al) == int:
        if len(s)>0 and r>0 and al>=0:
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
def obter_movimento(a):
    return a["move"]

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

#Funcoes de alto nivel
def eh_animal_fertil(a):
    return obter_idade(a) == obter_freq_reproducao(a)
def eh_animal_faminto(a):
    if eh_predador(a):
        return obter_fome(a) >= obter_freq_alimentacao(a)
    return False
def reproduz_animal(a):
    novo = cria_copia_animal(a)
    novo = reset_idade(novo)
    novo = reset_fome(novo)
    a = reset_idade(a)
    return novo


#TAD PRADO
#Construtores
def cria_prado(d,r,a,p): # usar o eh_prado?
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
def cria_copia_prado(m): #verificar as condicoes
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
def obter_posicao_animais(m):
    return ordenar_posicoes(m["pos_anim"])
def obter_animal(m,p):
    index = m["pos_anim"].index(p)
    return m["animais"][index]

#Modificadores

def eliminar_animal(m,p): #talvez tenha de mudar
    tup_pos = ()
    tup_anim = ()
    i=0
    animal = obter_animal(m,p)
    for pos in m["pos_anim"]:
        if pos != p:
            tup_pos += (pos,)
        else:
            if i == 1:
                tup_pos += (pos,)
            i=1
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
def reset_moves(m):
    for animais in m["animais"]:
        animais["move"]=False

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
    return str[:-1]

#funcoes de alto nivel
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
            if eh_posicao_animal(m,adjacentes[i]) and eh_presa(obter_animal(m,adjacentes[i])):
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

#Funcoes a parte
def geracao(m):
    pos = obter_posicao_animais(m)
    for i in range(len(pos)):
        animal = obter_animal(m,pos[i])
        animal = aumenta_idade(animal)
        animal = aumenta_fome(animal)
        if eh_animal_faminto(animal):
            m = eliminar_animal(m,pos[i])
        else:
            novo_pos = obter_movimento(m,pos[i])
            if novo_pos != pos[i]:
                m = mover_animal(m,pos[i],novo_pos)
                if eh_animal_fertil(animal): #condicao para caso nao se mexa se nao se reproduzir
                    bebe = reproduz_animal(animal)
                    m = inserir_animal(m,bebe,pos[i])
            else:
                if eh_animal_fertil(animal):
                    animal = diminui_idade(animal)
    pos = obter_posicao_animais(m) #problema: como interage com os movimentos antigos, varios animais tao a ir para o mesmo sitio portanto, temos de criar um valor no dicionario dos animais de true or false para registar se ja fez o movimento
    j,k = 0,0
    while j<len(pos):
        k=0
        while k<len(pos):
            if k!=j:
                if posicoes_iguais(pos[j],pos[k]):
                    if(eh_presa(obter_animal(m,pos[k]))):
                        m = eliminar_animal(m,pos[k])
                        animal = obter_animal(m,pos[k])
                        if eh_predador(animal):
                            animal = reset_fome(animal)
            k += 1
        j += 1
    return m
def simula_ecossistema(f,g,v):
    
    def ler_ficheiro(f,g,v):
        file = open(f,"r")
        nome = []
        pos = []
        p = []
        rochedo = []
        size = file.readline()
        size = size[1:-2].split(", ")
        size = [int(size[0]),int(size[1])]
        rochedos = file.readline()
        rochedos = rochedos[1:-2].split(", ")
        for i in range(0,len(rochedos),2):
            rochedo += [[int(rochedos[i][1:]),int(rochedos[i+1][:-1])],]
        animais = file.readlines()
        for j in range(len(animais)):
            if j != len(animais)-1:
                animais[j] = animais[j][1:-2]
            else:
                animais[j] = animais[j][1:-1]
            nome += [animais[j].split(", ")[:3]]
            pos += [animais[j].split(", ")[3:]]
        for i in range(len(nome)):
            nome[i][0] = (nome[i][0].replace('"',''))
            nome[i][1],nome[i][2] = int(nome[i][1]),int(nome[i][2])
        for coord in pos:
            coord[0] = int(coord[0].replace("(",""))
            coord[1] = int(coord[1].replace(")",""))
        file.close()
        return size,rochedo,nome,tuple(pos)
    
    def prints(f,g,v,prado):
        pra = prado
        if v:
            for i in range(g):
                if i != 0:
                    pra = geracao(pra)
                    if num_presas != obter_numero_presas(pra) or num_predadores != \
                        obter_numero_predadores(pra):
                        print("Predadores: " + str(obter_numero_predadores(pra)) + " vs Presas: "\
                            + str(obter_numero_presas(pra))+ " (Gen. "+ str(i) +")")
                        print(prado_para_str(pra))
                else:
                    print("Predadores: " + str(obter_numero_predadores(pra)) + " vs Presas: "\
                            + str(obter_numero_presas(pra))+ " (Gen. "+ str(i) +")")
                    print(prado_para_str(pra))
                num_presas = obter_numero_presas(pra)
                num_predadores = obter_numero_predadores(pra)
        else:
            for i in range(g):
                if i==0:
                    print("Predadores: " + str(obter_numero_predadores(pra)) + " vs Presas: "\
                            + str(obter_numero_presas(pra))+ " (Gen. "+ str(i) +")")
                    print(prado_para_str(pra))
                elif i==g-1:
                    print("Predadores: " + str(obter_numero_predadores(pra)) + " vs Presas: "\
                            + str(obter_numero_presas(pra))+ " (Gen. "+ str(g) +")")
                    print(prado_para_str(pra))
                else:
                    pra = geracao(pra)
        return (obter_numero_predadores(pra),obter_numero_presas(pra))
    
    size,rochedos,nome,pos = ler_ficheiro(f,g,v)
    dim = cria_posicao(size[0],size[1])
    obs = ()
    po = ()
    animal = ()
    for coord in rochedos:
        obs += (cria_posicao(coord[0],coord[1]),)
    for a in nome:
        animal += (cria_animal(a[0],a[1],a[2]),)
    for coord in pos:
        po += (cria_posicao(coord[0],coord[1]),)
    prado = cria_prado(dim,obs,animal,po)
    num_presas_predadores = prints(f,g,v,prado)

    return num_presas_predadores

print(simula_ecossistema("config.txt",20,True))