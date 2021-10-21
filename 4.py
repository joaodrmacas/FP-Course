#-------------------------------------------------------------------------------4.1----------------------------------------------------------------------------------

def obter_num_seguranca(security):
    lowest_dif = 2**31-1
    for i in security:
        for j in security:
            dif = i-j
            if dif > 0 and dif<lowest_dif:
                lowest_dif = dif
    return lowest_dif

print(obter_num_seguranca((2223,424,1316,99)))
