import random
import copy

xColours = {'green', 'turqs', 'ocean', 'prple', 'sprkl'}
oColours = {'yllow', 'ornge', 'smoke', 'blank'}
allColours = {'green', 'turqs', 'ocean', 'prple', 'sprkl', 'yllow', 'ornge', 'smoke', 'blank'}
allSquares = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

# Dictionary of dice: Contains colours = [value, dice1, dice2, dice3, dice4]
# Initialize dice = dictionary of colours, each with four dice, each die = [position, probability]
# (where position = -1 means not placed on board).
mainDice = {'green': [], 'turqs': [], 'ocean': [], 'prple': [], 'sprkl': [],
        'yllow': [], 'ornge': [], 'smoke': [], 'blank': []}
for colour in xColours:
    mainDice[colour] = ['X', [-1, 0.0], [-1, 0.0], [-1, 0.0], [-1, 0.0]]
for colour in oColours:
    mainDice[colour] = ['O', [-1, 0.0], [-1, 0.0], [-1, 0.0], [-1, 0.0]]

#print(dice)

# Game board: [square0, ..., square8], with squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
mainBoard = [
    [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]],
    [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]],
    [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]], [['X', 0.0, 'empty', -1], ['O', 0.0, 'empty', -1]]
]

#########################
#### BASIC FUNCTIONS ####
#########################

# Print board colours and probabilities
# Game board: [square0, ..., square8], with squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
def print_board(board):
    print("\nCurrent board:\n" +
        board[0][0][0] + ": " + str(board[0][0][1]) + " (" + board[0][0][2] + ")" # 0X
          + " | " + board[1][0][0] + ": " + str(board[1][0][1]) + " (" + board[1][0][2] + ")" # 1X
          + " | " + board[2][0][0] + ": " + str(board[2][0][1]) + " (" + board[2][0][2] + ")" # 2X 
          + "\n"
          + board[0][1][0] + ": " + str(board[0][1][1]) + " (" + board[0][1][2] + ")" # 0O
          + " | " + board[1][1][0] + ": " + str(board[1][1][1]) + " (" + board[1][1][2] + ")" # 1O
          + " | " + board[2][1][0] + ": " + str(board[2][1][1]) + " (" + board[2][1][2] + ")" # 2O
        + "\n-------------------------------------------------\n" +
        board[3][0][0] + ": " + str(board[3][0][1]) + " (" + board[3][0][2] + ")" # 3X
          + " | " + board[4][0][0] + ": " + str(board[4][0][1]) + " (" + board[4][0][2] + ")" # 4X
          + " | " + board[5][0][0] + ": " + str(board[5][0][1]) + " (" + board[5][0][2] + ")" # 5X 
          + "\n"
          + board[3][1][0] + ": " + str(board[3][1][1]) + " (" + board[3][1][2] + ")" # 3O
          + " | " + board[4][1][0] + ": " + str(board[4][1][1]) + " (" + board[4][1][2] + ")" # 4O
          + " | " + board[5][1][0] + ": " + str(board[5][1][1]) + " (" + board[5][1][2] + ")" # 5O
        + "\n-------------------------------------------------\n" +
        board[6][0][0] + ": " + str(board[6][0][1]) + " (" + board[6][0][2] + ")" # 6X
          + " | " + board[7][0][0] + ": " + str(board[7][0][1]) + " (" + board[7][0][2] + ")" # 7X
          + " | " + board[8][0][0] + ": " + str(board[8][0][1]) + " (" + board[8][0][2] + ")" # 8X 
          + "\n"
          + board[6][1][0] + ": " + str(board[6][1][1]) + " (" + board[6][1][2] + ")" # 6O
          + " | " + board[7][1][0] + ": " + str(board[7][1][1]) + " (" + board[7][1][2] + ")" # 7O
          + " | " + board[8][1][0] + ": " + str(board[8][1][1]) + " (" + board[8][1][2] + ")" # 8O
    )
    return True

# Places a die of a given colour on the board
# Remember, squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
def place_die(board, dice, colour, square, prob):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    if prob != 0.0 and prob != 0.25 and prob!= 0.5 and prob != 1.0:
        print("\nError: Probability " + str(prob) + " not allowed")
        return False
    dieNum = -1
    for i in range(1,5):
        if dice[colour][i][0] == -1:
            dieNum = i
            dice[colour][i][0] = square  # Update die placement
            dice[colour][i][1] = prob     # Update die orientation
            break
    else: # Break was never reached
        print("\nError: Out of " + colour + "-coloured dice")
        return False
    if dice[colour][0] == 'X':
        board[square][0][1] = prob  # Update X-value
        board[square][0][2] = colour # Update X-die colour
        board[square][0][3] = dieNum # Update X-die number
    elif dice[colour][0] == 'O':
        board[square][1][1] = prob  # Update O-value
        board[square][1][2] = colour # Update O-die colour
        board[square][1][3] = dieNum # Update O-die number
    else:
        print("\nError: Invalid die")
        return False
    print("\nPlaced " + dice[colour][0] + " die " + colour + " no." + str(dieNum)
          + " on square " + str(square+1) + "\n\twith squared-amplitude " + str(prob))
    return True

# Checks if a colour is available
def isColourFree(dice, colour):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    for i in range(1,5):
        if dice[colour][i][0] != -1: 
            print("\nError: Colour already placed")
            return False
    return True

# Halves the probability of a die of a given colour and updates the board
# Remember: die = [position, probability]
def halveProb(board, dice, colour, dieNum, value):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    if value != 'X' and value != 'O':
        print("\nError: Invalid value")
        return False
    square = dice[colour][dieNum][0]
    if square == -1:
        print("\nError: Die is not on board")
        return False
    dice[colour][dieNum][1] = dice[colour][dieNum][1] / 2 # Halves probability of die
    if value == 'X':
        board[square][0][1] = board[square][0][1] / 2 # Updates X value of square
    if value == 'O':
        board[square][1][1] = board[square][1][1] / 2 # Updates O value of square
    print("\nHalved squared-amplitude of\n\t" + value + " die " + colour + " no." +
          str(dieNum) + " on square " + str(square+1))
    return True

###############
#### MOVES ####
###############

# Performs a classical move
def classic_move(board, dice, colour, square):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    if board[square][0][1] != 0.0 or board[square][1][1] != 0.0:
        print("\nError: The square must be empty for a classical move")
        return False
    if isColourFree(dice, colour):
        return place_die(board, dice, colour, square, 1.0)

# Performs a superposition move
def superpos_move(board, dice, colour, square1, square2):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    if square1 == square2:
        print("Error: Please choose two squares for the superposition move")
        return False
    x1 = board[square1][0][1]
    o1 = board[square1][1][1]
    x2 = board[square2][0][1]
    o2 = board[square2][1][1]
    #if (x1 != 0.0 or o1 != 0.0) or (o2 != 0.0 or o2 != 0.0):
    if not x1 == o1 == x2 == o2 == 0.0:
        print("Error: Both squares must be empty for a superposition move")
        return False
    if isColourFree(dice, colour):
        return place_die(board, dice, colour, square1, 0.5) and place_die(board, dice, colour, square2, 0.5)

# Performs an entanglement move
# Game board: [square0, ..., square8], with squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
def entang_move(board, dice, colour, square1, square2):
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    if square1 == square2:
        print("Error: Please choose two squares for the entanglement move")
        return False
    x1 = board[square1][0][1]
    o1 = board[square1][1][1]
    x2 = board[square2][0][1]
    o2 = board[square2][1][1]
    value = dice[colour][0]
    if x1 != 0.0 or o1 != 0.0:
        if x2 != 0.0 or o2 != 0.0:
            print("Error: One square must be empty for the entanglement move")
            return False
    if isColourFree(dice, colour):
        if value == 'X':
            if x1 != 0.0 or x2 != 0.0:
                print("Error: X can't entangle with X")
                return False
            if o1 == o2 == 0.0:
                print("Error: One square must have an O to entangle with X")
                return False
            if o1 != 0.0: # square1 contains O-die
                oColour = board[square1][1][2]
                oDieNum = board[square1][1][3]
                halveProb(board, dice, oColour, oDieNum, 'O') # Halves probability of O-die in square1
                place_die(board, dice, oColour, square2, o1/2) # Places a new die of the same colour and probability in square2
            elif o2 != 0.0: # square2 contains O-die
                oColour = board[square2][1][2]
                oDieNum = board[square2][1][3]
                halveProb(board, dice, oColour, oDieNum, 'O') # Halves probability of O-die in square2
                place_die(board, dice, oColour, square1, o2/2) # Places a new die of the same colour and probability in square1
            else: # Can hopefully never be reached
                print("Error: Unknown error 1")
                return False
        if value == 'O':
            if o1 != 0.0 or o2 != 0.0:
                print("Error: O can't entangle with O")
                return False
            if x1 == x2 == 0.0:
                print("Error: One square must have an X to entangle with O")
                return False
            if x1 != 0.0: # square1 contains X-die
                xColour = board[square1][0][2]
                xDieNum = board[square1][0][3]
                halveProb(board, dice, xColour, xDieNum, 'X') # Halves probability of X-die in square1
                place_die(board, dice, xColour, square2, x1/2) # Places a new die of the same colour and probability in square2
            elif x2 != 0.0: # square2 contains X-die
                xColour = board[square2][0][2]
                xDieNum = board[square2][0][3]
                halveProb(board, dice, xColour, xDieNum, 'X') # Halves probability of X-die in square2
                place_die(board, dice, xColour, square1, x2/2) # Places a new die of the same colour and probability in square1
            else: # Can hopefully never be reached
                print("Error: Unknown error 2")
                return False
        # Finally, place your dice:
        return place_die(board, dice, colour, square1, 0.5) and place_die(board, dice, colour, square2, 0.5)

#############################
#### MEASURING THE BOARD ####
#############################
def rolld4():
    return random.randint(1,4)

# board: [square0, ..., square8], with squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
def findBoardColours(board):
    boardColours = []
    for square in range(9):
        xColour = board[square][0][2]
        if xColour not in boardColours and xColour != 'empty':
            boardColours.append(xColour)
        oColour = board[square][1][2]
        if oColour not in boardColours and oColour != 'empty':
            boardColours.append(oColour)
    return boardColours

def observeColour(board, dice, colour, roll):
    # Dictionary "dice" contains colours = [value, die1, die2, die3, die4], each die = [position, probability]
    # board: [square0, ..., square8], with squarei = [[X, probX, colour, die number], [O, probO, colour, die number]]
    assert isinstance(colour, str) # Ensure that colour is a string and not an array (as previously)
    print("DEBUG observeColour: board = ")
    print(board)
    boardColours = findBoardColours(board)
    if colour not in boardColours:
        print("\nError: Colour not on board")
        return False
    if roll not in range(1,5):
        print("\nError: Roll not between 1 and 4")
        return False
    value = dice[colour][0]
    onBoard = [] # Dice of colour currently on board
    squares = [] # Squares on board with dice of colour
    for i in range(1,4):
        if dice[colour][i][0] != -1:
            onBoard.append(i)
            squares.append(dice[colour][i][0])
    totalProb = 0.0
    # check for unitarity
    for i in onBoard:
        totalProb += dice[colour][i][1]
    if totalProb != 1.0:
        print("\nError: Total probability is " + str(totalProb) + " =/= 1.")
        return False
    # make a list of four equal-probability outcomes
    possibilities = []
    for i in onBoard:
        for j in range(0,int(4*dice[colour][i][1])):
            possibilities.append([i,dice[colour][i][0]])
    if len(possibilities) != 4:
        print("\nError: Number of possibilities =/= 4.")
        return False
    print("DEBUG observeColour: possibilities = ")
    print(possibilities)
    print("DEBUG observeColour: roll = " + str(roll))
    measuredDie = possibilities[roll - 1][0]
    print("DEBUG observeColour: measuredDie = " + str(measuredDie))
    measuredSquare = possibilities[roll - 1][1]
    print("DEBUG observeColour: measuredSquare = " + str(measuredSquare))
    # Update colour:
    for die in onBoard:
        if die == measuredDie: # Give prob 1
            dice[colour][die][1] = 1.0
        else: # Take die off board
            dice[colour][die] = [-1, 0.0]
    # Update board:
    for square in squares:
        if square == measuredSquare:
            if value == 'X':
                # Collapse observed X state
                board[square][0] = ['X', 1.0, 'obsrv', -1]
                if board[square][1][1] != 0.0:
                    # Remove die of opposite value:
                    removeColour = board[square][1][2]
                    removeDie = board[square][1][3]
                    dice[removeColour][removeDie] = [-1, 0.0] # Take affected die off board
                    board[square][1] = ['O', 0.0, 'empty', -1] # Make square void of die
            if value == 'O':
                # Collapse observed O state
                board[square][1] = ['O', 1.0, 'obsrv', -1]
                if board[square][0][1] != 0.0:
                    # Remove die of opposite value:
                    removeColour = board[square][0][2]
                    removeDie = board[square][0][3]
                    dice[removeColour][removeDie] = [-1, 0.0] # Take affected die off board
                    board[square][0] = ['X', 0.0, 'empty', -1] # Make square void of die
        elif square != measuredSquare:
            if value == 'X':
                board[square][0] = ['X', 0.0, 'empty', -1] # Make square void of non-measured die
                if board[square][1][1] != 0.0:
                    # Double prob of die of opposite value:
                    doubleColour = board[square][1][2]
                    doubleDie = board[square][1][3]
                    dice[doubleColour][doubleDie][1] = 2*dice[doubleColour][doubleDie][1] # Double prob of die
                    board[square][1][1] = 2*board[square][1][1] # Double prob on square
            if value == 'O':
                board[square][1] = ['O', 0.0, 'empty', -1] # Make square void of non-measured die
                if board[square][0][1] != 0.0:
                    # Double prob of die of opposite value:
                    doubleColour = board[square][0][2]
                    doubleDie = board[square][0][3]
                    dice[doubleColour][doubleDie][1] = 2*dice[doubleColour][doubleDie][1] # Double prob of die
                    board[square][0][1] = 2*board[square][0][1] # Double prob
    print("\n" + colour + " " + str(value) + " die observed in square " + str(measuredSquare))
    return True

def measureBoard(board, dice):
    print("\nObserving board...")
    boardColours = findBoardColours(board)
    for colour in boardColours:
        roll = rolld4()
        observeColour(board, dice, colour, roll)
    return True

##########################
#### RATING THE BOARD ####
##########################

# Checks if X currently has a winning position
def canXWin(board):
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
def canOWin(board):
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
# To-do: Add fourth option "continue" if there are empty squares left?
def check_board(board):
    if canXWin(board):
        if canOWin(board):
            print("\nDraw!")
            return True
        else:
            print("\nX won!")
            return True
    elif canOWin(board):
        print("\nO won!")
        return True
    else:
        print("\nDraw!")
        return True

def print_menu():
    print("\n1: Make classical move")
    print("2: Make superposition move")
    print("3: Make entanglement move")
    print("4: Observe colour")
    print("5: Observe board")
    print("6: Finalize")
    print("0: Print current board")
    print("m: Menu")
    print("q: Quit")
    return True

#####################################
#### CALCULATE WIN PROBABILITIES ####
#####################################

# WIP!!
# list-copy-issue, solution found here: 
#https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
def enumerateBoards(board, dice, colours, n):
    print("\nDEBUG: n = " + str(n) + ", colours = ")
    print(colours)
    boards = []
    diceSets = []
    for i in range(4):
        #print("\nDEBUG: i = " + str(i))
        boards.append(copy.deepcopy(board)) 
        diceSets.append(copy.deepcopy(dice)) 
        #print("\nDEBUG: boards[i] PRE OBSERVING")
        #print(boards[i])
        observeColour(boards[i], dice[i], colours[n-1], i+1)
        #print("\nDEBUG: boards[i] POST OBSERVING")
        #print(boards[i])
        #print("DEBUG: END")
    #if n > 1:
    #    boards.append(enumerateBoards(board, colours, n-1)) # RECURSION!!
    #print(boards)
    return boards

# superpos_move(mainBoard, mainDice, 'turqs', 5, 6)
# superpos_move(mainBoard, mainDice, 'smoke', 2, 3)
# #mainBoard2 = copy.deepcopy(mainBoard)
# #observeColour(mainBoard, mainDice, 'turqs', 1)
# #observeColour(mainBoard2, 'turqs', 3) # ??? hvorfor er possibilities ulike mellom disse to?
# # SVAR: Fordi at de driver og redigerer på det globale dice-biblioteket... howtofix
# enumerateBoards(mainBoard, mainDice, ['turqs', 'smoke'], 2)

# WIP!!
def calculateProbs(board):
    boardColours = findBoardColours(board)
    numberOfColours = len(boardColours)
    enumerateBoards(board, boardColours, numberOfColours)
    for a in range(4):
        aboards.append(board)
        for colour in boardColours:
            observeColour(board, dice, colour, roll)
    bboards = []
    for b in range(4):
        bboards.append(aboards)
    cboards = []
    for c in range(4):
        cboards.append(bboards)
    dboards = []
    for d in range(4):
        dboards.append(cboards)
    eboards = []
    for e in range(4):
        eboards.append(dboards)
    fboards = []
    for f in range(4):
        fboards.append(eboards)
    gboards = []
    for g in range(4):
        gboards.append(fboards)
    hboards = []
    for h in range(4):
        hboards.append(gboards)
    boards = []
    for i in range(4):
        boards.append(hboards)
    #print(boards) # 4^9 = 262,144 boards
    #boardColours = findBoardColours(board)
    #for colour in boardColours:
    #    observeColour(boards[1], colour, 1)

#calculateProbs(mainBoard)

#######################
#### PLAY THE GAME ####
#######################

print("\nWelcome to TiqTaqToe (d4 version)!")
print_menu()
print_board(mainBoard)

while(True):
    action = input("\nWhat would you like to do? (m: Menu, q: Quit)\n> ")
    if action == "1":
        colour = input("\nWhich colour? (q: Back) \n(X: green/turqs/ocean/prple/sprkl) \n(O: yllow/ornge/smoke/blank)\n> ")
        if colour == "q" or colour == "Q":
            continue
        if colour not in allColours:
            print("\nError: Not a colour")
            continue
        square = input("\nWhere? (1-9, q: Back)\n> ")
        if square == "q" or square == "Q":
            continue
        if square not in allSquares:
            print("\nError: Not a square")
            continue
        square = int(square) - 1
        classic_move(mainBoard, mainDice, colour, square)
        print_board(mainBoard)
    elif action == "2":
        colour = input("\nWhich colour? (q: Back) \n(X: green/turqs/ocean/prple/sprkl) \n(O: yllow/ornge/smoke/blank)\n> ")
        if colour == "q" or colour == "Q":
            continue
        if colour not in allColours:
            print("\nError: Not a colour")
            continue
        square1 = input("\nWhere? (1-9, q: Back)\n> ")
        if square1 == "q" or square1 == "Q":
            continue
        if square1 not in allSquares:
            print("\nError: Not a square")
            continue
        square1 = int(square1) - 1
        square2 = input("\nWhere else? (1-9, q: Back)\n> ")
        if square2 == "q" or square2 == "Q":
            continue
        if square2 not in allSquares:
            print("\nError: Not a square")
            continue
        square2 = int(square2) - 1
        superpos_move(mainBoard, mainDice, colour, square1, square2)
        print_board(mainBoard)
    elif action == "3":
        colour = input("\nWhich colour? (q: Back)\n(X: green/turqs/ocean/prple/sprkl) \n(O: yllow/ornge/smoke/blank)\n> ")
        if colour == "q" or colour == "Q":
            continue
        if colour not in allColours:
            print("\nError: Not a colour")
            continue
        square1 = input("\nWhere? (1-9, q: Back)\n> ")
        if square1 == "q" or square1 == "Q":
            continue
        if square1 not in allSquares:
            print("\nError: Not a square")
            continue
        square1 = int(square1) - 1
        square2 = input("\nWhere else? (1-9, q: Back)\n> ")
        if square2 == "q" or square2 == "Q":
            continue
        if square2 not in allSquares:
            print("\nError: Not a square")
            continue
        square2 = int(square2) - 1
        entang_move(mainBoard, mainDice, colour, square1, square2)
        print_board(mainBoard)
    elif action == "4":
        colour = input("\nWhich colour? (q: Back) \n(X: green/turqs/ocean/prple/sprkl) \n(O: yllow/ornge/smoke/blank)\n> ")
        if colour == "q" or colour == "Q":
            continue
        if colour not in allColours:
            print("\nError: Not a colour")
            continue
        roll = rolld4()
        observeColour(mainBoard, mainDice, colour, roll)
        print_board(mainBoard)
    elif action == "5":
        measureBoard(mainBoard)
        print_board(mainBoard)
    elif action == "6":
        measured = True
        boardColours = findBoardColours(mainBoard)
        for colour in allColours:
            if colour in boardColours:
                measured = False
        if not measured:
            print("\nError: Board not fully observed")
            continue
        check_board(mainBoard)
        break
    elif action == "0":
        print_board(mainBoard)
    elif action == "m" or action == "M":
        print_menu()
    elif action == "q" or action == "Q":
        print("\nBye!")
        break
    else:
        print("\nError: Invalid input")
