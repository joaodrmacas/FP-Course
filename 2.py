#-----------------------------------------------------------------2.1--------------------------------------------------------------------------

board = [[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0],[0,0,0,0,0]]

def obter_posicao (direction, position):
    
    if direction == "C":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i-1][j]!=0:
                    new_pos = board[i-1][j]
                    return new_pos
    
    elif direction == "B":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i+1][j]!=0:
                    new_pos = board[i+1][j]
                    return new_pos
    
    elif direction == "D":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i][j+1]!=0:
                    new_pos = board[i][j+1]
                    return new_pos

    elif direction == "E":
        for i in range(0,5):
            for j in range(0,5):
                if board[i][j] == position and board[i][j-1]!=0:
                    new_pos = board[i][j-1]
                    return new_pos
    
    return position

#-----------------------------------------------------------------2.2--------------------------------------------------------------------------

def obter_digito (sequence, position):
    t_sequence = tuple(sequence)
    for i in range(len(t_sequence)):
        position = obter_posicao(t_sequence[i], position)
    return position

#-----------------------------------------------------------------2.3--------------------------------------------------------------------------

def obter_pin(sequence_list):
    pin = ()
    pin += (obter_digito(sequence_list[0],5),)
    for i in range(1,len(sequence_list)):
        pin += (obter_digito(sequence_list[i],pin[i-1]),)
    return pin
