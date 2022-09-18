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

# MAIN

displayBoard(["a", "b", "c", "d", "e", "f", "g", "h", "i"])