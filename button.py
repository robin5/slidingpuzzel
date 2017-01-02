# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: button.py
# Description: This file implements the Button class
# Author: Robin Murray
# ========================================================

from graphics import *

class Button:

    # -----------------------------------------------------
    # Function: __init__
    # Description: Creates an instance of the button class
    # Return: None
    # -----------------------------------------------------

    def __init__(self, point, text):

        """Creates a button."""

        # Button dimensions
        width = 120
        height = 40

        # Create button rectangle
        self.button = Rectangle(point, Point(point.x + width, point.y + height))
        self.button.setFill("orange")

        # Create button text
        self.buttonText = Text(Point(point.x + width/2, point.y + height/2), text)
        self.buttonText.setTextColor('black')

    
    # -----------------------------------------------------
    # Function: draw
    # Description: draws the button on the graphics window
    # Parameters:
    #     win - Graphics Win to draw button on
    # Return: None
    # -----------------------------------------------------

    def draw(self, win):
        
        """Draws the button on the graphics window"""

        self.button.draw(win)
        self.buttonText.draw(win)
        
    # --------------------------------------------------
    # Function: hit
    # Description: determines if point is within region
    #     of buttons bounding rectangle
    # Parameters:
    #     point - mouse pointer clicked location
    # Return:
    #     True - if button was hit
    #     False - otherwise
    # --------------------------------------------------

    def hit(self, point):

        """Determines if point is within region of buttons bounding rectangle"""

        # Test for the button
        if self.button.getP1().getX() <= point.getX() <= self.button.getP2().getX() and\
           self.button.getP1().getY() <= point.getY() <= self.button.getP2().getY():
            return True

        return False
        
    # --------------------------------------------------
    # Function: getText
    # Description: Returns the text on the button
    # Parameters: None
    # Return: Button's text
    # --------------------------------------------------

    def getText(self):
        
        """Returns the text on the button"""
        
        return self.buttonText.getText()
    
