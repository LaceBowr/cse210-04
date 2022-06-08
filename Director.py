#from character import Character
#from keyboard_services import KeyboardService
from keyboard_services import KeyboardService
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

    def start_game(self, new_direction):
        
        question = input('Experience the thrill having gems or rocks fall upon you! <i>Greed</i>\nmight seem easy, but even the best treasure-hunter can end up in the wrong place and \nget hit by rocks.\nThe rules are simple.\n The character can move\non the screen trying to dodge or hit the falling objects.\n*If your character(#) move connects with a gem(*) you get a +1 to your score.\n*If the character move connects with a rock you get a -1 to your score.\n\nDo you want to start playing? y/n: ')   
        if question =="y":
            vs = VideoService()
            vs.open_window()
            syms = Symbols()
        else:
            exit()
        
        # Demonstrate functional video service
        vs.draw_grid(syms)
        sleep(10)
        
        while self.get_direction == True:
            VideoService.draw_grid()
            Symbols(KeyboardService.dx,KeyboardService.dy,(0,0,255,100),'#', False, player=True)
            Symbols.symbols.append()
            Director.update_score = print(f'{self.update_score}')
            
            return VideoService
