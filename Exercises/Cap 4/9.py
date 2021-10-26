#resumos leic
def reconhece(string):
    if not isinstance(string, str):
        raise TypeError("not a string")

    if len(string) == 0:
        return False

    i = 0
    while i < len(string) and string[i] in 'ABCD':
        i += 1
    if i == 0 or i == len(string):
        return False
    while i < len(string) and string[i] in '1234':
        i += 1
    return i == len(string)