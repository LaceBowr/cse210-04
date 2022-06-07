import random

colors = ["Red","Grey","Blue","White","Green"]
column = (0,1,2,3,4,5,6,7,8,9)



class NewItem:
    def __init__(self):        
        self.col = random.Random().choice(colors)


    def get_CaptureItem(self):
        if self.col == "Red" or self.col == "Blue" or self.col == "Green":
            ci = Gem(random.choice(column))
            ci.clr = self.col
        else: 
            ci = Rock(random.choice(column))  
            ci.clr = self.col     
        return ci
        
       

class CaptureItem:
    def __init__(self,position,color):
        self.pos = position
        self.clr = color
    
    

class Gem(CaptureItem):
    def __init__ (self,position):
        self.score = 0
        self.pos = position

    def get_score(self):
        if self.clr == "Red":
            return 5
        elif self.clr == "Blue":
            return 3
        else:
            return 1

    def is_hit(self):
        return ScoreResult(self.get_score(), self)
       

class Rock(CaptureItem):
    def __init__ (self,position):
        self.score = 0
        self.pos = position

    

    def get_score(self):
        if self.clr == "White":
            return -2
        else:
            return -1
    
    def is_hit(self):
        return ScoreResult(self.get_score(), self)

class ScoreResult:
    def __init__(self,score,captured):
        self.sc = score
        self.ci = captured


def main():
    newItm = NewItem()
    capturedItm = newItm.get_CaptureItem()
    result = capturedItm.is_hit()
    print("Here are the results:")
    print(f"Score:""{result.sc}")
    print(result.ci.clr)
    

if __name__== "__main__":
    main()