from colors import Colors

class Symbol():
    x = 0
    y = 0
    color = None
    text = 'X'
    colors = Colors()
    def __init__(self, x, y, color, text):
        self.x = x
        self.y = y
        if color not in self.colors.allowed_colors():
            raise Exception('Color not allowed')
        self.color = color
        self.text = text

    def get_display_color(self):
        if self.color == 'red':
            return self.colors.red_color()
        elif self.color == 'white':
            return self.colors.white_color()
        if self.color == 'gray':
            return self.colors.gray_color()
