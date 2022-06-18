from gems_rocks import Gem, Rock, Symbol
from character import Character

class Symbols():
    symbols = []
    def __init__(self):
        gem_positions = [(13,3),(23,5),(33,8),(4,7),(8,11),(5,15),(11,16),(39,39),(28,31),(59,30),(57,32),(52,25),(55,27),(53,29),(51,30)]
        rock_positions = [(2,2),(6,4),(10,6),(15,9),(5,10),(14,12),(4,14),(22,17),(21,21),(24,22),(58,26),(56,35),(49,31),(54,22),(56,12)]
        self.symbols.append(Character(30,39))
        for rock in rock_positions:
            self.symbols.append(Rock(rock[0],rock[1]))
        for gem in gem_positions:
            self.symbols.append(Gem(gem[0],gem[1]))
            
    def update_player_position(self, xdirection):
        # return score if there is a collision, otherwise it return None
        for symbol in self.symbols:
           if isinstance(symbol, Character):
               symbol.character_move(xdirection)
               return symbol.character_hit(self)
        return None

