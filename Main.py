import random

currentBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
positionsLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
userChoice = 1
a = [1, 4, 7]
b = [1, 3, 5]
playerChoice = [" ", " "]
winner = 2
computerWinMovePref = 0
computerBlockMovePref = 0

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
    global positionsLeft, currentBoard, playerChoice, computerWinMovePref, computerBlockMovePref
    if(computerWinMovePref == 0 and computerBlockMovePref == 0):
        computerChoice = random.choice(positionsLeft)
    else:
        if(computerWinMovePref != 0):
            computerChoice = computerWinMovePref
        else:
            computerChoice = computerBlockMovePref
    xAxis, yAxis = GetAxisForInput(computerChoice)
    currentBoard[xAxis][yAxis] = playerChoice[0]
    positionsLeft.remove(computerChoice)
    computerWinMovePref = computerBlockMovePref = 0

def BoardCheck():
    global positionsLeft
    if(len(positionsLeft) == 0):
        return True
    else:
        return False

def GetItemAtPosition(k):
    global currentBoard
    xAxis, yAxis = GetAxisForInput(k)
    return currentBoard[xAxis][yAxis]

def HorizontalCheck():
    global winner, playerChoice, computerWinMovePref, computerBlockMovePref
    for i in range(1, 8, 3):
        counterComputer = 0
        counterPlayer = 0
        positionOfBlank = 0
        for j in range(3):
            a = i+j
            if(GetItemAtPosition(a) == playerChoice[0]):
                counterComputer += 1
            elif(GetItemAtPosition(a) == playerChoice[1]):
                counterPlayer += 1
            else:
                positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2):
            computerBlockMovePref = positionOfBlank
    return False

def VerticalCheck():
    global winner, playerChoice, computerWinMovePref, computerBlockMovePref
    for i in range(1, 4):
        counterComputer = 0
        counterPlayer = 0
        positionOfBlank = 0
        for j in range(0, 7, 3):
            a = i+j
            if(GetItemAtPosition(a) == playerChoice[0]):
                counterComputer += 1
            elif(GetItemAtPosition(a) == playerChoice[1]):
                counterPlayer += 1
            else:
                positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2):
            computerBlockMovePref = positionOfBlank
    return False

def DiagonalCheck():
    global winner, playerChoice, computerWinMovePref, computerBlockMovePref
    for i in [1,3]:
        counterComputer = 0
        counterPlayer = 0
        positionOfBlank = 0
        if(i == 1):
            for j in range(0, 9, 4):
                a = i+j
                if(GetItemAtPosition(a) == playerChoice[0]):
                    counterComputer += 1
                elif(GetItemAtPosition(a) == playerChoice[1]):
                    counterPlayer += 1
                else:
                    positionOfBlank = a
        else:
            for j in range(0, 5, 2):
                a = i+j
                if(GetItemAtPosition(a) == playerChoice[0]):
                    counterComputer += 1
                elif(GetItemAtPosition(a) == playerChoice[1]):
                    counterPlayer += 1
                else:
                    positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2):
            computerBlockMovePref = positionOfBlank
    return False

def WinnerCheck():
    global winner
    if(HorizontalCheck()):
        if(winner == 0):
            PrintBoard()
            print("Computer Won, better luck next time!")
            return True
        elif(winner == 1):
            PrintBoard()
            print("Congratulations, You won!")
            return True
    elif(VerticalCheck()):
        if(winner == 0):
            PrintBoard()
            print("Computer Won, better luck next time!")
            return True
        elif(winner == 1):
            PrintBoard()
            print("Congratulations, You won!")
            return True
    elif(DiagonalCheck()):
        if(winner == 0):
            PrintBoard()
            print("Computer Won, better luck next time!")
            return True
        elif(winner == 1):
            PrintBoard()
            print("Congratulations, You won!")
            return True
    elif(BoardCheck()):
        PrintBoard()
        print("It's a draw!")
        return True
    else:
        return False

PlayerChoice()

while(True):
    if(WinnerCheck()):
        break
    PrintBoard()
    UserInput()
    if(userChoice == 0):
        break
    PlayerMove()
    if(WinnerCheck()):
        break
    ComputerMove()