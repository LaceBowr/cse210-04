#from character import Character
#from keyboard_services import KeyboardService
from video_service import VideoService
from symbols import Symbols
from time import sleep

class Director():
    #Keeps track of input, updates, and output and sends them to their needed locations
    '''
    '''
    def __init__(self):
        self.update_score = []
        #self.get_input=(int('x'))
        #self.output 

    def update_score(self, get_character_score):
        self.get_character_score += self.update_score.append()
        return self.update_score

    def start_game(self):
        vs = VideoService()
        vs.open_window()
        syms = Symbols()
        
        # Demonstrate functional video service
        vs.draw_grid(syms)
        sleep(10)
        
        # while loop while game is running
            # get keyboard direction
            # update positions of all symbols
            # update score
            # redraw the grid

        

    
