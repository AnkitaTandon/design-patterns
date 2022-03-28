from bird import *

class bird_adapter(toy_duck):

    def __init__(self,bird):
        self.bird = bird

    def squeak(self):
        self.bird.sing()



