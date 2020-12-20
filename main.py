# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

# Switch case
def mult():
    print("Value is multiple")

def div():
    print("Value is multiple")

def greater():
    print("Value is greater")

def smaller():
    print("Value is smaller")

# map the inputs to the function blocks
options = {0 : mult,
           1 : div,
           2 : greater,
           3 : smaller,
}


def giveHint(guess,value):
    #options = ["mult", "div" , "greater", "smaller"]
    options[random.randint(0,3)]()


def isEqual(guess: int,value: int):
    if int(guess) == value:
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tries = 5
    #print("Enter value:")

    #value = input()
    value = random.randint(1,20)
    print("Value is:", value)


    while tries > 0:
        print("Enter your guess between 1-20")
        print("Check this")
        guess = input()
        print(isEqual(guess,value))
        if isEqual(guess,value):
            print("Found")
            break
        else:
            giveHint(guess,value)
            tries-= 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
