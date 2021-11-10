def corta(entry,output,n):
    with open(entry,"r") as f1:
        with open(output,"w+") as f2:
            i = 0
            for l in f1.read():
                if i >= n:
                    break
                f2.write(l)
                i+=1
        f2.close()
    f1.close()
    return

corta("a.txt","b.txt",20)