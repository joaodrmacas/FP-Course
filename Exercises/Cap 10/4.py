def concatena(list, output):
    l = []
    for file_name in list:
        with open(file_name,"r") as read:
            l.extend(read.readlines())
        read.close()
    with open(output,"w+") as write:
        write.writelines(l)
    write.close
    return

concatena(["a.txt","b.txt"],"c.txt")