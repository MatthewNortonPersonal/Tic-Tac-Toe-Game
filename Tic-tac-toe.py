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

# imports
import random
import time

# Functions

# Function to display the board depending on states of all of the cells. "positions" is a 9-element list.
# The elements of the list should be strings, but I added the conversions just in case.
def displayBoard(positions):
    print("\n")
    for i in range(3):
        print(" " + str(positions[3 * i]), str(positions[3 * i + 1]), str(positions[3 * i + 2]), sep=" | ")

        # Prints the horizontal divider lines only twice
        if i < 2:
            print("---|---|---")
    print("\n")

# This prompts the user with the gamemodes that they can select from.
# It also returns a numerical value that corresponds with some gamemode. (1-3 = singleplayer, 4 = multiplayer)
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

# Location is an integer while symbol is a string. The location is where the move is being done and the symbol is "X" or "O"
# board is simply the list that holds the information about the cells on the board
def move(board, location, symbol):
    # If the board location is already occupied, it will not replace the symbol there. If it is empty, then it will replace that element in the list.
    if board[location] != " ":
        print("\nInvalid move--someone has already played there.")
        return False # returns False if the move was unsuccessful
    else:
        board[location] = symbol
        return True # returns True if the move was successful

# Simple function. It just prints a message saying that the input to it has won the game (input should be a string)
def presentWinner(symbol):
    print(symbol + " has won the game!")

# This function detects if there is a winning condition on the board and finishes the game if that is the case.
def detectWin(board):

    # 2D array that holds arrays that indicate the indices of the locations for the winning conditions
    conditions = [
        # Horizontal conditions
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        # Verical conditions
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        
        # Diagonal conditions
        [0, 4, 8],
        [2, 4, 6]
    ]

    for condition in conditions:
        cell1, cell2, cell3 = condition # This assigns cell1, cell2, and cell3 to the first, second, and third elements of condition respectfully.
        if (board[cell1] == board[cell2]) and (board[cell2] == board[cell3]) and (board[cell1] != " "):
            presentWinner(board[cell1])
            return True # The function returns true if there is a winner
    return False # The function returns false if there is not a wineer with the current board. This only happens when all of the conditions have been checked.

    # Former solution vvvv

    # # Horizontal winning conditions
    # if (board[0] == board[1]) and (board[1] == board[2]) and (board[0] != " "):
    #     presentWinner(board[0])
    # elif (board[3] == board[4]) and (board[4] == board[5]) and (board[3] != " "):
    #     presentWinner(board[3])
    # elif (board[6] == board[7]) and (board[7] == board[8]) and (board[6] != " "):
    #     presentWinner(board[6])
    
    # # Vertical winning conditions
    # elif (board[0] == board[3]) and (board[3] == board[6]) and (board[0] != " "):
    #     presentWinner(board[0])
    # elif (board[1] == board[4]) and (board[4] == board[7]) and (board[1] != " "):
    #     presentWinner(board[1])
    # elif (board[2] == board[5]) and (board[5] == board[8]) and (board[2] != " "):
    #     presentWinner(board[2])
    
    # # Diagonal winning conditions
    # elif (board[0] == board[4]) and (board[4] == board[8]) and (board[0] != " "):
    #     presentWinner(board[0])
    # elif (board[2] == board[4]) and (board[4] == board[6]) and (board[2] != " "):
    #     presentWinner(board[2])

# This is the function that displays how to enter the moves that you want to make.
def howToPlay():
    displayBoard(["0", "1", "2",
                  "3", "4", "5",
                  "6", "7", "8"])
    print("\nFor moves, enter the number that corresponds to the spot on the board.")

# This function plays the multiplayer gamemode.
def multiplayer(board):
    howToPlay()
    displayBoard(board)

    i = 1
    # print(detectWin(board)) # I used this to figure out an issue I had with the win detection system
    while detectWin(board) == False:
        while i == 1: # While it is X's turn
            try:
                location = int(input("Player 1 (X), move: "))
                
                # Input must be a number 1-8
                if location in range(9):
                    # Only breaks the loop if the move function was successful.
                    # I had an issue before where it was moving on to the next player even if the move didn't work.
                    if move(board, location, "X") == True:
                        displayBoard(board)
                        break
                    else:
                        displayBoard(board) # Displays the board again so the user can see it when they redo their move
                else:
                    print("Invalid input--you must enter an integer from 0-8.") # Invalid because it's the wrong integer
            except:
                print("Invalid input--you must enter an integer from 0-8.") # Invalid because it's not an integer

        while i == -1: # While it is O's turn
            try:
                location = int(input("Player 2 (O), move: "))
                
                # Input must be a number 1-8
                if location in range(9):
                    # Only breaks the loop if the move function was successful.
                    # I had an issue before where it was moving on to the next player even if the move didn't work.
                    if move(board, location, "O") == True:
                        displayBoard(board)
                        break
                    else:
                        displayBoard(board) # Displays the board again so the user can see it when they redo their move
                else:
                    print("Invalid input--you must enter an integer from 0-8.") # Invalid because it's the wrong integer
            except:
                print("You must enter an integer from 0-8.") # Invalid because it's not an integer

        i *= -1 # This switches i from 1 to -1 and vice versa, switching who plays.
    
    # playAgain()


# MAIN #

# This was used as a way to test the displayBoard function.
# displayBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"])

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# Welcome message for the game
# displayBoard(board)

print("Welcome to Tic Tac Toe!\n")
gamemode = displayGamemodes()

if gamemode == 4:
    multiplayer(board)