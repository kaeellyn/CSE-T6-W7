# Edited from artifact.py in rfk. The goal of this file is to provide a class which can be called to create many different rocks. 
# These rocks will be spread across the map initially, and spawn at the top every time the gems and rocks move down.
# When a rock is stepped on by the player it should be removed from the game and -1 the player's score.
# When a rock reaches the bottom of the screen it should cease to exist.

from game.casting.actor import Actor

class Rock(Actor):
    """A small individual actor intended to reduce the score of the player upon collision.

    Attributes:
        Actor (super): The Actor class
    """
    def __init__(self):
        super().__init__()
        
        super().set_text("o")
    