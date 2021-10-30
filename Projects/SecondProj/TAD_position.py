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

def obter_posicoes_adjacentes(p): #duvida
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
    
def ordenar_posicoes(t): # C->E->D->B NOT WORKING
    tup = ()
    high_y=high_x=low_y=low_x=0
    for coord in t:
        if coord[0] > high_x:
            high_x = coord[0]
        if coord[1] > high_y:
            high_y = coord[1]
        if coord[0] < low_x:
            low_x = coord[0]
        if coord[1] < low_y:
            low_y = coord[1]
    for coord in t:
        if coord[1] == high_y:
            tup += (coord,)
        if coord[0] == low_x:
            tup += (coord,)
        if coord[0] == high_y:
            tup += (coord,)
        if coord[1] == low_y:
            tup += (coord,)
    return tup
 
# p1 = cria_posicao(2,3)
# p2 = cria_posicao(7,0)
# t = obter_posicoes_adjacentes(p2)
# #print(tuple(posicao_para_str(p) for p in t))
# print(tuple(posicao_para_str(p) for p in ordenar_posicoes(t)))

