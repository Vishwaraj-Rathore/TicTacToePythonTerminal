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
difficultyChoice = " "
corners = [1, 3, 7, 9]
squares = [2, 4, 6, 8]
counterHardXMove = 0
compHardXMoveTempPosition = 0
compXWay = 0
cornerAdjacentSigns = [[1, +1, +1], [3, -1, +1], [7, +1, -1], [9, -1, -1]]

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
    global difficultyChoice
    while(True):
        choiceInput = input("Do you wanna be X or O: ").lower()
        if(choiceInput == "x" or choiceInput == "o"):
            playerChoice[1] = choiceInput
            if(choiceInput == "x"):
                playerChoice[0] = "o"
            else:
                playerChoice[0] = "x"
            while(True):
                difficultyChoice = input("Please choose difficulty { easy or hard }: ").lower()
                if(difficultyChoice == "easy" or difficultyChoice == "hard"):
                    ComputerMove() if difficultyChoice == "easy" else ComputerMoveHardX()
                    break
                else:
                    print("Entered difficutly is invalid, please choose either easy or hard")
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
            elif(GetItemAtPosition(a) == " "):
                positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2 and positionOfBlank != 0):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2 and positionOfBlank != 0):
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
            elif(GetItemAtPosition(a) == " "):
                positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2 and positionOfBlank != 0):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2 and positionOfBlank != 0):
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
                elif(GetItemAtPosition(a) == " "):
                    positionOfBlank = a
        else:
            for j in range(0, 5, 2):
                a = i+j
                if(GetItemAtPosition(a) == playerChoice[0]):
                    counterComputer += 1
                elif(GetItemAtPosition(a) == playerChoice[1]):
                    counterPlayer += 1
                elif(GetItemAtPosition(a) == " "):
                    positionOfBlank = a
        if(counterComputer == 3):
            winner = 0
            return True
        elif(counterPlayer == 3):
            winner = 1
            return True
        elif(counterComputer == 2 and positionOfBlank != 0):
            computerWinMovePref = positionOfBlank
        elif(counterPlayer == 2 and positionOfBlank != 0):
            computerBlockMovePref = positionOfBlank
    return False

def WinnerCheck():
    global winner, computerBlockMovePref, computerWinMovePref
    computerWinMovePref = 0
    computerBlockMovePref = 0
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

def ComputerMoveHardX():
    global squares, computerWinMovePref, computerBlockMovePref, corners, positionsLeft, counterHardXMove, playerChoice, currentBoard, compHardXMoveTempPosition, difficultyChoice, compXWay
    options = Intersection(corners, positionsLeft)
    if(computerWinMovePref == 0 and computerBlockMovePref == 0):
        if(counterHardXMove == 0):
            computerChoice = random.choice(options)
            xAxis, yAxis = GetAxisForInput(computerChoice)
            currentBoard[xAxis][yAxis] = playerChoice[0]
            positionsLeft.remove(computerChoice)
            compHardXMoveTempPosition = computerChoice
            counterHardXMove += 1
            return
        elif(counterHardXMove == 1):
            if(GetItemAtPosition(5) == "o" ):
                compXWay = 1
                xAxis, yAxis = GetAxisForInput(DiagnolOpposite(compHardXMoveTempPosition))
                positionsLeft.remove(DiagnolOpposite(compHardXMoveTempPosition))
                currentBoard[xAxis][yAxis] = playerChoice[0]
                compHardXMoveTempPosition = DiagnolOpposite(compHardXMoveTempPosition)
                counterHardXMove += 1
                return
            for i in corners:
                if(GetItemAtPosition(i) == "o"):
                    compXWay = 2
                    computerChoice = random.choice(options)
                    xAxis, yAxis = GetAxisForInput(computerChoice)
                    currentBoard[xAxis][yAxis] = playerChoice[0]
                    positionsLeft.remove(computerChoice)
                    compHardXMoveTempPosition = computerChoice
                    counterHardXMove += 1
                    return
            ad1, ad2 = GetAdjacents(compHardXMoveTempPosition)
            if(GetItemAtPosition(ad1) == "o" or GetItemAtPosition(ad2) == "o"):
                compXWay = 3
                for i in options:
                    if(GetItemAtPosition(i) == " "):
                        ad1, ad2 = GetAdjacents(i)
                        if(GetItemAtPosition(ad1) == " " and GetItemAtPosition(ad2) == " "):
                            if(i != DiagnolOpposite(compHardXMoveTempPosition)):
                                xAxis, yAxis = GetAxisForInput(i)
                                currentBoard[xAxis][yAxis] = playerChoice[0]
                                positionsLeft.remove(i)
                                compHardXMoveTempPosition = i
                                counterHardXMove += 1
                                return
            ad1, ad2 = GetAdjacents(DiagnolOpposite(compHardXMoveTempPosition))
            if(GetItemAtPosition(ad1) == "o" or GetItemAtPosition(ad2) == "o"):
                compXWay = 4
                for i in options:
                    if(GetItemAtPosition(i) == " "):
                        ad1, ad2 = GetAdjacents(i)
                        if(GetItemAtPosition(ad1) == " " and GetItemAtPosition(ad2) == " "):
                            xAxis, yAxis = GetAxisForInput(i)
                            currentBoard[xAxis][yAxis] = playerChoice[0]
                            positionsLeft.remove(i)
                            compHardXMoveTempPosition = i
                            counterHardXMove += 1
                            return
        elif(counterHardXMove == 2):
            if(compXWay == 1):
                for i in corners:
                    if(GetItemAtPosition(i) == "o"):
                        xAxis, yAxis = GetAxisForInput(DiagnolOpposite(i))
                        positionsLeft.remove(DiagnolOpposite(i))
                        currentBoard[xAxis][yAxis] = playerChoice[0]
                        compHardXMoveTempPosition = DiagnolOpposite(i)
                        counterHardXMove += 1
                        return
            elif(compXWay == 2):
                    computerChoice = random.choice(options)
                    xAxis, yAxis = GetAxisForInput(computerChoice)
                    currentBoard[xAxis][yAxis] = playerChoice[0]
                    positionsLeft.remove(computerChoice)
                    compHardXMoveTempPosition = computerChoice
                    counterHardXMove += 1
                    return
            elif(compXWay == 3):
                for i in options:
                    if(GetItemAtPosition(i) == " "):
                        ad1, ad2 = GetAdjacents(i)
                        if(GetItemAtPosition(ad1) == " " and GetItemAtPosition(ad2) == " "):
                            xAxis, yAxis = GetAxisForInput(i)
                            currentBoard[xAxis][yAxis] = playerChoice[0]
                            positionsLeft.remove(i)
                            compHardXMoveTempPosition = i
                            counterHardXMove += 1
                            return
            elif(compXWay == 4):
                xAxis, yAxis = GetAxisForInput(5)
                currentBoard[xAxis][yAxis] = playerChoice[0]
                positionsLeft.remove(5)
                compHardXMoveTempPosition = 5
                counterHardXMove += 1
                return
    else:
        counterHardXMove += 1
        ComputerMove()
        return

def Intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def DiagnolOpposite(k):
    if(k == 1):
        return 9
    elif(k == 3):
        return 7
    elif(k == 9):
        return 1
    elif(k == 7):
        return 3

def GetAdjacents(k):
    global cornerAdjacentSigns
    for i in range(4):
        if(cornerAdjacentSigns[i][0] == k):
            ad1 = k + 1*(cornerAdjacentSigns[i][1])
            ad2 = k + 3*(cornerAdjacentSigns[i][2])
            return ad1, ad2

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
    if(difficultyChoice == "easy"):
        ComputerMove()
    elif(difficultyChoice == "hard" and playerChoice[0] == "x"):
        ComputerMoveHardX()