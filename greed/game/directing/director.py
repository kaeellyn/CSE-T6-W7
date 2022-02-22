from game.casting.gem import Gem
from game.casting.rock import Rock

from game.shared.color import Color
from game.shared.point import Point
from game.shared.constants import Constants
import random

constants = Constants()
# Direct paste from rfk

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        self._frames = 0
        ()
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position, resolves any collisions with artifacts, removes artifacts that fall off the screen and spawns new artifacts from the top of the screen..
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")

        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        removals = cast.get_actors("removals")
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        # Check for collision in rocks and gems.
        for gem in gems:
            if robot.get_position().equals(gem.get_position()):
                self._score += 1
                cast.remove_actor("gems", gem)
        for rock in rocks:
            if robot.get_position().equals(rock.get_position()):
                self._score -= 1
                cast.remove_actor("rocks", rock)


        if self._frames % 4 == 0:
            # Move all the gems one space down
            for gem in gems:
                gem.set_velocity(Point(0, constants.CELL_SIZE))
                gem.move_next(max_x, max_y)
                if robot.get_position().equals(gem.get_position()):
                    self._score += 1
                    cast.remove_actor("gems", gem)

            # Move all the rocks one space down
            for rock in rocks:
                rock.set_velocity(Point(0, constants.CELL_SIZE))
                rock.move_next(max_x, max_y)
                if robot.get_position().equals(rock.get_position()):
                    self._score -= 1
                    cast.remove_actor("rocks", rock)

            banner.set_text(f"Score: {self._score}")

            # Remove all gems and rocks marked for removal.
            for i in removals:
                cast.remove_actor("removals", i)

            # If a gem is moving out of bounds, mark it for removal.
            for gem in gems:
                if Point.get_y(gem.get_position()) >= constants.MAX_Y - constants.CELL_SIZE:
                    cast.remove_actor("gems", gem)
                    cast.add_actor("removals", gem)
            
            # If a rock is moving out of bounds, mark it for removal.
            for rock in rocks:
                if Point.get_y(rock.get_position()) >= constants.MAX_Y - constants.CELL_SIZE:
                    cast.remove_actor("rocks", rock)
                    cast.add_actor("removals", rock)

            # If there aren't enough artifacts, spawn more. 
            if len(gems) + len(rocks) <= constants.DEFAULT_ARTIFACTS:
                new_artifact_count = random.randint(-1, 4)
                if new_artifact_count > 0:
                    for _ in range(new_artifact_count):
                        gem_or_rock = random.randint(1, 2)
                        if gem_or_rock == 1:
                            artifact = Gem()
                        elif gem_or_rock == 2:
                            artifact = Rock()
                        else:
                            print("There was an error in finding whether this is a rock or a gem in director.py")
                        
                        artifact.create_random_values()
                        artifact_x = Point.get_x(artifact.get_position())
                        artifact.set_position(Point(artifact_x, 0))

                        if gem_or_rock == 1:
                            cast.add_actor("gems", artifact)
                        elif gem_or_rock == 2:
                            cast.add_actor("rocks", artifact)


        self._frames += 1
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()