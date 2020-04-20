global textmove, move, debug

import sys

theBoard = {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }

debug = True

player1Name = "Player 1"

player1Piece = "0"

player2Name = "Player 2"

player2Piece = "X"

currentPlayerName = player1Name

currentPlayerPiece = player1Piece

currentPlayerName1 = player2Name

currentPlayerPiece1 = player2Piece




def printBoard(theBoard):
    print(theBoard[7] + '|' + theBoard[8] + '|' + theBoard[9])
    print('-+-+-')
    print(theBoard[4] + '|' + theBoard[5] + '|' + theBoard[6])
    print('-+-+-')
    print(theBoard[1] + '|' + theBoard[2] + '|' + theBoard[3])



def key():
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')



def checkWin(x,y,z):
    #if debug: print("checkWin")
    if theBoard[z] == player2Piece:
        if theBoard[x] == theBoard[y] == theBoard[z]:
            print('Game Over')
            print(player2Piece + " won")
            currentPlayerPiece
            sys.exit()
                
        elif theBoard[z] == player1Piece:
            if theBoard[x] == theBoard[y] == theBoard[z]:
                print('Game Over')
                print(player1Piece + " won")
                currentPlayerPiece
                sys.exit()
            
                
def placeOnGrid(currentPlayerPiece):
    #if debug: print("placeOnGrid")
    print("It's your turn,  " + currentPlayerPiece + " Move to which place?")
    printBoard(theBoard)
    textmove= input()
    move= int(textmove)
    theBoard[move]=currentPlayerPiece
    currentPlayerPiece = 'X'

def noFunnyBusiness():
    isAValidMove = true
    
    if move > '9':
        print('Sorry that is not a square on the board. Please try again')
        print("It's your turn," + currentPlayerPiece + " Move to which place?")
        printBoard(theBoard)
        textmove= input()
        move= int(textmove)
        theBoard[move]=currentPlayerPiece
    if move < '1':
        print('Sorry that is not a square on the board. Please try again')
        print("It's your turn," + currentPlayerPiece + " Move to which place?")
        printBoard(theBoard)
        textmove= input()
        move= int(textmove)
        theBoard[move]=currentPlayerPiece
    if move == '':
        print('Sorry that is not a square on the board. Please try again')
        currentPlayerPiece= currentPlayerPiece
        print("It's your turn," + currentPlayerPiece + " Move to which place?")
        printBoard(theBoard)
        textmove= input()
        move= int(textmove)
        theBoard[move]=currentPlayerPiece
        currentPlayerPiece = player2Piece
def fullCheckWin():
    checkWin(7,8,9)
    checkWin(4,5,6)
    checkWin(1,2,3)
    checkWin(7,4,1)
    checkWin(8,5,2)
    checkWin(9,6,3)
    checkWin(9,5,1)
    checkWin(7,5,3)

def syntaxError():
    print('Sorry that is not a square on the board. Please try again')
    currentPlayerPiece= currentPlayerPiece
    print("It's your turn," + currentPlayerPiece + " Move to which place?")
    printBoard(theBoard)
    textmove= input()
    move= int(textmove)
    theBoard[move]=currentPlayerPiece

        
def executeTurn(currentTurn):    
    placeOnGrid(currentTurn)
    everythingCheck()
    


def CheckGame(x,y,z):
    if theBoard[x] == player2Piece:
        if theBoard[y] == player2Piece:
            if theBoard[z] == player2Piece:
                print('Game Over!' + player2Piece +  'won!')
                sys.exit()
    if theBoard[x] == player1Piece:
        if theBoard[y] == player1Piece:
            if theBoard[z] == player1Piece:
                print('Game Over!' + player1Piece +  'won!')
                sys.exit()                   
def everythingCheck():
    CheckGame(1,2,3)
    CheckGame(4,5,6)
    CheckGame(7,8,9)
    CheckGame(1,4,7)
    CheckGame(2,5,8)
    CheckGame(3,6,9)
    CheckGame(7,5,3)
    CheckGame(9,5,1)
    

def allTurns():
    executeTurn('0')
    executeTurn('X')
    executeTurn('0')
    executeTurn('X')
    executeTurn('0')
    executeTurn('X')
    executeTurn('0')
    executeTurn('X')
    executeTurn('0')

    
def game():
    
    allTurns()
    while True:
        everythingCheck()
    while True:
        noFunnyBusiness()

#Ask Player1 where they want to move, Check for a valid move, Put the move into the board
#Check for win
#Switch Players
#Repeat    

#isValid = CheckMove(currentMove)
#if isValid:

                    
def FullGame():
    key()
    game()
       
    


FullGame()
sys.exit()
