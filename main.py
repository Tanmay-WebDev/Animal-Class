# Animal Class

from abc import ABC , abstractmethod


class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self): 
        print("I can walk and run.")

class Dog(Animal):
    def move(self): 
      print("I can Bark.")

class Snake(Animal):
    def move(self): 
     print("I can crawl.")

class Lion(Animal):
    def move(self): 
        print("I can Roar.")

class Eagle(Animal):
    def move(self): 
        print("I can see people from far.")


H = Human()
H.move()

D = Dog()
D.move()

S = Snake()
S.move()

L = Lion()
L.move()

E = Eagle()
E.move()
