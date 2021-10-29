def resumo_FP(dic):
    alunos_rep = 0
    alunos_pass = 0
    nota_media = 0
    for nota in dic:
        if nota < 10:
            alunos_rep += len(dic[nota])
        else:
            alunos_pass += len(dic[nota])
            nota_media += nota * len(dic[nota])
    return (nota_media/alunos_pass, alunos_rep)

notas_dict = {1 : [46592, 49212, 90300, 59312], \
15 : [52592, 59212], 20 : [58323]}
print(resumo_FP(notas_dict))