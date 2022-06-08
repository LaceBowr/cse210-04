import pyray
# Need to import the horizontal and vertical position to work

class Keyboard_service:
    """Detects player input. 
    
    The responsibility of the Keyboard_services class is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """    
    def __init__(self, cell_size=1):
        self._cell_size=cell_size
    
    def define_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        x_movement=0
        dy=0

        if pyray.is_key_down(pyray.KEY_LEFT):
            x_movement=-1
        if pyray.is_key_down(pyray.KEY_RIGHT):
            x_movement=1
    #Class that defines the horizontal distance from a certain point in the display
        direction: Point(x_movement,dy) 
        direction=direction.scale(self._cell_size)
    
        return direction


