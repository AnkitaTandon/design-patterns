from draw import *

class shape_decorator(square):

    _dec_shape = square()

    def __init__(self, _dec_shape) :
        self._dec_shape = _dec_shape

    def draw(self):
        self._dec_shape.draw()

class red_shape_dec(shape_decorator):

    def __init__(self, _dec_shape):
        super().__init__(_dec_shape)

    def set_red_border(self):
        print("border color red done!")

    def draw(self):
        self.set_red_border()
        return super().draw()

class fill_color(shape_decorator):

    def __init__(self, _dec_shape):
        super().__init__(_dec_shape)

    def set_red_color(self):
        print("Filled in red color")

    def draw(self):
        self.set_red_color()
        return super().draw()




