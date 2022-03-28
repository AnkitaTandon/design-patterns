from deco import *
from draw import *

if __name__ == "__main__":
    
    square = square()

    red_square = fill_color(red_shape_dec(square))

    print("square with normal border")
    square.draw()

    print("\nsquare of red border")
    red_square.draw()