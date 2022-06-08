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
        self._text = ""
        self._collision_score = 0
        self._is_gem = False
        self._is_rock = False
        self._is_used = False

    def get_text(self):
        """Gets the artifact's text.
        
        Returns:
            string: The message.
        """
        return self._text
    
    def set_text(self, text):
        """Updates the text to the given one.
        
        Args:
            text (string): The given message.
        """
        self._text = text

    def get_position(self):
        """Updates the objects position to its current one.
        """
        return self._position

    def get_points(self):
        """Gets the artifact's text.
        
        Returns:
            string: The message.
        """
        return self._collision_score

    def is_used(self, new_text):
        """Updates the object to an empty message and set its status to used.
        """
        self._text = new_text
        self._is_used = True
        self._collision_score = 0
    
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
        
        