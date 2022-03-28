from abc import ABCMeta, abstractstaticmethod

class Lang(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def say_hi():
        pass

class English(Lang):
    def say_hi(self):
        print("Hey Amigo!")

class Hindi(Lang):
    def say_hi(self):
        print("Namaste Dosto!")

class French(Lang):
    def say_hi(self):
        print("Bonjour les amis!")