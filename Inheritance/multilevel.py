# multilevel inheritance inherit from a parent which inherits from another parent
#C(B) <- B(A) <- A
class Animal:
    def __init__(self,name):
        self.name = name 
        
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is feeling.")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):  #multiple inheritance
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()
hawk.eat()
hawk.sleep()
