import numpy as np

gameBoard = np.array([['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']])

print(gameBoard  , "\n")

gameBoard[0,0] = 'X'

gameBoard[2,1] = 'O'

def printBoard():
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard)):
            print(gameBoard[i,j], end = " ")
        print()

def choosePlacement():
    print("Where to change?")
    playerChoice = input()
    print(playerChoice)
    
    
choosePlacement()    
printBoard()