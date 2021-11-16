#TAD POSICAO
#Construtores
def cria_posicao(x,y):
    """cria posicao: int × int → posicao

    Recebe os valores correspondentes as coordenadas de uma
    posicao e devolve a posicao correspondente.
    Levanta Erro caso os argumentos sejam invalidos
    """
    if not eh_posicao([x,y]):
        raise ValueError("cria_posicao: argumentos invalidos")
    return [x,y]
def cria_copia_posicao(p):
    """cria copia posicao: posicao → posicao
    
    Recebe uma posicao e devolve uma copia nova da posi¸c˜ao.
    Levanta erro caso os argumentos sejam invalidos
    """
    if eh_posicao(p):
        return cria_posicao(obter_pos_x(p),obter_pos_y(p))
    raise ValueError("cria_copia_posicao: argumentos invalidos")

#Seletores
def obter_pos_x(p):
    """obter pos x : posicao → int

    Devolve a componente x da posicao p.
    """
    return p[0]
def obter_pos_y(p):
    """obter pos y: posicao -> int

    Devolve a componente y da posicao p.
    """
    return p[1]

#Reconhecedores
def eh_posicao(arg):
    """eh posicao: universal → booleano´

    Devolve True caso o seu argumento seja um TAD posicao e
    False caso contrario.
    """
    return type(arg) == list and len(arg)==2 and type(arg[0])==int and \
        type(arg[1])==int and arg[0]>=0 and arg[1]>= 0
def eh_positivo(a1,a2):
    """eh positivo: int,int -> booleano

        Devolve True apenas se os dois argumentos sejam positivos
    """
    return a1>=0 and a2>=0
#Teste
def posicoes_iguais(p1,p2):
    """posicoes iguais: posicao × posicao → booleano

    Devolve True apenas se p1 e p2 sao posicoes e sao
    iguais.
    """
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_x(p1) == obter_pos_x(p2)\
        and obter_pos_y(p1) == obter_pos_y(p2)

#Transformador
def posicao_para_str(p): 
    """posicao para str : posicao → str

    Devolve a cadeia de caracteres ‘(x, y)’ que representa o
    seu argumento, sendo os valores x e y as coordenadas de p.
    """
    return "(" + str(obter_pos_x(p)) + ", " + str(obter_pos_y(p)) + ")"

#Funcoes de alto nivel
def obter_posicoes_adjacentes(p):
    """obter posicoes adjacentes: posicao → tuplo

    Devolve um tuplo com as posicoes adjacentes a posicao p,
    comecando pela posicao acima de p e seguindo no sentido horario.
    """
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
    """ ordenar posicoes: tuplo → tuplo

    Devolve um tuplo contendo as mesmas posicoes do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado.
    """
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
    """cria animal: str × int × int → animal

    Recebe uma cadeia de caracteres s nao vazia correspondente a especie do 
    animal e dois valores inteiros correspondentes a frequencia de reproducao
    "r" e a frequencia de alimentacao "a", e devolve o animal.
    Levanta erro caso os argumentos nao sejam validos
    """
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
    """cria copia animal: animal → animal
    
     recebe um animal a (predador ou presa) e devolve uma
    nova copia do animal.
    """
    if eh_animal(a):
        return cria_animal(obter_especie(a),obter_freq_reproducao(a),\
            obter_freq_alimentacao(a))
    raise ValueError("cria_copia_animal: argumentos invalidos")

#Seletores
def obter_especie(a):
    """obter especie: animal → str
    
    Devolve a cadeia de caracteres correspondente `a esp´ecie do
    animal.
    """
    return a["especie"]
def obter_freq_reproducao(a):
    """obter freq reproducao: animal → int
    Devolve a frequencia de reproducao do animal a
    """
    return a["reproducao"]
def obter_freq_alimentacao(a):
    """obter freq alimentacao: animal → int
    
    Devolve a frequencia de alimentacao do animal "a"
    """
    return a["alimentacao"]
def obter_idade(a):
    """obter idade: animal 7→ int
    
    Devolve a idade do animal a.
    """
    return a["idade"]
def obter_fome(a):
    """obter fome: animal → int
    
    Devolve a fome do animal a 
    """
    return a["fome"]
def obter_tipo(a):
    """obter tipo: animal -> str
    
    Devolve o tipo do animal a
    """
    return a["tipo"]
def ja_moveu(a):
    """ja moveu: animal -> booleano
    
    Devolve True apenas se o animal já se moveu
    """
    return a["move"]
def eh_eliminado(a):
    """eh eliminado: animal -> booleano

    Devolve True se o animal foi eliminado
    """
    return a["del"]

#Modificadores
def aumenta_idade(a):
    """aumenta idade: animal → animal

    Modifica destrutivamente o animal a incrementando o valor da sua idade
    em uma unidade, e devolve o proprio animal.
    """
    a["idade"]+=1
    return a
def diminui_idade(a):
    """diminui idade: animal → animal

    Modifica destrutivamente o animal a decrementando o valor da sua idade
    em uma unidade, e devolve o proprio animal.
    """
    a["idade"]-=1
    return a
def reset_idade(a):
    """reset idade: animal → animal
    
    Modifica destrutivamente o animal a definindo o valor da sua
    idade igual a 0, e devolve o proprio animal.
    """
    a["idade"]=0
    return a
def aumenta_fome(a):
    """aumenta fome: animal → animal
    
    Modifica destrutivamente o animal predador a incrementando o
    valor da sua fome em uma unidade, e devolve o proprio animal.
    """
    if a["tipo"] == "predador":
        a["fome"]+=1
    return a
def reset_fome(a):
    """reset fome: animal → animal
     
    modifica destrutivamente o animal predador a definindo o valor
    da sua fome igual a 0, e devolve o proprio animal. 
    """
    if a["tipo"] == "predador":
        a["fome"] = 0
    return a
def move(a):
    """move: animal -> animal
    
    Modifica destrutivamente o animal a definindo o valor do move
    para True, e devolve o proprio animal.
    """
    a["move"] = True
    return a
def eliminar(a):
    """eliminar: animal -> animal
    
    Modifica destrutivamente o animal a definindo o valor do del
    para True, e devolve o proprio animal.
    """
    a["del"] = True
    return a
def nao_eliminar(a):
    """nao eliminar: animal -> animal
    
    Modifica destrutivamente o animal a definindo o valor do del
    para False, e devolve o proprio animal.
    """
    a["del"] = False
    return a
def reset_move(a):
    """reset move: animal → animal
    
    Modifica destrutivamente o animal a definindo o valor do move
    para False, e devolve o proprio animal.
    """
    a["move"]=False
    return a

#Reconhecedores
def eh_animal(arg):
    """eh animal: universal → booleano
    
    Devolve True caso o seu argumento seja um TAD animal e
    False caso contr´ario.
    """
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
    """universal → booleano
    
    Devolve True caso o seu argumento seja um TAD animal do
    tipo predador e False caso contrario
    """
    if eh_animal(arg) and arg["tipo"]=="predador":
        return True
    return False
def eh_presa(arg):
    """eh presa: universal 7→ booleano
    
    Devolve True caso o seu argumento seja um TAD animal do
    tipo presa e False caso contrario.

    """
    if eh_animal(arg) and arg["tipo"]=="presa":
        return True
    return False

#Teste
def animais_iguais(a1,a2):
    """animais iguais: animal × animal → booleano
    
    devolve True apenas se a1 e a2 sao animais e sao
    iguais.
    """
    return eh_animal(a1) and eh_animal(a2) and obter_especie(a1)==\
        obter_especie(a2) and obter_idade(a1)==obter_idade(a2) and \
            obter_freq_reproducao(a1)==obter_freq_reproducao(a2) and \
                obter_freq_alimentacao(a1)==obter_freq_alimentacao(a2)\
                and obter_tipo(a1)==obter_tipo(a2) and obter_fome(a1)==\
                    obter_fome(a2) and ja_moveu(a1)==ja_moveu(a2) and \
                        eh_eliminado(a1)==eh_eliminado(a2)

#Transformadores
def animal_para_char(a):
    """ animal para char : animal → str
    
    Devolve a cadeia de caracteres dum unico elemento correspondente ao
    primeiro caracter da especie do animal passada por argumento, em maiuscula
    para animais predadores e em min´uscula para animais presa.
    """
    if eh_presa(a):
        return obter_especie(a)[0].lower()
    if eh_predador(a):
        return obter_especie(a)[0].upper()
def animal_para_str(a):
    """animal para str : animal → str

    Devolve a cadeia de caracteres que representa o animal:
    Exemplo: cria_animal(’fox’, 20, 10) -> "fox [0/20;0/10]"
    """
    if eh_presa(a):
        return str(obter_especie(a)) + " [" + str(obter_idade(a)) + "/" + \
            str(obter_freq_reproducao(a)) + "]"
    elif eh_predador(a):
        return str(obter_especie(a)) + " [" + str(obter_idade(a)) + "/" + \
            str(obter_freq_reproducao(a)) + ";" + str(obter_fome(a)) + "/" +\
                str(obter_freq_alimentacao(a)) + "]"

#Alto Nivel
def eh_animal_fertil(a):
    """eh animal fertil: animal → booleano
    
    devolve True caso o animal a tenha atingido a idade de reproducao e
    False caso contrario.
    """
    return obter_idade(a) == obter_freq_reproducao(a)
def eh_animal_faminto(a):
    """eh animal faminto: animal → booleano
    
    devolve True caso o animal a tenha atingindo um valor de
    fome igual ou superior a sua frequencia de alimentacao e False caso
    contrario. As presas devolvem sempre False.
    """
    if eh_predador(a):
        return obter_fome(a) >= obter_freq_alimentacao(a)
    return False
def reproduz_animal(a):
    """reproduz animal: animal → animal
    
    recebe um animal a devolvendo um novo animal da mesma
    especie com idade e fome igual a 0, e modificando destrutivamente 
    o animal passado como argumento a alterando a sua idade para 0.
    """
    novo = cria_copia_animal(a)
    novo = reset_idade(novo)
    novo = nao_eliminar(novo)
    novo = reset_fome(novo)
    a = reset_idade(a)
    return novo

#TAD Prado
#Construtores
def cria_prado(d,r,a,p):
    """cria prado: posicao × tuplo × tuplo × tuplo → prado
    
    Recebe uma posciao d correspondente a posicao que
    ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
    mais posicoes correspondentes aos rochedos que nao sao as montanhas dos
    limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p 
    da mesma dimensao do tuplo a com as posicoes correspondentes ocupadas pelos
    animais; e devolve o prado que representa internamente o mapa e os animais
    presentes.
    Levanta erro caso os argumentos sejam invalidos
    """
    prado = {"pos":d, "rochedos":r, "animais":a,"pos_anim":p}
    if eh_prado(prado):
        return prado
    raise ValueError("cria_prado: argumentos invalidos")
def cria_copia_prado(m):
    """cria copia prado: prado → prado
    
    Recebe um prado e devolve uma nova copia do prado.
    """
    rochedos,animais,posicoes = (),(),()
    if eh_prado(m):
        for rocha in m["rochedos"]:
            rochedos += (cria_copia_posicao(rocha),)
        for animal in m["animais"]:
            animais += (cria_copia_animal(animal),)
        for pos in m["pos_anim"]:
            posicoes += (cria_copia_posicao(pos),)
        return cria_prado(cria_copia_posicao(m["pos"]),rochedos,animais,posicoes)
    raise ValueError("cria_copia_prado: argumentos invalidos")

#Seletores
def obter_tamanho_x(m):
    """obter tamanho x: prado 7→ int
    
    Devolve o valor inteiro que corresponde a dimensao N(x)
    do prado.
    """
    return obter_pos_x(m["pos"]) + 1
def obter_tamanho_y(m):
    """obter tamanho y: prado → int
    
    Devolve o valor inteiro que corresponde a dimensao N(y)
    do prado.
    """
    return obter_pos_y(m["pos"]) + 1
def obter_numero_predadores(m):
    """obter numero predadores: prado → int
    
    Devolve o numero de animais predadores no prado.
    """
    num = 0
    for animais in m["animais"]:
        if eh_predador(animais):
            num += 1
    return num
def obter_numero_presas(m):
    """obter numero presas: prado → int
    
    Devolve o numero de animais presa no prado.
    """
    num = 0
    for animais in m["animais"]:
        if eh_presa(animais):
            num += 1
    return num
def obter_posicao_animais(m):
    """obter posicao animais: prado → tuplo posicoes
    
    devolve um tuplo contendo as posi¸c˜oes do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado.
    """
    return ordenar_posicoes(m["pos_anim"])
def obter_animal(m,p):
    """obter animal: prado × posicao → animal
    
    Devolve o animal do prado que se encontra na posicao p.
    """
    index = ver_index(m,p)
    return m["animais"][index]

#Modificadores
def eliminar_animal(m,p):
    """eliminar animal: prado × posicao → prado
    
    Modifica destrutivamente o prado m eliminando o animal da posicao p
    deixando-a livre. Devolve o proprio prado.
    """
    tup_anim = ()
    tup_pos = ()
    for i in range(len(m["pos_anim"])):
        if not posicoes_iguais(m["pos_anim"][i],p):
            tup_pos += (m["pos_anim"][i],)
        else:
            index = ver_index(m,p)
    for j in range(len(m["animais"])):
        if not eh_eliminado(m["animais"][j]) and j!=index:
            tup_anim += (m["animais"][j],)
    m["pos_anim"] = tup_pos
    m["animais"] = tup_anim
    return m
def mover_animal(m,p1,p2):
    """mover animal: prado × posicao × posicao → prado
    
    Modifica destrutivamente o prado m movimentando
    o animal da posicao p1 para a nova posicao p2, deixando livre a posicao onde
    se encontrava. Devolve o proprio prado.
    """
    tup = ()
    for pos in m["pos_anim"]:
        if not posicoes_iguais(pos,p1):
            tup += (pos,)
        else:
            tup += (p2,)
    m["pos_anim"] = tup
    return m
def inserir_animal(m,a,p):
    """inserir animal: prado × animal × posicao 7→ prado
    
    Modifica destrutivamente o prado m acrescentando
    na posicao p do prado o animal a passado com argumento.
    Devolve o proprio prado.
    """
    m["animais"] += (a,)
    m["pos_anim"] += (p,)
    return m
def reset_move_prado(m):
    """reset move prado: prado -> prado
    
    Modifica destrutivamente o prado m, alterando todos os "move" dos animais
    para False. Retorna o proprio prado
    """
    for animais in m["animais"]:
        animais = reset_move(animais)
    return m

#Reconhecedores
def eh_prado(arg):
    """eh prado: universal → booleano
    
    Devolve True caso o seu argumento seja um TAD prado e False
    caso contrario.
    """
    if type(arg)==dict and len(arg)==4 and eh_posicao(arg["pos"]) and type\
        (arg["rochedos"])==tuple and len(arg["rochedos"])>=0 and type(arg\
            ["animais"])==tuple and len(arg["animais"])>=1 and type(arg\
                ["pos_anim"])==tuple and len(arg["pos_anim"])==len(arg\
                    ["animais"]):
                for posicoes in arg["rochedos"]:
                    if not eh_posicao(posicoes):
                        return False
                    if obter_pos_x(posicoes)>=obter_pos_x(arg["pos"]) or \
                        obter_pos_y(posicoes)>=obter_pos_y(arg["pos"]) or \
                        (obter_pos_x(posicoes)==0 and obter_pos_y(posicoes)==0):
                        return False
                for animal in arg["animais"]:
                    if not eh_animal(animal):
                        return False
                for posicao in arg["pos_anim"]:
                    if not eh_posicao(posicao):
                        return False
                    if obter_pos_x(posicao)>=obter_pos_x(arg["pos"]) or \
                        obter_pos_y(posicao)>=obter_pos_y(arg["pos"]):
                        return False
                return True
    return False
def eh_posicao_animal(m,p):
    """eh posicao animal: prado × posicao → booleano

    Devolve True apenas no caso da posicao p do prado
    estar ocupada por um animal.
    """
    for pos in m["pos_anim"]:
        if posicoes_iguais(pos,p):
            return True
    return False
def eh_posicao_obstaculo(m,p):
    """eh posicao obstaculo: prado × posicao → booleano
    
    Devolve True apenas no caso da posicao p do prado
    corresponder a uma montanha ou rochedo
    """

    def eh_montanha(m,p):
        """eh montanha: prado x posicao -> booleano
        
        Devolve True apenas se no caso da posicao p do prado corresponder
        a uma montanha
        """
        for i in range(obter_tamanho_x(m)):
            if posicoes_iguais(p,cria_posicao(i,0)):
                return True
            if posicoes_iguais(p,cria_posicao(i,obter_tamanho_y(m)-1)):
                return True
        for j in range(obter_tamanho_y(m)):
            if posicoes_iguais(p,cria_posicao(0,j)):
                return True
            if posicoes_iguais(p,cria_posicao(obter_tamanho_x(m)-1,j)):
                return True
        return False

    if eh_montanha(m,p):
        return True
    for pos in m["rochedos"]:
        if posicoes_iguais(pos,p):
            return True
    return False
def eh_posicao_livre(m,p):
    """eh posicao livre: prado × posicao → booleano
    
    devolve True apenas no caso da posicao p do prado
    corresponder a um espaco livre (sem animais, nem obstaculos).
    """
    if not eh_posicao_animal(m,p) and not eh_posicao_obstaculo(m,p):
        return True
    return False

#Teste
def prados_iguais(p1,p2):
    """prados iguais: prado × prado → booleano
    
    Devolve True apenas se p1 e p2 forem prados e forem
    iguais.
    """
    return eh_prado(p1) and eh_prado(p2) and p1 == p2

#Transformador
def prado_para_str(m):
    """prado para str : prado 7→ str
    
    Devolve uma cadeia de caracteres que representa o prado
    """
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

#Alto nivel
def obter_valor_numerico(m,p):
    """obter valor numerico: prado × posicao → int
    
    Devolve o valor num´erico da posicao p correspondente
    a ordem de leitura no prado m.
    """
    l,c = obter_pos_y(p),obter_pos_x(p)
    Ncol = obter_tamanho_x(m)
    return l*Ncol + c
def obter_movimento(m,p):
    """obter movimento: prado × posicao → posicao
    
    Devolve a posicao seguinte do animal na posicao p dentro
    do prado m de acordo com as regras de movimento dos animais no prado.
    """
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
    """geracao: prado → prado 
    
    E a funcao auxiliar que modifica o prado m fornecido como argumento de
    acordo com a evolucao correspondente a uma geracao completa, e devolve o
    proprio prado. Isto e, seguindo a ordem de leitura do prado, cada animal
    realiza o seu turno de acao de acordo com as regras.
    """
    posicoes = obter_posicao_animais(m)
    for pos in posicoes:
        animal = obter_animal(m,pos)
        if not ja_moveu(animal):
            animal = aumenta_idade(animal)
            animal = aumenta_fome(animal)
            nova_pos = obter_movimento(m,pos)
            if not posicoes_iguais(nova_pos,pos):
                if eh_predador(animal) and eh_posicao_animal(m,nova_pos) and \
                    eh_presa(obter_animal(m,nova_pos)):
                    animal = reset_fome(animal)
                    eliminar(obter_animal(m,nova_pos))
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
                if eh_animal_faminto(animal):
                    animal = eliminar(animal)
                    m = eliminar_animal(m,pos)
                if eh_animal_fertil(animal):
                    animal = diminui_idade(animal)
        posicoes = obter_posicao_animais(m)
    return reset_move_prado(m)
def simula_ecossistema(f,g,v):
    """simula ecossistema: str × int × booleano → tuplo
    E a funcao principal que permite simular o ecossistema de um  prado. A
    funcao recebe uma cadeia de caracteres f, um valor inteiro g e um valor
    booleano v e devolve o tuplo de dois elementos correspondentes ao numero 
    de predadores e presas no prado no fim da simulacao. A cadeia de caracteres
    f passada por argumento corresponde ao nome do ficheiro de configuracao
    da simulacao. O valor inteiro g corresponde ao numero de geracoes a simular.
    O argumento booleano v ativa o modo verboso (True) ou o modo quiet (False).
    No modo quiet mostra-se pela saida standard o prado,o numero de animais e o
    numero de geracao no inicio da simulacao e apos a ultima geracao. No modo
    verboso, apos cada geracao, mostra-se tambem o prado, o numero de animais e
    o n´umero de geracao, apenas se o numero de animais predadores ou presas se
    tiver alterado.
    """
    def ler_ficheiro(file_name):
        """ler ficheiro: str -> posicao x tuplo posicoes x tuplo animais + posicoes

        Recebe o nome do ficheiro e retorna a dimensao do prado, as posicoes dos
        rochedos e os animais com as suas posicoes
        """
        r = []
        a = []
        s = []
        with open(file_name,"r") as f:
            file = f.readlines()
            size = file[0]
            size = size[1:-2].split(",")
            for el in size:
                s.append(el.replace(" ",""))
            size = [int(s[0]),int(s[1])]
            #rochedos
            rochedos = file[1]
            if rochedos != "()\n":
                rochedos = rochedos[1:-2].split(",")
                for rocha in rochedos:
                    r += [int(rocha.replace("(","").replace(")","").\
                        replace(" ",""))]
            else:
                r = []
            #animais
            animais = file[2:]
            for animal in animais:
                animal = animal[1:-2].replace("'","").replace("(","").\
                    replace(")","").replace(" ","")
                animal = animal.split(",")
                for i in range(1,5):
                    animal[i] = int(animal[i])
                a += [animal]
        return size,r,a
    
    def prints(g,v,prado):
        """prints: int x booleano x prado -> tuplo int
        
        E a funcao que permite printar o prado enquanto as condicoes do argumento
        v não forem alcancadas. Retorna o tuplo com o numero de predadores e presas
        no fim da simulacao 
        """
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
            for i in range(g+2):
                if i==0:
                    print("Predadores: " + str(obter_numero_predadores(pra)) +\
                        " vs Presas: " + str(obter_numero_presas(pra))+\
                            " (Gen. "+ str(i) +")")
                    print(prado_para_str(pra))
                elif i==g+1:
                    print("Predadores: " + str(obter_numero_predadores(pra)) +\
                        " vs Presas: " + str(obter_numero_presas(pra))+ \
                            " (Gen. "+ str(g) +")")
                    print(prado_para_str(pra))
                else:
                    pra = geracao(pra)
        return (obter_numero_predadores(pra),obter_numero_presas(pra))
    
    size,rochedos,creatures = ler_ficheiro(f)
    dim = cria_posicao(size[0],size[1])
    obs = ()
    po = ()
    animal = ()
    i = 0
    while i <= len(rochedos)-1:
        obs += (cria_posicao(rochedos[i],rochedos[i+1]),)
        i+=2
    for creature in creatures:
        animal += (cria_animal(creature[0],creature[1],creature[2]),)
        po += (cria_posicao(creature[3],creature[4]),)
    prado = cria_prado(dim,obs,animal,po)
    num_presas_predadores = prints(g,v,prado)

    return num_presas_predadores
def ver_index(m,p):
    """ver index: prado x posicao -> int
    
    Percorre as posicoes do prado até encontrar uma posicao igual ao
    segundo argumento. Devolve o index dessa posicao
    """
    for i in range(len(m["pos_anim"])):
        if posicoes_iguais(m["pos_anim"][i],p):
            return i