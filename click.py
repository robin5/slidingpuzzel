# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: click.py
# Description: This file implements the Click class
# Author: Robin Murray
# ========================================================

class Click:

    """This class indicates if a tile was clicked, or a button was pressed."""

    def __init__(self, value):

        """Creates an instance of the Click class.  This class indicates
        if a tile was clicked, or a button was pressed."""

        # Initialize all click values
        self.tileValue_ = -1
        self.isTile_ = False
        self.isResetButton_ = False
        self.isNewGameButton_ = False
        self.isReplayButton_ = False
        self.isExit_ = False
        
        # See if a tile was clicked
        if type(value) is int:
            self.isTile_ = True
            self.tileValue_ = value

        # See if the graphics windows was closed
        elif (type(value) is str) and (value == "Exit"):
            self.isExit_ = True
            
        # See if the <Reset> button was clicked
        elif value.getText() == "Reset":
            self.isResetButton_ = True
            
        # See if the <New Game> button was clicked
        elif value.getText() == "New Game":
            self.isNewGameButton_ = True
            
        # See if the <Replay> button was clicked
        elif value.getText() == "Replay":
            self.isReplayButton_ = True

        # We should never get here, but if we do raise an exception
        else:
            raise ValueError("Invalid click value encountered!")

    def getTilePosition(self):
        """Returns the position of the clicked tile or -1 if tile was not clicked"""
        return self.tileValue_

    def isTile(self):
        """"Returns True if a tile was clicked, False otherwise"""
        return self.isTile_
    
    def isResetButton(self):
        """Returns True if the <Reset> button was clicked, False otherwise"""
        return self.isResetButton_
    
    def isNewGameButton(self):
        """Returns True if the <New Game> button was clicked, False otherwise"""
        return self.isNewGameButton_
    
    def isReplayButton(self):
        """Returns True if the <Replay> button was clicked, False otherwise"""
        return self.isReplayButton_
    
    def isExit(self):
        """Returns True if the graphics window was closed, False otherwise"""
        return self.isExit_
