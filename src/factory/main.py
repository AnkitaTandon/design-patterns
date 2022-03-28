from fac import *

if __name__ == "__main__":
    lang = input("Select a lang (eng/hindi/french): ")
    obj = Factory.abc(lang)
    obj.say_hi()