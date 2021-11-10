def b(f1,f2):
    with open(f1,'r') as file1:
        lines = file1.readlines()[::-1]
        with open(f2,'w') as file2:
            for line in lines:
                file2.write(line)
        file2.close()
    file1.close()
    return

b("a.txt","b.txt")