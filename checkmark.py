# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: checkmark.py
# Description: This file implements a large check mark
# Author: Robin Murray
# ========================================================

from graphics import *

class CheckMark():

    """This class displays a large check mark on the graphics window."""

    def __init__(self, win, point):

        """Instantiates an image of a large orange check mark"""
        
        self.win = win
        self.checkImage = Image(point, "orangecheck.png")
        self.checkDrawn = False

    def show(self):

        """Shows the check mark image"""
        
        # Draw the orange check image is 214 x 235
        if not self.checkDrawn:
            self.checkImage.draw(self.win)
            self.checkDrawn = True

    def hide(self):

        """Hides the check mark image"""
        
        if self.checkDrawn:
            self.checkImage.undraw()
            self.checkDrawn = False
        
