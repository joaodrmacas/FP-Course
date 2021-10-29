#b)
#construtores
def cria_rac(n,d):
    if isinstance(n,int) and isinstance(d,int):
        if d < 0:
            raise ValueError("..")
        return {"n":n, "d":d}
#seletores
def num(r):
    return r["n"]
def den(r):
    return r["d"]

#reconhecedores
def eh_racional(r):
    if isinstance(r,dict):
        if len(r) == 2 and "n" in r and "d" in r:
            return True
    return False

def eh_rac_zero(r):
        return r["n"] == 0

#testes
def rac_iguais(r1,r2):
    return r1["n"]*r2["d"] == r2["n"]*r1["d"]

#c
def escreve_rac(r):
    return  str(r["n"]) + "/" + str(r["d"])

#d
def produto_rac(r1,r2):
    return cria_rac(num(r1)*num(r2), den(r1)*den(r2))