# Edited from artifact.py in rfk. The goal of this file is to provide a class which can be called to create many different gems. 
# These gems will be spread across the map initially, and spawn at the top every time the gems and rocks move down.
# When a gem is stepped on by the player it should be removed from the game and +1 the player's score.
# When a gem reaches the bottom of the screen it should cease to exist.

from game.casting.actor import Actor

class Gem(Actor):
    """"""
    def __init__(self):
        super().__init__()

        super().set_text("*")