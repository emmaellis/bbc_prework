"""
Assumptions:

Positions outside the size of the seed board can be added if life
can be created there.

The user will specify the number of iterations they want to print, along with
the starting max_x and max_y value (min x, and y assumed to be 0).

Game state is stored in a dictionary mapping position as (x, y) to value 0 or 1
depending on whether there's a live cell.

"""
MAX_X, MAX_Y, MIN_X, MIN_Y = 0, 0, 0, 0
#play function that takes in a seed board
# maybe give user the option to input the number of iterations they would like?
# print out representation of the board
# assuming the user is specifying the board
def play(board, iterations, max_x, max_y):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    MIN_X = MIN_Y = 0
    MAX_X = max_x
    MAX_Y = max_y
    print_board(board)
    while (iterations > 0):
        # checking to see if a life can be created beyond the current edges
        temp_board = board.copy()
        for y in range(MIN_Y-1, MAX_Y+2):
            for x in range(MIN_X-1, MAX_X+2):
                neighbors = get_neighbors(x, y, temp_board)
                # print(neighbors, x, y)
                #scenario 1: underpopulation
                if neighbors < 2:
                    die(x, y, board)
                #scenario 2: overcrowding
                elif neighbors > 3:
                    die(x, y, board)
                #scenario 4: creation of life
                elif neighbors == 3:
                    live(x, y, board)
        print_board(board)
        iterations -= 1


# create a new life and adjust the board dimensions as needed
def live(x, y, board):
    # if x is greater than MAX_X or less than MIN_X add a new column
    global MIN_X, MAX_X, MIN_Y, MAX_Y
    if x < MIN_X or x > MAX_X:
        for i in range(MIN_Y, MAX_Y + 1):
            if i == y:
                board[(x, y)] = 1
            else:
                board[(x, i)] = 0
        if x < MIN_X:
            MIN_X = x
        else:
            MAX_X = x
    # if y is greater than MAX_Y or less than MIN_Y add a new row
    elif y < MIN_Y or y > MAX_Y:
        for i in range(MIN_X, MAX_X + 1):
            if i == x:
                board[(x, y)] = 1
            else:
                board[(i, y)] = 0
        if y < MIN_Y:
            MIN_Y = y
        else:
            MAX_Y = y
    # a life will never begin in position -1, -1, len(board[0]), len(board), etc
    else:
        board[(x,y)] = 1

def die(x, y, board):
    # if y is between in the current range and domain of the board
    if x >= MIN_X and x <= MAX_X and y >= MIN_Y and y <= MAX_Y:
        board[(x,y)] = 0

#print out the board
def print_board(board):
    for y in range (MIN_Y, MAX_Y + 1):
        row = ""
        for x in range(MIN_X, MAX_X + 1):
            if board[(x, y)] == 0:
                row += "-"
            else:
                row += "x"
        print(row)
    print('\n')

# return number of live neighbors given a positions's x and y values
def get_neighbors(x, y, board):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            #check if it's in board and alive and not the position
            if i!=0 or j!=0:
                if (x+i,y+j) in board and board[(x+i,y+j)] == 1:
                    # print("position:")
                    # print(x, y)
                    # print(x+i,y+j)
                    neighbors += 1
    return neighbors
