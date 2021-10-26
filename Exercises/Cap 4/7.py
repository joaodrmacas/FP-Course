def amigas(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
    return count/len(str1) >= 0.9

print(amigas("amigas","amigae"))