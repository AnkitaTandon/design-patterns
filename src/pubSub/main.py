from pub import *
from sub import *

if __name__ == '__main__':
    pub = Publisher()
 
    ASub = Subscriber('Ankita')
    BSub = Subscriber('Prakash')
 
    pub.subscribe(ASub, 'cats')
    pub.subscribe(ASub, 'dogs')
    pub.subscribe(BSub, 'dogs')
 
    pub.publish('new cats in town!', 'cats')
    pub.publish('a dog named Runo was found at Area 83!', 'dogs')
    print("\n")