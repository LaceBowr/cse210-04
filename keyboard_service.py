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
        self.dx=0
        self.dy=0
    def get_direction(self):
        #takes input done by character in play and implements a move
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        dx,dy = self.new_direction()# = (dx,dy)
        #self.new_direction == get_direction(dx,dy) 
  
        return dx
