# Abstract class: A class that cannot be instantiated on its own; 
# Meant to be subclassed.They can contain abstract methods, which are declared but have no implementation.
# Abstract classes benefits:
#1. Prevents instantiation of the class itself
#2. Requires children to use inherited abstract methods

from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")
class Motercycle(Vehical):
    def go(self):
        print("You ride the motercycle.")

    def stop(self):
        print("You Stop the motercycle.") 
car = Car()
motercycle = Motercycle()
car.go()
car.stop()
motercycle.go()
motercycle.stop()
