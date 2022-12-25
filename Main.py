currentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
positionsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
userChoice = 1

def PrintBoard():
    for i in range(3):
        for j in range(3):
            print("",currentBoard[i][j], "|" if j!=2 else "", end="")
        print("\n - | - | - " if i!=2 else "")

def UserInput():
    while(True):
        userChoice = input("Enter position number: ")
        if(userChoice.isnumeric()):
            userChoice = int(userChoice)
            if(userChoice > 9 or userChoice < 0):
                print("Position chosen is out of bounds, please enter a valid position.")
                continue
            elif(userChoice not in positionsLeft):
                print("Position already taken, please enter a valid position.")
                continue
            else:
                break
        else:
            print("Please enter a valid position value.")
            continue

UserInput()
PrintBoard()