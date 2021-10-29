def cria_data(d,m,a):
    if type(d) == int and type(m) == int and type(a) == int:
        if 0<d<=31 and 0<m<=12:
            return {"d":d, "m":m, "a":a}

def dia(dt):
    return dt["d"]
def mes(dt):
    return dt["m"]
def ano(dt):
    return dt["a"]

def eh_data(arg):
    if type(arg["d"]) == int and type(arg["m"])==int and type(arg["a"])==int:
        if 0<arg["d"]<=31 and 0<arg["m"]<=12:
            return True
    return False

def mesma_data(d1,d2):
    return d1["d"]==d2["d"] and d1["m"] == d2["m"] and d1["a"] == d2["a"]