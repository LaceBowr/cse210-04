from keyboard_service import KeyboardService
from video_service import VideoService
from character import Character
from symbols import Symbols
from time import sleep

class Director():
    #Keeps track of input, updates, and output and sends them to their needed locations
    '''
    self.update_score
    self.get_input
    self.
    '''
    def __init__(self):
        self.score = 0
        #self.get_input=(int('x'))
        #self.output 

    def get_input(self):
        question = input('Experience the thrill having gems or rocks fall upon you! <i>Greed</i>\nmight seem easy, but even the best treasure-hunter can end up in the wrong place and \nget hit by rocks.\nThe rules are simple.\n The character can move\non the screen trying to dodge or hit the falling objects.\n*If your character(#) move connects with a gem(*) you get a +1 to your score.\n*If the character move connects with a rock you get a -1 to your score.\n\nDo you want to start playing? y/n: ')   
        if question != "y":
            exit()
    
    def falling_movement(self, symbols, vs):
        # go through and adjust the y position of every item in the symbol list
        for symbol in symbols.symbols:
            if isinstance(symbol, Character):
                continue
            if symbol.y < 39:
                symbol.y += 1
            else:
                symbol.y = 0
        # This is tricky, we only update score when we update the players position because
        # the score is stored in the character object.  Of course you can have a hit event
        # when the object fall, so we follow up with a fake player movement with a 0 direction
        # just to detect a collision and update the score
        score = symbols.update_player_position(0)
        if score:
            # we got a score update, because of collision
            vs.set_score(score)

    def start_game(self):    
        # Demonstrate functional video service
        self.get_input()
        vs=VideoService()
        vs.open_window()
        symbols = Symbols()
        ks = KeyboardService()
        totaltime = 0.0
        frame_interval = 0.05
        while vs.game_running():
            vs.draw_grid(symbols)
            xdirection = ks.get_direction()
            if xdirection != 0:
                score = symbols.update_player_position(xdirection)
                if score:
                    # we got a score update, because of collision
                    vs.set_score(score)
            sleep(frame_interval)
            totaltime += frame_interval
            if totaltime > 1.0:
                self.falling_movement(symbols, vs)
                totaltime = 0.0
        vs.close_window()
