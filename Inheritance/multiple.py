#multiple inheritance inherit from more than one parent class
#C(AB)
class Prey:
    def flee(self):
        print("This animal is feeling.")
class Predator:
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):  #multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()