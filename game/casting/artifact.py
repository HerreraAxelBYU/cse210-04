from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._collision_score = 0
        self._is_gem = False
        self._is_rock = False

    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_position(self):
        """Updates the objects position to its current one.
        """
        return self._position


class Gem(Artifact):
    """A child class of the Artifact, inherits all Artifact and Actor attributes.
    When the player touches a Gem, their 'self._score' adds 1.
    """
    def __init__(self):
        super().__init__()
        self._is_gem = True
        self._collision_score = 1

class Rock(Artifact):
    """A child class of the Artifact, inherits all Artifact and Actor attributes.
    When the player touches a Rock, their 'self._score' subtracts 1.
    """
    def __init__(self):
        super().__init__()
        self._is_rock = True
        self._collision_score = -1