def sim_1(board):
    nextBoard = board.copy()
    repeat, count = True, 0

    while repeat:
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != '.'):
                    counted = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if i+k>-1 and j+l>-1 and i+k<len(board) and j+l<len(board[i]) and (k, l) != (0,0):
                                counted += (board[i+k][j+l] == '#')
                    if board[i][j] == 'L' and counted == 0:
                        nextBoard[i] = nextBoard[i][:j] + '#' + board[i][j+1:]
                    if board[i][j] == '#' and counted >= 4:
                        nextBoard[i] = nextBoard[i][:j] + 'L' + board[i][j+1:]
        repeat = (nextBoard != board)
        board = nextBoard.copy()
        
    for i in range(len(board)):
        count += board[i].count('#')

    return(count)

def sim_2(board):
    nextBoard = board.copy()
    repeat, count = True, 0

    while repeat:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j] != '.'):
                    counted = 0
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if (k, l) != (0, 0):
                                p=(i+k, j+l)
                                while p[0] in range(0,len(board)) and p[1] in range(0,len(board[1])) and board[p[0]][p[1]] not in ('L', '#'):
                                    p = (p[0]+k, p[1]+l)
                                if p[0] in range(len(board)) and p[1] in range(len(board[1])):
                                    counted += board[p[0]][p[1]] == '#'
                    if board[i][j] == 'L' and counted == 0:
                        nextBoard[i] = nextBoard[i][:j] + '#' + board[i][j+1:]
                    if board[i][j] == '#' and counted >= 5:
                        nextBoard[i] = nextBoard[i][:j] + 'L' + board[i][j+1:]
        repeat = (nextBoard != board)
        board = nextBoard.copy()
        
    for i in range(len(board)):
        count += board[i].count('#')

    return(count)
                    

with open('input.txt') as file:
    board = [e[:-1] for e in file.readlines()]

    #print(sim_1(board))
    print(sim_2(board))

print('gotem')
