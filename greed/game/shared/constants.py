from game.shared.color import Color

class Constants:
    """A collection of useful variables for the game Greed.

    The Constants class was made to hold a number of variables for us to reference throughout the program. 
    The hope is that this will allow us to change a variable here without breaking anything within the program itself.
    """ 

    def __init__(self):
        self.FRAME_RATE = 12
        self.MAX_X = 900
        self.MAX_Y = 600
        self.CELL_SIZE = 15
        self.FONT_SIZE = 15
        self.COLS = 60
        self.ROWS = 40
        self.CAPTION = "Greed"
        self.WHITE = Color(255, 255, 255)
        self.DEFAULT_ARTIFACTS = 40