#-------------------------------------------------------------------------------5.1----------------------------------------------------------------------------------

def eh_utilizador(entry):
    dict_keys = ["name","pass","rule"]
    rule_keys = ["vals", "char"]
    if type(entry) == dict:
        for key in dict_keys:
            if not key in entry:
                return False
        if type(entry["name"]) == str and type(entry["pass"]) == str and type(entry["rule"]) == dict:
            for key_rule in rule_keys:
                if not key_rule in entry["rule"]:
                    return False
                if type(entry["rule"]["vals"]) == tuple and type(entry["rule"]["char"] == str):
                    if len(entry["rule"]["vals"]) != 2 or len(entry["rule"]["char"])!=1 or entry["rule"]["vals"][0] > entry["rule"]["vals"][1] :
                        return False
                    return True
        return False
    return False

#-------------------------------------------------------------------------------5.2----------------------------------------------------------------------------------

def eh_senha_valida(password,entry):
    # regra individual
    if not entry["vals"][0] < password.count(entry["char"]) < entry["vals"][1]:
        return False
    #regras gerais
    repeated_letter_flag = 0
    vowel_count = password.count("a") + password.count("e") + password.count("i") + password.count("o") + password.count("u")
    for letter in password:
        if password.count(letter) >= 2:
            repeated_letter_flag = 1
    if vowel_count < 3 or repeated_letter_flag == 0:
        return False
    return True

#-------------------------------------------------------------------------------5.3----------------------------------------------------------------------------------

def filtrar_senhas(entry):
    wrong_password = []
    if type(entry) != list:
        raise ValueError("filtrar senhas:argumento invalido")
    for dictionary in entry:
        if not eh_utilizador(dictionary):
            raise ValueError("filtrar senhas:argumento invalido")
        if not eh_senha_valida(dictionary["pass"],dictionary["rule"]):
            wrong_password.append(dictionary["name"])
    return sorted(wrong_password)