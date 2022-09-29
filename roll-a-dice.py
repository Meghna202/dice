# Program to simulate the rolling odf a dice

# importing the random module
import random

# Get user input
userInput = input("Do you want to roll a dice? (Y or N) ")
while (userInput == "Y" or userInput == "y"):
    no = random.randint(1, 6)
    # Edge of the dice
    print("~~~~~~~~~~~")
    # First row
    if (no == 1):
        print("[         ]")
    elif (no == 2 or no == 3):
        print("[       * ]")
    else:
        print("[ *     * ]")   
    # Second Row
    if (no == 1 or no == 3 or no == 5):
        print("[    *    ]")
    elif (no == 6):
        print("[ *     * ]")
    else:
        print("[         ]")
    # Third Row
    if (no == 1):
        print("[         ]")
    elif (no == 2 or no == 3):
        print("[ *       ]")
    else:
        print("[ *     * ]")  
    #Edge of the dice  
    print("~~~~~~~~~~~")
    userInput = input("Do you want to roll again? (Y or N) ")
print("Thank you for playing with us!!!")