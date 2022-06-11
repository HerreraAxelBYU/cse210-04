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
        # Set the starting score to 0.
        self._score = 0
        
    
    def _help_test(self, cast):
        """Use to view the list of cast objects.
        """
        # (TEST) Temporary method, just used to check on the amount of objects.
        all_cast = cast.get_all_actors()
        print("--------------------")
        print("Objects in game:\n")
        print(f"All Actors: {all_cast}")
        print("--------------------")
        banner = cast.get_first_actor("banners")
        tracker = cast.get_first_actor("tracker")
        notification = cast.get_first_actor("notification")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")
        print(f"Player: {robot}, Banner: {banner}, Tracker: {tracker}, Notify: {notification}")
        print(f"Gems: [{gems}] \n Rocks: [{rocks}]")
        print(f"All Artifacts: [{artifacts}]")
        print("---------------------")

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._help_test(cast)

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
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        banner = cast.get_first_actor("banners")
        tracker = cast.get_first_actor("tracker")
        notification = cast.get_first_actor("notification")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # (Test) Get the robots location to print in the tracker.
        robot_position = robot.get_position()
        rob_x_pos = robot_position.get_x()
        rob_y_pos = robot_position.get_y()

        banner.set_text(f'SCORE: {self._score}')
        tracker.set_text(f'Position: [{rob_x_pos}, {rob_y_pos}]')
        notification.set_text(f'Collision: ')

        # Cause Gems and Rocks to fall continuously.
        for gem in gems:
            gem.falling()
        for rock in rocks:
            rock.falling()

        # Check if in collision with gem.
        for gem in gems:
            if robot.get_position().equals(gem.get_position()):
                notification.set_text(f'Collision: Gem')
                self._score += gem._collision_score
                # Update the gem object to 'is_used'.
                gem.is_used(" ")
        # Check if in collision with rock.
        for rock in rocks:
            if robot.get_position().equals(rock.get_position()):
                notification.set_text(f'Collision: Rock')
                self._score += rock._collision_score
                # Update the rock object to 'is_used'. 
                rock.is_used(" ")

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        
        