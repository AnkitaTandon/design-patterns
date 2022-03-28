from langs import *

class Factory:
    def abc(lang):
        if lang == "eng":
            return English()
        elif lang == "hindi":
            return Hindi()
        else:
            return French()

