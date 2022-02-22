# Import all needed libraries and other resources
import random

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rock import Rock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.shared.constants import Constants

# Set the constants for use in the program

constants = Constants()

# FRAME_RATE = constants.FRAME_RATE
# MAX_X = constants.MAX_X
# MAX_Y = constants.MAX_Y
# CELL_SIZE = constants.CELL_SIZE
# FONT_SIZE = constants.FONT_SIZE
# COLS = constants.COLS
# ROWS = constants.ROWS
# CAPTION = constants.CAPTION
# WHITE = constants.WHITE
# DEFAULT_ARTIFACTS = constants.DEFAULT_ARTIFACTS


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(constants.FONT_SIZE)
    banner.set_color(constants.WHITE)
    banner.set_position(Point(constants.CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - (constants.CELL_SIZE* 2))
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(constants.FONT_SIZE)
    robot.set_color(constants.WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the gems and rocks
    for n in range(constants.DEFAULT_ARTIFACTS):
        i = 0
        j = random.randint(42, 43)
        if j == 42:
            i = 42
        else: 
            i = 111
            
        text = chr(i)

        x = random.randint(1, constants.COLS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        if i == 42:
            artifact = Gem()
        elif i == 111:
            artifact = Rock()
        else:
            print("There was an error in finding whether this is a rock or a gem in __main__.py")
        
        artifact.set_text(text)
        artifact.set_font_size(constants.FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)

        if i == 42:
            cast.add_actor("gems", artifact)
        elif i == 111:
            cast.add_actor("rocks", artifact)
        
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()