import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact, Gem, Rock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

# ======= Colors ======= #
WHITE = Color(183,183,183)
GRAY = Color(142,142,142)
BLUE = Color(0,0,255)
RED = Color(255,0,0)
GREEN = Color(0,255,0)
YELLOW = Color(255,255,0)
#     (Just for fun)     #
DIAMOND = Color(0,238,238)
EMERALD = Color(0,201,87)
RUBY = Color(220,20,60)
SAPPHIRE = Color(30,144,255)
TOPAZ = Color(255,20,147)
GARNET = Color (154,50,205)
GOLD = Color(255,215,0)
SILVER = Color(187,255,255)
BRONZE = Color(255,128,0)
GEM_COLOR_LIST = [DIAMOND, EMERALD, RUBY, SAPPHIRE, TOPAZ, GARNET, GOLD, SILVER, BRONZE]
STONE = Color(110,123,139)
SLATE = Color(139,115,85)
GRANITE = Color(180,205,205)
SANDSTONE = Color(139,139,122)
ROCK_COLOR_LIST = [STONE, SLATE, GRANITE, SANDSTONE]
#      Random Colors     #
rand_r = random.randint(50, 255)
rand_g = random.randint(60, 255)
rand_b = random.randint(70, 255)
RANDOM_COLOR = Color(rand_r, rand_g, rand_b)

# ==== Game Options ==== #
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
DEFAULT_GEMS = 60
DEFAULT_ROCKS = 30

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner (score)
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(YELLOW)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # (TEST) create the tracker, which displays the position of the robot.
    tracker = Actor()
    tracker.set_text("")
    tracker.set_font_size(FONT_SIZE)
    tracker.set_color(GRAY)
    tracker.set_position(Point(400, 0))
    cast.add_actor("tracker", tracker)

    # (TEST) create a notification, which displays the positon of a collison.
    notification = Actor()
    notification.set_text("")
    notification.set_font_size(FONT_SIZE)
    notification.set_color(GRAY)
    notification.set_position(Point(800, 0))
    cast.add_actor("notification", notification)

    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create Gems to be scattered on the screen.
    for n in range(DEFAULT_GEMS):
        # place Gems in random positions.
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        # get Gem colors:
        color = random.choice(GEM_COLOR_LIST)
        # set Gem text:
        text = "*"
        # set up a Gem object.
        gem = Gem()
        gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        cast.add_actor("gems", gem)

    # create Rocks to be scattered on the screen.
    for n in range(DEFAULT_ROCKS):
        # place Rocks in random positions.
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        # get Rock colors:
        color = random.choice(ROCK_COLOR_LIST)
        # set Rock text:
        text = "O"
        # set up a Gem object.
        rock = Rock()
        rock.set_text(text)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        cast.add_actor("rocks", rock)
    
    # Start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

    # Temporary, only for testing.
    director._help_test(cast)

if __name__ == "__main__":
    main()
    
    