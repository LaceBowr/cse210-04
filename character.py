from gems_rocks import Symbol, Gem, Rock

class Character(Symbol):
    score = 0
    def __init__(self, x, y):
        super().__init__(x, y, 'gray', '#')
        
    def character_hit(self, symbols):
        for symbol in symbols.symbols:
            if isinstance(symbol, Character):
                # oh, we iterated over our own position
                continue
            if symbol.x == self.x and symbol.y == self.y:
                # collision
                hit_gem = False
                hit_rock = False
                if isinstance(symbol,Rock):
                    hit_rock = True
                elif isinstance(symbol, Gem):
                    hit_gem = True
                return self.character_score(hit_gem, hit_rock)
        return None

    def character_move(self, direction):
        if self.x == 0 and direction < 0:
            return
        if self.x == 59 and direction > 0:
            return 
        self.x += direction

    

    def character_score(self,player_hit_gem, player_hit_rock):
        if player_hit_gem:
            self.score += 1
        else:
            self.score -= 1
        return self.score
    

    
