import colors

class Colors():
    #appends the tuple of colors needed for each symbol on screen

    '''Attributes:
        candy_apple_red=RGBA
        white=RGBA
        gray=RGBA

        Returns with an append to the item that inherits it
        '''
    
    def __init__(self):
        # defines the RGBA of each color and leaves an open append to whatever inherits it.
        self.red = [255,8,0,100]
        self.white =[255,255,255,100]
        self.gray = [31,216,222,57]

    def allowed_colors(self):
        return ['red', 'white', 'gray']
