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

constants = Constants()

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
    for _ in range(constants.DEFAULT_ARTIFACTS):
        gem_or_rock = random.randint(1, 2)
        if gem_or_rock == 1:
            artifact = Gem()
        elif gem_or_rock == 2:
            artifact = Rock()
        else:
            print("There was an error in finding whether this is a rock or a gem in __main__.py")
        
        artifact.create_random_values()

        if gem_or_rock == 1:
            cast.add_actor("gems", artifact)
        elif gem_or_rock == 2:
            cast.add_actor("rocks", artifact)
        
    
    # start the game
    keyboard_service = KeyboardService(constants.CELL_SIZE)
    video_service = VideoService(constants.CAPTION, constants.MAX_X, constants.MAX_Y, constants.CELL_SIZE, constants.FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()