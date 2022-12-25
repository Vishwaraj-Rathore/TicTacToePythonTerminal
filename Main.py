currentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def printBoard():
    for i in range(3):
        for j in range(3):
            print("",currentBoard[i][j], "|" if j!=2 else "", end="")
        print("\n - | - | - " if i!=2 else "")

printBoard()