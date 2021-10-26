def num_para_seq_cod(i):
    tup = ()
    if i < 0:
        raise ValueError("erro")
    while i > 0:
        digit = i%10
        i //= 10
        if digit%2 == 0:
            if digit != 8:
                digit += 2
            else:
                digit = 0
        else:
            if digit != 1:
                digit -= 2
            else:
                digit = 9
        tup = (digit,) + tup
    return tup
            
print(num_para_seq_cod(1234567890))