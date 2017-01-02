# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: tileboard.py
# Description: This file implements the GameBoard class
# Author: Robin Murray
# ========================================================

from graphics import *
from random import *
from click import *
from button import *
from checkmark import *

class GameBoard:

    """Implements a sliding puzzle game board"""

    # A list which describes allowable tile moves on the puzzle
    _allowableMoves = [[1,4], [0,2,5], [1,3,6], [2,7],
             [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11],
             [4,9,12], [5,8,10,13], [6,9,11,14], [7,10,15],
             [8,13], [9,12,14], [10,13,15], [11,14]]

    # --------------------------------------------------
    # Function: __init__
    # Description: Creates an instance of the TileBoard class
    # Return: None
    # --------------------------------------------------

    def __init__(self, win, side, offset):

        """Creates a sliding puzzle game board."""

        self.win = win
        self.side = side
        self.offset = offset
        self._lockTiles = False

        # Place the 16 tiles into the tile list
        self.tiles = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        # Shuffle the tile list
        self._shuffle()

        # Make a copy of the order of the tiles for Reset feature
        self.originalTiles = self._cloneTiles(self.tiles)

        # The instantiated tile rectangles and text graphics objects
        self.tileRects = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.tileTexts = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        # Draw Reset button
        self.resetButton = Button(Point(11 * side / 2,  1 * offset - 10), "Reset")
        self.resetButton.draw(win)

        # Draw New Game button
        self.newGameButton = Button(Point(11 * side / 2,  7 * offset / 4 - 10), "New Game")
        self.newGameButton.draw(win)

        # Draw Replay button
        self.replayButton = Button(Point(11 * side / 2, 10 * offset / 4 - 10), "Replay")
        self.replayButton.draw(win)

        # Create orange rectangle behind board
        rect = Rectangle(Point(self.offset-10, self.offset-10), \
                         Point(self.offset+self.side*4+10, self.offset+self.side*4+10))
        rect.setFill("orange")
        rect.draw(win)
        self._drawTiles()

        # Draw Message text
        self.message = Text(Point(3 * self.side, self.offset / 2), "")
        self.message.setTextColor('orange')
        self.message.setStyle('bold')
        self.message.setSize(18)
        self.message.draw(win)

        # Create the orange check mark
        self.checkMark = CheckMark(win, Point(self.offset + self.side + 214/2, 3 * self.side))

    # --------------------------------------------------
    # Function: _drawTiles
    # Description: Draws the 16 puzzle tile squares
    #              given the contents of the tiles array
    # Return: None
    # --------------------------------------------------

    def _drawTiles(self):

        """Draws the 16 puzzle tile squares"""
        
        # Draw 16 tile squares
        for i in range(16):
            
            # retain a reference to the tile rectangles
            self.tileRects[i], self.tileTexts[i] = self._drawTile(i, self.tiles[i])
            

    # --------------------------------------------------
    # Function: setTiles
    # Description: Copies the passed in tiles and  
    #              redraws the puzzle board
    # Return: None
    # --------------------------------------------------

    def setTiles(self, tiles):
        
        """Copies the passed in tiles and redraws the puzzle board"""

        # Make an internal copy of the tiles
        self.tiles = self._cloneTiles(tiles)
        
        # Make another copy to be used when the user presets <Reset> button
        self.originalTiles = self._cloneTiles(self.tiles)

        # Draw the passed in tiles
        self._drawTiles()

    # --------------------------------------------------
    # Function: getTiles
    # Description: Returns a copy of the current tile   
    #              array 
    # Return: None
    # --------------------------------------------------

    def getTiles(self):

        """Returns a copy of the current tile array"""

        return self.tiles
        

    # --------------------------------------------------
    # Function: _drawTile
    # Description: Draws a puzzle tile on the graphics window
    # Parameter:
    #     tilePosition - Position of the tile to draw
    #     tileNumber - The number that appears on the tile
    # Return: None
    # --------------------------------------------------

    def _drawTile(self, tilePosition, tileNumber):

        """Draws a puzzle tile on the graphics window."""

        # Determine the x and y offsets of the tile given the tile's index
        x = (tilePosition % 4) * self.side + self.offset
        y = (tilePosition // 4) * self.side + self.offset

        # Create the tile's rectangle
        rect = Rectangle(Point(x, y), Point(x + self.side, y + self.side))

        # Set the color of the tile given the number on the tile
        if tileNumber == 0: # The tile with 0 value is the gray tile
            rect.setFill("gray")
            rect.setOutline("gray")
            tileNumber = ""
        else: # All other tiles are green with the tileNumber on the top
            rect.setFill("green")
            rect.setOutline("gray")

        # Draw the tile's rectangle on the graphic window
        rect.draw(self.win)

        # Draw the white numbered value which appears on the tile
        text = Text(Point(x + self.side/2, y + self.side/2), tileNumber)
        text.setTextColor('white')
        text.draw(self.win)

        # return the tile's rectangle object
        return rect, text

    # --------------------------------------------------
    # Function: slideTile
    # Description: Attempt to slide the tile
    # Parameters: tilePosition - which tile to slide
    # Return: Whether the slide was sucessful or not
    # --------------------------------------------------

    def slideTile(self, tilePosition):

        """Attempt to slide the tile specified by tilePosition parameter"""

        # Each tile position has a given set of allowable moves (i.e. tiles)
        # it can swap positions with.  The only legal move however is to
        # swap positions with the gray tile that has a tileNumber of 0

        # Loop through the allowable moves
        for i in GameBoard._allowableMoves[tilePosition]:

            # See if one of the tile positions has a tile value of 0
            if self.tiles[i] == 0:

                # If we get here, one of the legal moves has the
                # 0 tile, so swap tiles
                self._swap(tilePosition, i)
                
                # Now that we have moved the tile, Test 
                # to see if this move wins the game
                self._testForWinningBoard()
                return True

        # If we get here then we did not find the 0 tile in the list
        # of legal moves so return that we did not make a move
        return False

    # --------------------------------------------------
    # Function: _swap
    # Description: swaps two tiles given by a and b
    # Parameters:
    #     a - a tile to swap with tile b
    #     b - a tile to swap with tile a
    # Return: None
    # --------------------------------------------------

    def _swap(self, a, b):

        """Swaps tiles given by tile positions a and b"""
        
        # Swap the tile numbers
        self.tiles[a], self.tiles[b] = self.tiles[b], self.tiles[a]

        # Undraw the tile in position a
        self.tileRects[a].undraw()
        self.tileTexts[a].undraw()
        
        # draw a new tile in position a with the swapped value
        self.tileRects[a], self.tileTexts[a] = self._drawTile(a, self.tiles[a])

        # Undraw the tile in position b
        self.tileRects[b].undraw()
        self.tileTexts[b].undraw()

        # Draw a new tile in position b with the swapped value
        self.tileRects[b], self.tileTexts[b] = self._drawTile(b, self.tiles[b])
        return

    
    # --------------------------------------------------
    # Function: _shuffle
    # Description: Causes a shuffle of the tileNumbers in
    #              the tile positions array
    # Parameters:
    #     a - a tile to swap with tile b
    #     b - a tile to swap with tile a
    # Return: None
    # --------------------------------------------------

    def _shuffle(self):

        """Causes a shuffle of the tileNumbers in the tilePositions array"""
        
        # Place the 16 tiles into the tile list
        shuffle(self.tiles)
        
    # --------------------------------------------------
    # Function: _testForWinningBoard
    # Description: Test to see if the tiles are in a
    #     winning game order
    # Parameters:
    #     win - The graphics window
    #     tiles - The tile list
    # Return:
    #     True - If game is won
    #     False - otherwise
    # --------------------------------------------------

    def _testForWinningBoard(self):

        """Test to see if the tiles are in winning game order,
           and if so, display it to the user."""
        
        # Note: The winning order looks like this:
        # ----------------------------------------------------------------
        # Position:  0  1  2  3  4  5  6  7  8   9  10  11  12  13  14  15
        # Value      1  2  3  4  5  6  7  8  9  10  11  12  13  14  15   0
        
        # Loop throught the tiles array
        for i in range(len(self.tiles) - 1):
            if self.tiles[i] != i + 1: # then this is not a winning board
                return False
            
        # If we get here, then a bad combination was not found
        # so tell the user we won!
        
        # Display winning message
        self.message.setText("Congratulations, You WON!")

        # Display the orange check mark image
        self.checkMark.show()
            
        # Don't allow the user to click on any more tiles since game is over
        self._lockTiles = True
        return True

    # --------------------------------------------------
    # Function: reset
    # Description: Resets the game board back to it's
    #              initial state
    # Parameters: None
    # Return: None
    # --------------------------------------------------

    def reset(self):

        """Resets the game board back to it's initial state"""
        
        # Set the tiles array back to the original array
        self.tiles = self._cloneTiles(self.originalTiles)

        # Draw the board with the original tiles
        self._drawTiles()

        self._lockTiles = False

    # --------------------------------------------------
    # Function: newGame
    # Description: Resets the game board to a new game
    # Parameters: None
    # Return: None
    # --------------------------------------------------

    def newGame(self):

        """Resets the game board back to it's initial state"""
        
        # Shuffle the tiles
        self._shuffle()
            
        # Save a copy of the reshuffled tiles (for reset)
        self.originalTiles = self._cloneTiles(self.tiles)
            
        # Draw the board with the newly shuffled tiles
        self._drawTiles()
            
        self._lockTiles = False

    # --------------------------------------------------
    # Function: _cloneTiles
    # Description: Creates a copy of the tile list
    # Parameters:
    #     The tile list
    # Return: A new list of tiles
    # --------------------------------------------------

    def _cloneTiles(self, tiles):

        """Creates a copy of the tile list"""

        # Create a new tiles list        
        newTilesList = []

        # Loop over the tiles
        for i in range(len(tiles)):

            # Add a new tile in the new list
            newTilesList.append(tiles[i])

        return newTilesList

    # --------------------------------------------------
    # Function: getClick
    # Description: Waits for a click on the board then
    #     returns a new click object indicating what
    #     was clicked.
    # Return: 
    # --------------------------------------------------

    def getClick(self):

        try:
            # Indicate nothing yet clicked
            newClick = False
            
            # Loop until we get a hit on a valid object
            while True:
                
                # Input the mouse location
                p = self.win.getMouse()

                # If the tiles are locked, then don't check for them being clicked
                if not self._lockTiles:

                    # Test for input on 1 of the 16 tiles
                    for i in range(16):
                        
                        # calculate the extent of the given tile
                        x1 = (i % 4) * self.side + self.offset
                        y1 = (i // 4) * self.side + self.offset
                        x2 = x1 + self.side
                        y2 = y1 + self.side

                        # Test for a tile hit and it not being the 0 (i.e. gray) tile
                        if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2 and self.tiles[i] != 0:
                            newClick = Click(i)
                            break

                # If not a tile clicked, test for one of the buttons clicked
                if newClick == False:
                    
                    # test for input on the reset button
                    if self.resetButton.hit(p):
                        newClick = Click(self.resetButton)

                    # test for input on the new game button
                    elif self.newGameButton.hit(p):
                        newClick = Click(self.newGameButton)

                    # test for input on the replay button
                    elif self.replayButton.hit(p):
                        newClick = Click(self.replayButton)
                        
                # If a tile or a button has been clicked, 
                # clear the ui and return the result
                if not newClick == False:
                    
                    # Clear any previous messages
                    self.message.setText("")

                    # Hide the check mark
                    self.checkMark.hide()

                    return newClick


        except GraphicsError:
            return Click("Exit")
        
        return None

