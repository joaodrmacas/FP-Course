#b
#construtores
def cria_rel(h,m,s):
    if type(h) == int and type(m) == int and type(s) == int:
        if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
            return [h,m,s]
    raise ValueError("..")
#seletores
def horas(r):
    return r[0]
def minutos(r):
    return r[1]
def segundos(r):
    return r[2]
#reconhecedores
def eh_relogio(arg):
    if type(arg) == list:
        if len(arg) == 3 and 0 <= arg[0] <= 23 and 0<=arg[1]<=59 and 0<=arg[2]<=59:
            return True
    return False

def eh_meia_noite(r):
    return r[0] == 0 and r[1] == 0 and r[2] == 0
def eh_meio_dia(r):
    return r[0] == 12 and r[1] == 0 and r[2] == 0

def mesmas_horas(r1,r2):
    return r1[0] == r2[0] and r1[1] == r2[1] and r1[2] == r2[2]

#c
def escreve_relogio(arg):
    h = m = s = ""
    if arg[0] <= 9:
        h += "0" + str(arg[0])
    else:
        h += str(arg[0])
    if arg[1] <= 9:
        m += "0" + str(arg[1])
    else:
        m += str(arg[1])
    if arg[2] <= 9:
        s += "0" + str(arg[2])
    else:
        s += str(arg[2])
    return h + ":" + m + ":" + s

#d
def depois_rel(r1,r2):
    return r1[0] < r2[0] or (r1[0]==r2[0] and r1[1]<r2[1]) or (r1[0]==r2[0] and r1[1]==r2[1] and r1[2]<r2[2])

#e
def dif_segs(r1,r2):
    if depois_rel(r1,r2):
        s1 = r1[0]*3600 + r1[1]*60 + r1[2]
        s2 = r2[0]*3600 + r2[1]*60 + r2[2]
        return s2-s1
    raise ValueError("dif_segs: primeiro arg posterior ao segundo")

print(dif_segs(cria_rel(10,2,34), cria_rel(9,21,34)))

#f
#?  