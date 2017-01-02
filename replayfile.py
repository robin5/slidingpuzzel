# ========================================================
# CTEC 121 - Final Project - Sliding Puzzel
# ========================================================
# File: replayfile.py
# Description: This file implements the ReplayFile class
# Author: Robin Murray
# ========================================================

class ReplayFile:
    
    """ This class implements the interface between the Sliding Puzzle program and the replay file."""

    MISSING_FILE = "Missing replay file!  Replay terminated."
    CORRUPTED_FILE = "Replay file has been corrupted!  Replay Terminated."
    FILE_OPEN_ERROR = "File Open Error: Can't access replay file."
    FILE_WRITE_ERROR = "File Write Error: Can't access replay file."

    # ---------------------------------------------------------
    # Function: __init__
    # Description: Creates an instance of the ReplayFile class
    # Return: None
    # ---------------------------------------------------------

    def __init__(self, fileName):

        """Create a file containg the initial board setup and subsequent tile moves."""
        
        self._fileName = fileName

    # ---------------------------------------------------------
    # Function: reset
    # Description: Erases the replay file, and creates a
    #              new one with the initial tile setup
    # Return: None
    # ---------------------------------------------------------

    def reset(self, tiles):
        
        """Erases the replay file, and creates a new one with the initial tile setup"""

        try:
            # Open the replay file
            outputfile = open(self._fileName, "w")
            try:
                # Put the initial tile setup
                print(tiles, file = outputfile)
            except:
                print(self.FILE_WRITE_ERROR)
            finally:
                outputfile.close()
        except:
            print(self.FILE_OPEN_ERROR)

    # ---------------------------------------------------------
    # Function: writeClick
    # Description: Puts the clicked tile into the replay file
    # Return: None
    # ---------------------------------------------------------

    def writeClick(self, click):
        
        """Write the clicked tile to the replay file"""

        try:
            # Open the replay file
            outputfile = open(self._fileName, "a")
            try:
                # Put the clicked tile into the file
                print(click.getTilePosition(), file = outputfile)
            except:
                print(self.FILE_WRITE_ERROR)
            finally:
                outputfile.close()
        except:
            print(self.FILE_OPEN_ERROR)

    # ---------------------------------------------------------
    # Function: input
    # Description: Reads the initial tile setup,
    #              and all of the clicked tiles
    # Return: None
    # ---------------------------------------------------------

    def input(self):

        """Reads the initial tile setup, and all of the clicked tiles"""

        try:
            # open the file for input
            inputFile = open(self._fileName, "r")

        except:
            print(self.MISSING_FILE)
            return None, None
        
        try:
            # Read the first line which should be the tiles array
            tiles = inputFile.readline().lstrip().rstrip()
            
            # Remove surrounding brackets and split the entries into a list
            # These are now the tiles for the start of play in the form of
            # a list of strings
            tiles = tiles[1:-1].split(',')

            # Turn the strings into ints
            for i in range(len(tiles)):
                tiles[i] = int(tiles[i])
                
            # Now for the clicks of the game

            # initialize the clicks array to an empty array
            clicks=[]

            # loop through the file
            for line in inputFile:
                
                # Each line of the file is one click value,
                # trim the line, and append the entry 
                clicks.append(int(line.rstrip().lstrip()))

            return tiles, clicks

        except ValueError:
            print(self.CORRUPTED_FILE)
            return None, None

        except:
            print(self.CORRUPTED_FILE)
            return None, None

        finally:
            # close the file
            inputFile.close()

    
