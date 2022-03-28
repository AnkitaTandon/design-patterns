from ada import *

if __name__ == "__main__":
    sparrow = sparrow()
    toy_duck = toy_duck()
    bird_adapter = bird_adapter(sparrow)

    print("Sparrow...")
    sparrow.fly()
    sparrow.sing()
  
    print("ToyDuck...")
    toy_duck.squeak()
      
    print("BirdAdapter...")
    bird_adapter.squeak()