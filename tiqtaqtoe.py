import random

# Dictionary of dice: Contains colours = [value, dice1, dice2, dice3, dice4], with dice = [position, probability].
xColours = {'green', 'turq', 'blue', 'purple', 'sparkle'}
oColours = {'yellow', 'orange', 'grey', 'blank'}
allColours = {'green', 'turq', 'blue', 'purple', 'sparkle', 'yellow', 'orange', 'grey', 'blank'}

# Initialize dice
dice = {'green': [], 'turq': [], 'blue': [], 'purple': [], 'sparkle': [],
        'yellow': [], 'orange': [], 'grey': [], 'blank': []}
for colour in xColours:
    dice[colour] = ['X', [-1,0.0], [-1,0.0], [-1,0.0], [-1,0.0]]
for colour in oColours:
    dice[colour] = ['O', [-1,0.0], [-1,0.0], [-1,0.0], [-1,0.0]]

# Game board: [square0, ..., square8], with squarei = [[X, probX], [O, probO]]
mainBoard = [
    [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]],
    [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]],
    [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]]
]

#########################
#### BASIC FUNCTIONS ####
#########################

# Print board
def print_board(board):
    print("Current board:\n" +
        board[0][0][0] + ": " + str(board[0][0][1]) + ", " + board[0][1][0] + ": " + str(board[0][1][1])
          + " | " + board[1][0][0] + ": " + str(board[1][0][1]) + ", " + board[1][1][0] + ": " + str(board[1][1][1])
          + " | " + board[2][0][0] + ": " + str(board[2][0][1]) + ", " + board[2][1][0] + ": " + str(board[2][1][1])
        + "\n-------------------------------------------------\n" +
        board[3][0][0] + ": " + str(board[3][0][1]) + ", " + board[3][1][0] + ": " + str(board[3][1][1])
          + " | " + board[4][0][0] + ": " + str(board[4][0][1]) + ", " + board[4][1][0] + ": " + str(board[4][1][1])
          + " | " + board[5][0][0] + ": " + str(board[5][0][1]) + ", " + board[5][1][0] + ": " + str(board[5][1][1])
        + "\n-------------------------------------------------\n" +
        board[6][0][0] + ": " + str(board[6][0][1]) + ", " + board[6][1][0] + ": " + str(board[6][1][1])
          + " | " + board[7][0][0] + ": " + str(board[7][0][1]) + ", " + board[7][1][0] + ": " + str(board[7][1][1])
          + " | " + board[8][0][0] + ": " + str(board[8][0][1]) + ", " + board[8][1][0] + ": " + str(board[8][1][1])
    )
    return True

# Places a die of a given colour on the board
def place_die(board, colour, square, prob):
    if prob != 0.0 and prob != 0.25 and prob!= 0.5 and prob != 1.0:
        print("Error: Probability " + str(prob) + " not allowed.")
        return False
    for i in range(1,5):
        if colour[i][0] == -1:
            colour[i][0] = square  # Update die placement
            colour[i][1] = prob     # Update die orientation
            break
    else: # Break was never reached
        print("Error: Out of dice.")
        return False
    if colour[0] == 'X':
        board[square][0][1] = prob  # Update X-value
    elif colour[0] == 'O':
        board[square][1][1] = prob  # Update O-value
    else:
        print("Error: Invalid die.")
        return False
    print("Placed " + colour[0] + " on square " + str(square) + " with probability " + str(prob) + ".")
    return True

# Checks if a colour is available
def isColourFree(colour):
    for i in range(1,5):
        if colour[i][0] != -1: 
            print("Error: Colour already placed.")
            return False
    return True

# Halves the probability of a die of a given colour and updates the board
def halveProb(board, die, value):
    if value != 'X' and value != 'O':
        print("Error: Invalid value.")
        return False
    square = die[0]
    if square == -1:
        print("Error: Die is not on board.")
        return False
    die[1] = die[1] / 2 # Halves probability of die
    if value == 'X':
        board[square][0][1] = board[square][0][1] / 2 # Updates X value of square
    if value == 'O':
        board[square][1][1] = board[square][1][1] / 2 # Updates O value of square
    print("Halved probability of " + value + " on square " + str(square) + ".")
    return True

###############
#### MOVES ####
###############

# Performs a classical move
def classic_move(board, die, square):
    if board[square][0][1] != 0.0 or board[square][1][1] != 0.0:
        print("Error: The square must be empty for a classical move.")
        return False
    if isColourFree(die):
        return place_die(board, die, square, 1.0)

# Performs a superposition move
def superpos_move(board, die, square1, square2):
    if square1 == square2:
        print("Error: Please choose two squares for the superposition move.")
        return False
    x1 = board[square1][0][1]
    o1 = board[square1][1][1]
    x2 = board[square2][0][1]
    o2 = board[square2][1][1]
    #if (x1 != 0.0 or o1 != 0.0) or (o2 != 0.0 or o2 != 0.0):
    if not x1 == o1 == x2 == o2 == 0.0:
        print("Error: Both squares must be empty for a superposition move.")
        return False
    if isColourFree(die):
        return place_die(board, die, square1, 0.5) and place_die(board, die, square2, 0.5)

# Performs an entanglement move
def entang_move(board, die, square1, square2):
    if square1 == square2:
        print("Error: Please choose two squares for the entanglement move.")
        return False
    x1 = board[square1][0][1]
    o1 = board[square1][1][1]
    x2 = board[square2][0][1]
    o2 = board[square2][1][1]
    if x1 != 0.0 or o1 != 0.0:
        if x2 != 0.0 or o2 != 0.0:
            print("Error: One square must be empty for the entanglement move.")
            return False
    if isColourFree(die):
        if die[0] == 'X':
            if x1 != 0.0 or x2 != 0.0:
                print("Error: X can't entangle with X.")
                return False
            if o1 == o2 == 0.0:
                print("Error: One square must have an O to entangle with X.")
                return False
            if o1 != 0.0:
                for colour in oColours: # Searches for the relevant die
                    for j in range(1,5):
                        if dice[colour][j][0] == square1:
                            halveProb(board, dice[colour][j], 'O') # Halves probability of present die
                            place_die(board, dice[colour], square2, o1/2) # Places a new die of the same colour
            elif o2 != 0.0:
                for colour in xColours: # Searches for the relevant die
                    for j in range(1,5):
                        if dice[colour][j][0] == square2:
                            halveProb(board, dice[colour][j], 'O') # Halves probability of present die
                            place_die(board, dice[colour], square1, o2/2) # Places a new die of the same colour
            else:
                print("Error: Unknown error.")
                return False
        if die[0] == 'O':
            if o1 != 0.0 or o2 != 0.0:
                print("Error: O can't entangle with O.")
                return False
            if x1 == x2 == 0.0:
                print("Error: One square must have an X to entangle with O.")
                return False
            if x1 != 0.0:
                for colour in xColours: # Searches for the relevant die
                    for j in range(1,5):
                        if dice[colour][j][0] == square1:
                            halveProb(board, dice[colour][j], 'X') # Halves probability of present die
                            place_die(board, dice[colour], square2, dice[colour][j][1]) # Places a new die of the same colour
            elif x2 != 0.0:
                for colour in oColours: # Searches for the relevant die
                    for j in range(1,5):
                        if dice[colour][j][0] == square2:
                            halveProb(board, dice[colour][j], 'X') # Halves probability of present die
                            place_die(board, dice[colour], square1, o2/2) # Places a new die of the same colour
            else:
                print("Error: Unknown error.")
                return False
        return place_die(board, die, square1, 0.5) and place_die(board, die, square2, 0.5)

#############################
#### MEASURING THE BOARD ####
#############################
def rolld4():
    return random.randint(1,4)

# WIP!!
def measureColour(board, colour):
    # colour = [value, dice1, dice2, dice3, dice4], with dice = [position, probability]
    # board: [square0, ..., square8], with squarei = [[X, probX], [O, probO]]
    value = colour[0]
    onBoard = [] # Dice of colour currently on board
    squares = [] # Squares on board with dice of colour
    for i in range(1,4):
        if colour[i][0] != -1:
            onBoard.append(i)
            squares.append(colour[i][0])
    totalProb = 0.0
    for i in onBoard:
        totalProb += colour[i][1]
    if totalProb != 1.0:
        print("Error: Total probability is " + str(totalProb) + ".")
        return False
    # make a list of four equal-probability outcomes
    possibilities = []
    for i in onBoard:
        for j in range(0,int(4.0*colour[i][1])):
            possibilities.append([i,colour[i][0]])
    if len(possibilities) != 4:
        print("Error: Number of possibilities not equal to 4.")
        return False
    roll = rolld4()
    measuredDie = possibilities[roll - 1][0]
    measuredSquare = possibilities[roll - 1][1]
    # Update colour:
    for die in onBoard:
        if die == measuredDie: # Give prob 1
            colour[die][1] = 1.0
        else: # Take die off board
            colour[die] = [-1, 0.0]
    # Update board:
    # This thing feels like it could and should be simplified...
        for square in squares:
            if square == measuredSquare:
                if value == 'X':
                    board[square][0][1] = 1.0
                    if board[square][1][1] != 0.0:
                        # Remove die of opposite value:
                        for ocolour in oColours: # Find the affected die
                            for j in range(1,5):
                                if dice[ocolour][j][0] == square:
                                    dice[ocolour][j] = [-1, 0.0] # Take die off board
                        board[square][1][1] = 0.0
                if value == 'O':
                    board[square][1][1] = 1.0
                    if board[square][0][1] != 0.0:
                        # Remove die of opposite value:
                        for xcolour in xColours: # Searches for the affected die
                            for j in range(1,5):
                                if dice[xcolour][j][0] == square:
                                    dice[xcolour][j] = [-1, 0.0] # Take die off board
                        board[square][0][1] = 0.0
            elif square != measuredSquare:
                if value == 'X':
                    board[square][0][1] = 0.0
                    if board[square][1][1] != 0.0:
                        # Double prob of die of opposite value:
                        for ocolour in oColours: # Find the affected die
                            for j in range(1,5):
                                if dice[ocolour][j][0] == square:
                                    dice[ocolour][j][1] = 2*dice[ocolour][j][1] # Double prob
                        board[square][1][1] = 2*board[square][1][1] # Double prob
                if value == 'O':
                    board[square][1][1] = 0.0
                    if board[square][0][1] != 0.0:
                        # Double prob of die of opposite value:
                        for xcolour in xColours: # Find the affected die
                            for j in range(1,5):
                                if dice[xcolour][j][0] == square:
                                    dice[xcolour][j][1] = 2*dice[xcolour][j][1] # Double prob
                        board[square][0][1] = 2*board[square][0][1] # Double prob
    print("Measured value " + str(value) + " in square " + str(measuredSquare) + ".")
    return True


def measureBoard(board):
    return True

##########################
#### RATING THE BOARD ####
##########################

# Checks if X currently has a winning position
def CanXWin(board):
    # Top three horizontal
    if board[0][0][1] == board[1][0][1] == board[2][0][1] == 1.0:
        return True
    # Middle three horizontal
    if board[3][0][1] == board[4][0][1] == board[5][0][1] == 1.0:
        return True
    # Bottom three horizontal
    if board[6][0][1] == board[7][0][1] == board[8][0][1] == 1.0:
        return True
    # Left three vertical
    if board[0][0][1] == board[3][0][1] == board[6][0][1] == 1.0:
        return True
    # Middle three vertical
    if board[1][0][1] == board[4][0][1] == board[7][0][1] == 1.0:
        return True
    # Middle three vertical
    if board[2][0][1] == board[5][0][1] == board[8][0][1] == 1.0:
        return True
    # Falling diagonal
    if board[0][0][1] == board[4][0][1] == board[8][0][1] == 1.0:
        return True
    # Rising diagonal
    if board[6][0][1] == board[4][0][1] == board[2][0][1] == 1.0:
        return True
    return False

# Checks if O currently has a winning position
def CanOWin(board):
    # Top three horizontal
    if board[0][1][1] == board[1][1][1] == board[2][1][1] == 1.0:
        return True
    # Middle three horizontal
    if board[3][1][1] == board[4][1][1] == board[5][1][1] == 1.0:
        return True
    # Bottom three horizontal
    if board[6][1][1] == board[7][1][1] == board[8][1][1] == 1.0:
        return True
    # Left three vertical
    if board[0][1][1] == board[3][1][1] == board[6][1][1] == 1.0:
        return True
    # Middle three vertical
    if board[1][1][1] == board[4][1][1] == board[7][1][1] == 1.0:
        return True
    # Middle three vertical
    if board[2][1][1] == board[5][1][1] == board[8][1][1] == 1.0:
        return True
    # Falling diagonal
    if board[0][1][1] == board[4][1][1] == board[8][1][1] == 1.0:
        return True
    # Rising diagonal
    if board[6][1][1] == board[4][1][1] == board[2][1][1] == 1.0:
        return True
    return False

# Checks the board to see if anyone won or if it's a draw
def check_board(board):
    if CanXWin(board):
        if CanOWin(board):
            print("Draw!")
            return True
        else:
            print("X won!")
            return True
    elif CanOWin(board):
        print("O won!")
        return True
    else:
        print("Draw!")
        return True


#######################
#### Testing/Debug ####
#######################

testBoard = [
    [['X',1.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]],
    [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]],
    [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]], [['X',0.0], ['O',0.0]]
]

print_board(testBoard)
print()
classic_move(testBoard, dice['blue'], 1)
print()
print_board(testBoard)
print()
entang_move(testBoard, dice['yellow'], 1, 2)
print()
print_board(testBoard)
print()
superpos_move(testBoard, dice['green'], 3, 4)
print()
print_board(testBoard)
print()
entang_move(testBoard, dice['orange'], 4, 5)
print()
print_board(testBoard)
print()
measureColour(testBoard, dice['orange'])
print(dice['orange'])
print(dice['green'])
print_board(testBoard)
print()
measureColour(testBoard, dice['green'])
print()
print_board(testBoard)
