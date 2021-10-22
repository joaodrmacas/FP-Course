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
