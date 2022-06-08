from pyray import draw_grid
from keyboard_services import KeyboardService

class Symbols():
    symbols = []
    def __init__(self):
        star_positions = [(13,3),(23,5),(33,8),(4,7),(8,11),(5,15),(11,16),(39,39),(28,31),(59,30),(57,32),(52,25),(55,27),(53,29),(51,30)]
        oh_positions = [(2,2),(6,4),(10,6),(15,9),(5,10),(14,12),(4,14),(22,17),(21,21),(24,22),(58,26),(56,35),(49,31),(54,22),(56,12)]
        self.symbols.append(Symbol(30,39,(0,0,255,100),'#', False, player=True))
        for oh in oh_positions:
            self.symbols.append(Symbol(oh[0],oh[1],(255,255,255,100),'o',False))
        for star in star_positions:
            self.symbols.append(Symbol(star[0],star[1],(255,0,0,100),'*',True))

class Symbol(KeyboardService):
    x = 0
    y = 0
    color = None
    text = 'X'
    star = False
    player = False
    def __init__(self, x, y, color, text, star, player=False):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.player = player
        self.star = star

    def stars(self):
        # a list of coordinates for the stars, o's, and the cursor- in the grid of 40x60
        for star in self.stars:
            (self.x,self.y) == '*'+ (self.red) 
        return self.stars

    def ohs(self):          
        for oh in self.ohs:
            (self.x,self.y) == 'o'+ (self.white)
        return self.ohs; 

    def cursors(self, set_direction):
        x = set_direction()
        for cursor in self.cursors:
            (self.x,self.y) = '#'+ (self.gray)
        return self.cursors;   
