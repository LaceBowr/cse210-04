
import pyray

class VideoService():
    '''Outputs the game onto the screen by using the keyboard_services input.'''
    def __init__(self):
        cellx, celly = self.cell_size()
        self.width = cellx * 60 
        self.height = celly * 40
        self.score = 0
        '''
        Attributes:
        self.director.set_direction = (x,0)
        self.get_width = dx
        self.get_height = dy
        self.cell_size = (dx=60 ,dy=40)
        self.draw_grid = (dx,dy), self.get_positon
        self.gems_rocks.set_player_hit_results = (self.gems_rocks.player_hit: +1 gem or -1rock)
        self.set_score(self.character.character_score)
        '''

    def open_window(self):
        pyray.init_window(self.width, self.height, 'Greed')
        pyray.set_target_fps(20)
        pyray.clear_background(pyray.BLACK)
        pyray.begin_drawing()
  
    def get_width(self):
        #Gets video screen width for the session of the game
        #if cell_size(dx,dy):
        #    dx = width
        return self.width

    def get_height(self):
        #Gets video screen height for the session of the game
        #if cell_size(dx,dy):
        #    dy = height
        return self.height

    def cell_size(self):
        #maps out cell size for each game that is initiated
        return 20,20

    def draw_grid(self, symbols):
    #Draws out the overall cell window, the symbols, the colors and 
    # the falling movements to the screen
        pyray.clear_background(pyray.BLACK)
        pyray.begin_drawing()
        cellx, celly = self.cell_size()
        for symbol in symbols.symbols:
            pyray.draw_text(symbol.text, symbol.x*cellx, symbol.y*celly, cellx-2, symbol.get_display_color())
        pyray.draw_text(f'Score: {self.score}', 20, 100, 16, pyray.WHITE)
        pyray.end_drawing()

    def game_running(self):
        if pyray.window_should_close() or self.score < 0:
            return False
        return True

    def player_hit_results(self, player, symbol, red, white):
        if (player.x,player.y) == (symbol.x,symbol.y):
            if symbol.stars:
                self.red = 1
                self.white = -1
                return True
        return False

    def character_move(self):
        #sets gems/rocks and the player's hit/move_at_end_position to the screen
        (self.dx,self.dy)
        return self.dx, self.dy

    def set_score(self,score):
        self.score = score
        #print(f'SCORE:{score}') 
        #pyray.begin_drawing()
        #pyray.draw_text(f'Score: {score}',20,100,16,pyray.WHITE)
        #pyray.end_drawing

    def close_window(self):
        pyray.close_window()
