# ==============================================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ==============================================================================
# File: SlidingPuzzle.py
# Description: This program implements the Sliding Puzzle game.
# Author: Robin Murray
# ==============================================================================

from graphics import *
from gameboard import *
from movecounter import *
from replayfile import *

# --------------------------------------------------
# Function: replayGame
# Description: Replays the game from the replay file
# Parameters:
#     replayFile - The ReplayFile object that records the game
#     gameBoard - the tile board
#     moveCounter - the MoveCounter object on the graphics window
# Return: none
# --------------------------------------------------

def replayGame(replayFile, gameBoard, moveCounter):
    
    """Replays the game from the replay file."""

    # Input the tiles and clicks from the replay file
    tiles, clicks = replayFile.input()

    # Test for valid input
    if ((tiles == None) or (clicks == None)):
        return

    # Redraw the tile board
    gameBoard.setTiles(tiles)

    # Reset the move counter
    moveCounter.reset()

    # Replay the clicks from the file
    for click in clicks:

        # Move the clicked tile
        if not gameBoard.slideTile(click):
            print("The replay file has been corrupted!  Replay terminated.")
            return
        
        # increment the move counter
        moveCounter.incrementCount()
        
        #print(click)
        time.sleep(.1)

# ----------------------------------------------------
# Function: main
# Description: Executes main program loop which draws 
#     the game board, accepts user input and executes
#     user commands
# Return: 
# ----------------------------------------------------

def main():
    '''Implements main program loop.'''

    # Introduction
    print("Play sliding puzzle game!")

    # Puzzle dimensions
    side = 80
    offset = 80

    # Create a graphics window 8 wide and 6 height
    win = GraphWin("Sliding Puzzle by Robin Murray", 15 * side / 2, 6 * side)
    win.setBackground("gray")
    
    # Draw board with the shuffled tiles
    gameBoard = GameBoard(win, side, offset)

    # Draw the move counter
    moveCounter = MoveCounter(Point((12 * side / 2) + (side/4), 4 * offset))
    moveCounter.draw(win)

    # Create replay file
    replayFile = ReplayFile("replay.txt")
    replayFile.reset(gameBoard.getTiles())

    # Loop continually until user closes the graphics window
    while True:
        
        # Input a click on the board        
        click = gameBoard.getClick()

        # Test for a numbered tile being clicked
        if click.isTile():

            # Try to slide the numbered tile
            if gameBoard.slideTile(click.getTilePosition()):

                # Increment the move counter
                moveCounter.incrementCount()

                # save the click to the replay file
                replayFile.writeClick(click)

        # Test for Reset button
        elif click.isResetButton():

            # Reset the puzzle board
            gameBoard.reset()
            
            # Reset the number of moves counter
            moveCounter.reset()

            # Reset the replay file
            replayFile.reset(gameBoard.getTiles())
            
        # Test for New game button
        elif click.isNewGameButton():

            # Start a new game on the puzzle board
            gameBoard.newGame()
            
            # Reset the move counter
            moveCounter.reset()
            
            # Reset the replay file
            replayFile.reset(gameBoard.getTiles())

        # Test for replay button
        elif click.isReplayButton():
            
            # Replay the game
            replayGame(replayFile, gameBoard, moveCounter)
            
        elif click.isExit():
            
            print("done")
            break;

    win.close()

# ------------------------------------------------------------------------------
#                              End of Script
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
