#resumos leic

def remove_multiplos(list, n):
    for i in range(len(list) - 1, -1, -1):
        if list[i] % n == 0:
            del(list[i])
    return list

print(remove_multiplos([2,3,5,9,12,33,34,45],3))
            
