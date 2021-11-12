#TAD POSICAO
#Construtores
def cria_posicao(x,y):
    if not eh_posicao([x,y]):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [x,y]
def cria_copia_posicao(p):
    if eh_posicao(p):
        raise ValueError("cria_copia_posicao: argumentos invalidos")
    return p.copy()

#Seletores
def obter_pos_x(p):
    return p[0]
def obter_pos_y(p):
    return p[1]

#Reconhecedores
def eh_posicao(arg):
    return type(arg) == list and len(arg)==2 and type(arg[0])==int and \
        type(arg[1])==int and arg[0]>=0 and arg[1]>= 0

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

#Reconhecedores
def eh_animal(arg):
    if type(arg) == dict:
        if "especie" in arg and "idade" in arg and "reproducao" in arg and \
            "alimentacao" in arg and "tipo" in arg and "fome" in arg and\
                "move" in arg and "del" in arg and len(arg) == 8:
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
    return arg["tipo"]=="predador"
def eh_presa(arg):
    return arg["tipo"]=="presa"
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
def reproduz_animal(a): #Ver se é preciso dar reset ao move do bebe
    novo = cria_copia_animal(a)
    novo = reset_idade(novo)
    novo = reset_fome(novo)
    a = reset_idade(a)
    return novo

#TAD Prado
#Construtores
def cria_prado(d,r,a,p):
    return {"pos":d, "rochedos":r, "animais":a,"pos_anim":p}
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
def obter_posicao_animais(m):
    return ordenar_posicoes(m["pos_anim"])
def obter_animal(m,p): #Talvez tenha que mudar
    index = m["pos_anim"].index(p)
    return m["animais"][index]

#Modificadores
def eliminar_animal(m,p):#Tentar adicionar uma forma para as presas ficarem sempre a frente no m["animais"]
    tup_anim = ()
    tup_pos = ()
    for pos in m["pos_anim"]:
        if pos != p:
            tup_pos += (pos,)
    for animais in m["animais"]:
        if not eh_eliminado(animais):
            tup_anim += (animais,)
    m["pos_anim"] = tup_pos
    m["animais"] = tup_anim
    return m
def mover_animal(m,p1,p2):
    tup = ()
    for pos in m["pos_anim"]:
        if pos != p1:
            tup += (pos,)
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
    return m

#Reconhecedores
#def eh_prado(arg)
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
                if (coord[0]==0 and coord[1]==0) or (coord[0]==\
                    obter_tamanho_x(m)-1 and coord[1]==0) or (coord[0]==\
                        obter_tamanho_x(m)-1 and coord[1]==\
                            obter_tamanho_y(m)-1) or (coord[0]==0 and coord[1]\
                                ==obter_tamanho_y(m)-1):
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

#Alto nivel
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

#Funcoes externas
def geracao(m):
    posicoes = obter_posicao_animais(m)
    for pos in posicoes:
        animal = obter_animal(m,pos)
        if not ja_moveu(animal):
            animal = aumenta_idade(animal)
            animal = aumenta_fome(animal)
            nova_pos = obter_movimento(m,pos)
            if nova_pos != pos:
                if eh_predador(animal) and eh_posicao_animal(m,nova_pos) and \
                    eh_presa(obter_animal(m,nova_pos)):
                    animal = reset_fome(animal)
                    animal = eliminar(obter_animal(m,nova_pos))
                    m = eliminar_animal(m,nova_pos)
                    m = mover_animal(m,pos,nova_pos)
                    animal = move(animal)
                else:
                    if eh_animal_faminto(animal):
                        animal = eliminar(animal)
                        m = eliminar_animal(m,pos)
                    else:
                        m = mover_animal(m,pos,nova_pos)
                        animal = move(animal)
                if eh_animal_fertil(animal):
                    bebe = reproduz_animal(animal)
                    m = inserir_animal(m,bebe,pos)
            else:
                if eh_animal_fertil(animal):
                    animal = diminui_idade(animal)
        posicoes = obter_posicao_animais(m)
    return reset_moves(m)
def simula_ecossistema(f,g,v):
    
    def ler_ficheiro(f):
        file = open(f,"r")
        nome = []
        pos = []
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
    
    def prints(g,v,prado):
        pra = prado
        if v:
            for i in range(g):
                if i != 0:
                    pra = geracao(pra)
                    if num_presas != obter_numero_presas(pra) or num_predadores\
                       != obter_numero_predadores(pra):
                        print("Predadores: "+str(obter_numero_predadores(pra))+\
                        " vs Presas: "+str(obter_numero_presas(pra))+\
                            " (Gen. "+ str(i) +")")
                        print(prado_para_str(pra))
                else:
                    print("Predadores: " + str(obter_numero_predadores(pra)) +\
                        " vs Presas: "+ str(obter_numero_presas(pra))+\
                            " (Gen. "+ str(i) +")")
                    print(prado_para_str(pra))
                num_presas = obter_numero_presas(pra)
                num_predadores = obter_numero_predadores(pra)
        else:
            for i in range(g):
                if i==0:
                    print("Predadores: " + str(obter_numero_predadores(pra)) +\
                        " vs Presas: " + str(obter_numero_presas(pra))+\
                            " (Gen. "+ str(i) +")")
                    print(prado_para_str(pra))
                elif i==g-1:
                    print("Predadores: " + str(obter_numero_predadores(pra)) +\
                        " vs Presas: " + str(obter_numero_presas(pra))+ \
                            " (Gen. "+ str(g) +")")
                    print(prado_para_str(pra))
                else:
                    pra = geracao(pra)
        return (obter_numero_predadores(pra),obter_numero_presas(pra))
    
    size,rochedos,nome,pos = ler_ficheiro(f)
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
    num_presas_predadores = prints(g,v,prado)

    return num_presas_predadores

print(simula_ecossistema("config.txt",200,False))