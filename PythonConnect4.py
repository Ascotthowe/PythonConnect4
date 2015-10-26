import turtle

theBoardList = []
squaresize = 50
whichturn = 1
redCounterx = [0, 0, 0, 0, 0, 0]
blackCounterx = [0, 0, 0, 0, 0, 0]
winner = False
userXpos = 0
BORDER = 10
WINDOWWIDTH = 6*squaresize+BORDER
WINDOWHEIGHT = 7*squaresize+BORDER
BROSEF = turtle.Turtle()

# defines a list of lists 6x7 to create the game board and store the moves
def createBoardArray():
    for x in range(6):
        theBoardList.append([0, 0, 0, 0, 0, 0, 0])


# toggles which player is to go next
def changeTurn(turn):
    if turn == 1:
        print("Whichturn is 1, now it's player 2's turn")
        turn = 2
    else:
        print("Whichturn is not 1, it must be player 1's turn")
        turn = 1


# Called after each turn to determine if either player has won
def checkBoard():
    global redCounterx
    global blackCounterx
    global redCountery
    global blackCountery
    global winner
    winner = False
    # this will be used to store red count for each column
    redCounterx = [0, 0, 0, 0, 0, 0]
    # this will be used to store black count for each column
    blackCounterx = [0, 0, 0, 0, 0, 0]
    # this will be used to store red count for each row
    redCountery = [0, 0, 0, 0, 0, 0]
    # this will be used to store black count for each row
    blackCountery = [0, 0, 0, 0, 0, 0]
    for x in range(6):  # we loop through the whole board
        # print(redCounterx)
        # print(blackCounterx)
        for y in range(7):
            if theBoardList[x][y] == 1:  # this is a red cell
                # this counts red cells vertically
                redCounterx[x] = redCounterx[x]+1
                blackCounterx[x] = 0
                # this counts red cells horizontally
                redCountery[y] = redCountery[y]+1
                blackCountery[y] = 0
            elif theBoardList[x][y] == 2:  # this is a black cell
                # this counts black cells vertically
                blackCounterx[x] = blackCounterx[x]+1
                redCounterx[x] = 0
                # this counts black cells horizontally
                blackCountery[y] = blackCountery[y]+1
                redCountery[y] = 0
            else:
                break
        if redCounterx[x] >= 4:  # Red won
            print("Connect 4! Vertical")
            winner = True
            drawFinish("Red", "Red wins!")
            break
        if blackCounterx[x] >= 4:  # black won
            print("Connect 4! Vertical")
            winner = True
            drawFinish("Black", "Black wins!")
            break
        if redCountery[y] >= 4:
            print("Connect 4! Horizontal")
            winner = True
            drawFinish("Red", "Red Wins!")
            break
        if blackCountery[y] >= 4:
            print("Connect 4! Horizontal")
            winner = True
            drawFinish("Black", "Black wins!")
            break


def checkClick(x, y):
    global winner
    global userXpos
    global whichturn
    userXpos = 0
    userXpos = (x)/50
    userXpos = int(userXpos)
    if winner:
        print("The game is already over!")
        return
    if x < 0:
        return
    # userXpos = int(input("enter the column you want to drop in:"))

    # We know what column we're dropping in,
    # now we need to check with row is free
    for y in range(7):
        # 0 means the column is not occupied
        if theBoardList[userXpos][y] == 0:
            drawMove(userXpos, y, whichturn)
            #  We found an unoccupied cell,
            #  so we draw it and set it to 1 or 2 on the board list
            theBoardList[userXpos][y] = whichturn
            checkBoard()
            if whichturn == 1:
                print("Player 2's turn")
                whichturn = 2
            else:
                print("Player 1's turn")
                whichturn = 1
            break
        else:  # we haven't found an unoccupied cell yet, keep iterating
            continue


# draws a 50x50 square at the current location
def drawSquare(piecesize):
    square.forward(piecesize)
    square.left(90)
    square.forward(piecesize)
    square.left(90)
    square.forward(piecesize)
    square.left(90)
    square.forward(piecesize)
    square.left(90)
    # square.forward(piecesize)


# draws a move
# x: column, y: row,
# turn: determines which color is drawn
def drawMove(x, y, turn):
    if turn == 1:
        color = "red"
    else:
        color = "black"
    posx = x*squaresize
    posy = y*squaresize
    square.goto(posx, posy)
    square.fillcolor(color)
    square.begin_fill()
    drawSquare(50)
    square.end_fill()

def drawwelcome():
        BROSEF.penup()
        BROSEF.goto(50,325)    
        BROSEF.color("blue")
        BROSEF.pensize(3)
        BROSEF.write ('Welcome to Connect 4!', font = ('Calligrapher', 38, 'bold'))

def drawFinish(color, message):
    wn.clear()
    BROSEF.goto(50,200)
    BROSEF.color(color)
    BROSEF.pensize(3)
    BROSEF.write (message, font = ('Calligrapher', 38, 'bold'))
        
# Prints 7x6 game board of squares
def createGameBoard():
    for x in range(6):
        for y in range(7):
            posx = (x*squaresize)
            posy = (y*squaresize)
            square.speed(0)
            square.penup()
            square.goto(posx, posy)
            square.pendown()
            drawSquare(squaresize)
            square.penup()

# setting up the window and turtle
wn = turtle.Screen()
# turtle.setup(width=400, height=400, startx=0 , starty=0)
square = turtle.Turtle()

print("Welcome to Connect4")
wn.setworldcoordinates(0-BORDER, 0-BORDER, WINDOWWIDTH, WINDOWHEIGHT)
createGameBoard()
createBoardArray()
drawwelcome()
wn.onscreenclick(checkClick)
