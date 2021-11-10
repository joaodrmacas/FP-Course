def procura(word,file_name):
    with open(file_name,"r") as f:
        for line in f:
            if word in line:
                print(line, end="")
    f.close()
    return

procura("ola","c.txt")