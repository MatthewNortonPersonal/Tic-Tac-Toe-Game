# This program is going to allow the user to play a two-player game of tic-tac-toe.
# I will try to add more features over time, but for now, that is going to be the main feature.

# Grid Appearance
# 
#  O |   |  
# ---|---|---
#    | X | 
# ---|---|---
#    |   |   
# 

import random

# Function to display the board depending on states of all of the cells. "positions" is a 9-element list.
def displayBoard(positions):
    
    for i in range(3):
        print(" " + positions[i], positions[i + 1], positions[i + 2], sep=" | ")

        # Prints the horizontal divider lines only twice
        if i < 2:
            print("---|---|---")

# This prompts the user with the gamemodes that they can select from.
# It returns a numerical value that corresponds with some gamemode. (1-3 = singleplayer, 4 = multiplayer)
def displayGamemodes():
    print("What mode would you like to play?")
    # \n is to separate the first message and the modes with an empty line as well as to separate the modes with the prompt
    print("\nSingleplayer: 1")
    print("Multiplayer: 2\n")

    # This is set to 0 to indicate that a mode hasn't been chosen.
    # It will not change until the user inputs an integer, and the while loop detects if the user input either 1 or 2 (valid inputs)
    mode = 0

    while mode not in [1, 2]:
        try:
            mode = int(input("Enter the number that corresponds with the mode you'd like to play: "))
            
            if mode not in [1, 2]:
                print("\nInvalid input--please enter either 1 or 2.\n")
        except:
            print("\nInvalid input--please enter an integer.\n")
    
    # If singleplayer, the user chooses the AI level.
    if mode == 1:
        print("\nGamemode chosen: Singleplayer\n")
        print("What level of AI would you like to play against?")
        print("\nLevel 1: Easy")
        print("Level 2: Medium")
        print("Level 3: Hard\n")
        # level indicates the AI difficulty level
        level = 0

        while level not in [1, 2, 3]:
            try:
                level = int(input("Enter the number that corresponds with the AI level you'd like to play against: "))

                if level not in [1, 2, 3]:
                    print("\nInvalid input--please enter a number between 1 and 3.\n")
            except:
                print("\nInvalid input--please enter an integer.\n")
        
        # This list stores the names of the AI levels with the index of each element corresponding to the number of the level.
        aiLevels = ["N/A", "Easy", "Medium", "Hard"]

        print("\nAI level chosen: " + aiLevels[level] + "\n")

        return level # 1 = AI level 1, 2 = AI level 2, 3 = AI level 3
        
    # If multiplayer  
    if mode == 2:
        print("\nGamemode chosen: Multiplayer\n")
        
        return 4 # 4 = multiplayer





# MAIN #

# This was used as a way to test the displayBoard function.
# displayBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"])

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Welcome message for the game
displayBoard(board)

print("Welcome to Tic Tac Toe!\n")
displayGamemodes()
