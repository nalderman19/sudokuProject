

board = [
    [0,0,0,1,7,0,2,0,0],
    [0,0,3,0,5,0,6,0,9],
    [5,0,0,0,0,0,0,1,0],
    [0,0,0,6,0,0,0,5,1],
    [8,0,0,0,0,0,0,0,3],
    [1,6,0,0,0,5,0,0,0],
    [0,2,0,0,0,0,0,0,4],
    [9,0,7,0,3,0,1,0,0],
    [0,0,1,0,2,7,0,0,0]]


def pick_empty(board):
    for i in range(9):
        for k in range(9):
            if board[i][k] == 0:
                return (i,k)
    return None


def valid(board, n, y, x):
   # look for i in row
   if n in board[y]:
       return False
   # look for i in column
   for j in range(9):
       if n == board[j][x]:
           return False
   # look in box
   # get pos in box
   boxx = x // 3
   boxy = y // 3
   for i in range(boxy*3, boxy*3+3):
       for k in range(boxx*3, boxx*3+3):
           if board[i][k] == n and (i != y and k != x):
               return False
   return True


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - - - - ")
        for k in range(9):
            print(" " + str(board[i][k]) + " ", end="")
            if (k+1) % 3 == 0 and k != 0 and k != 8:
                print(" | ", end="")
        print()


def solve_board(board):
    # get empty space to fill in
    pos = pick_empty(board)
    if pos:
        # unsolved: there is an empty cell
        y, x = pos
    else:
        # solved
        return True

    # loop through 1-9 and get first valid option
    for i in range(1,10):
        if valid(board,i,y,x):
            board[y][x] = i
            # recusion/ backtracking
            if solve_board(board): # do same thing with updated board
                return True
            board[y][x] = 0 # reset if invalid number
    return False


#pos = pick_empty(board)
#for i in range(1,10):
#    if valid(board,i,pos[0],pos[1]):
#        print(i)

print("\n - - - - - Input Board - - - - - ")
print_board(board)

solve_board(board)

print("\n - - - - - Output Board - - - - - ")
print_board(board)
print("\n\n\n")
