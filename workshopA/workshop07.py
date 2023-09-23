import random

def Randomnumber():
    random_number = random.randint(1, 100)
    return random_number

def InputNum():
    guess_number = int(input("Enter number:"))
    return guess_number

def CheckNum(random_number, guess_number):
    print("-----------------------------")
    print("        GAME BINGO           ")
    print("-----------------------------")
    if guess_number == random_number:
        print("----------YAY----------------")
        print("-Correct, You are the winner-")
    else:
        print("-----  Not correct  !!! -----")
        print("-----  Try again    !!! -----")

def showResult(random_number):
    print(f"Random Number is: {random_number}")

random_number = Randomnumber()
guess_number = InputNum()
CheckNum(random_number, guess_number)
showResult(random_number)