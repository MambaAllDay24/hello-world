import sys

import randint() from random

theBoard = {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }


player1Name = "Player 1"

player1Piece = "O"

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
    return


def key():
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')
    return



def checkWin(x,y,z):
        if theBoard[z] == 'X':
            if theBoard[x] == theBoard[y] == theBoard[z]:
                print('Game Over')
                print("X won")
                return
        elif theBoard[z] == '0':
            if theBoard[x] == theBoard[y] == theBoard[z]:
                print('Game Over')
                print("0 won")
                return
            
                

def placeOnGrid(currentPlayerPiece):
    turn= currentPlayerPiece
    print("It's your turn, " + turn + " Move to which place?")
    printBoard(theBoard)
    textmove= input()
    move= int(textmove)
    theBoard[move]=turn
    turn = 'X'
    return


def fullCheckWin():
    checkWin(7,8,9)
    checkWin(4,5,6)
    checkWin(1,2,3)
    checkWin(7,4,1)
    checkWin(8,5,2)
    checkWin(9,6,3)
    checkWin(9,5,1)
    checkWin(7,5,3)
    return


        
def executeTurn():    
    placeOnGrid('0')
    placeOnGrid('X')
    return

def CheckGame(x,y,z):
    if theBoard[z] == 'X':
        if theBoard[x] == theBoard[y] == theBoard[z]:
                print('Game Over! X Won!')
                sys.exit()
    elif theBoard[z] == '0':
        if theBoard[x] == theBoard[y] == theBoard[z]:
                print('Game Over! 0 Won!')
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
    return


    
def game():
    for x in range(0,5):
        executeTurn()
        if x == 5:
             placeOnGrid('0')
        while x >= 2:
            everythingCheck()
            
    return


                    
def FullGame():
    key()
    game()
    fullCheckWin()
    return

                
FullGame()
sys.exit()
