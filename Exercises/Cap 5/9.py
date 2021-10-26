from random import random
from math import ceil

def euromilhoes():
    num,esp = [],[]
    i=0
    j=0
    while i < 5:
        r = ceil(random()*50)
        if r not in num:
            num.append(r)   
        i+=1
    while j < 2:
        r = ceil(random()*12)
        if r not in esp:
            esp.append(r)
        j+=1
    return [num,esp]

print(euromilhoes())