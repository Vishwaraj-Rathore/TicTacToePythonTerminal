import random

currentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
positionsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
userChoice = 1
a = [1, 4, 7]
b = [1, 3, 5]
playerChoice = [" ", " "]

def PrintBoard():
    global currentBoard
    for i in range(3):
        for j in range(3):
            print("",currentBoard[i][j], "|" if j!=2 else "", end="")
        print("\n - | - | - " if i!=2 else "")

def UserInput():
    global userChoice, positionsLeft
    while(True):
        userChoice = input("Enter position number: ")
        if(userChoice.isnumeric()):
            userChoice = int(userChoice)
            if(userChoice > 9 or userChoice < 0):
                print("Position chosen is out of bounds, please enter a valid position.")
                continue
            elif(userChoice not in positionsLeft and userChoice!= 0):
                print("Position already taken, please enter a valid position.")
                continue
            else:
                break
        else:
            print("Please enter a valid position value.")
            continue

def GetRowNum(k):
    if(k < 4):
        return 0
    elif(k < 7):
        return 1
    else:
        return 2

def GetAxisForInput(k):
    global a, b
    rowNumber = GetRowNum(k)
    yAxis = k - a[rowNumber]
    xAxis = a[rowNumber] - b[rowNumber]
    return xAxis, yAxis

def PlayerMove():
    global userChoice, currentBoard, playerChoice
    xAxis, yAxis = GetAxisForInput(userChoice)
    currentBoard[xAxis][yAxis] = playerChoice[1]
    positionsLeft.remove(userChoice)

def PlayerChoice():
    while(True):
        choiceInput = input("Do you wanna be X or O: ").lower()
        if(choiceInput == "x" or choiceInput == "o"):
            playerChoice[1] = choiceInput
            if(choiceInput == "x"):
                playerChoice[0] = "o"
            else:
                playerChoice[0] = "x"
                ComputerMove()
            break
        else:
            print("Entered choice is invalid, please choose either X or O")
            continue

def ComputerMove():
    global positionsLeft, currentBoard, playerChoice
    computerChoice = random.choice(positionsLeft)
    xAxis, yAxis = GetAxisForInput(computerChoice)
    currentBoard[xAxis][yAxis] = playerChoice[0]
    positionsLeft.remove(computerChoice)

def BoardCheck():
    global positionsLeft
    if(len(positionsLeft) == 0):
        return True
    else:
        return False

PlayerChoice()

while(True):
    if(BoardCheck()):
        PrintBoard()
        print("No more positions left to play")
        break
    PrintBoard()
    UserInput()
    if(userChoice == 0):
        break
    PlayerMove()
    if(BoardCheck()):
        PrintBoard()
        print("No more positions left to play")
        break
    ComputerMove()