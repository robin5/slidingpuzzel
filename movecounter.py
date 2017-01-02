# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: movecounter.py
# Description: This file implements the MoveCounter class
# Author: Robin Murray
# ========================================================

from graphics import *

class MoveCounter:

    """This class keeps track of how many moves have occurred in a game."""

    INITIAL_TEXT = "How many moves\n will it take\n you to win!!!"

    # ----------------------------------------------------------
    # Function: __init__
    # Description: Creates an instance of the MoveCounter class
    # Return: None
    # ----------------------------------------------------------

    def __init__(self, point):

        """Creates a MoveCounter with initial text."""
        
        self.text = Text(point, MoveCounter.INITIAL_TEXT)
        self.text.setTextColor('white')
        self.text.setStyle('bold')
        self.count = 0

    # --------------------------------------------------
    # Function: draw
    # Description: draws the button on the graphics window
    # Parameters:
    #     win - Graphics Win to draw button on
    # Return: None
    # --------------------------------------------------

    def draw(self, win):
        
        """Draw the MoveCounter onto the graphics window.."""

        self.text.draw(win)
        
    # --------------------------------------------------
    # Function: incrementCount
    # Description: Increment the move count
    # Parameters: None
    # Return: None
    # --------------------------------------------------

    def incrementCount(self):
        
        """Increment the move count."""

        self.count += 1
        self.text.setSize(36)
        self.text.setText(str(self.count))

    # --------------------------------------------------
    # Function: reset
    # Description: Reset the count to 0 and show the
    #              initial message.
    # Parameters: None
    # Return: None
    # --------------------------------------------------

    def reset(self):
        
        """Reset the count to 0 and show the initial message."""

        self.text.setSize(13)
        self.text.setText(MoveCounter.INITIAL_TEXT)
        self.count = 0
    
