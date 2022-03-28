from abc import ABCMeta, abstractstaticmethod


class shape(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def draw():
        pass

class square(shape):

    def draw(self):
        print("square done!")