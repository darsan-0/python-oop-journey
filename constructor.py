#This is class
class Car:
    def __init__(self,model,year,color,for_sale): #Dunder method--> Double underscore method
        #__init__()==> It is constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

#Object
Car1 = Car("Mustang", 2026, "Red", False)

#case1
print(Car1) #output: <__main__.Car object at 0x000001AC84791210> memory addres of the Car1 object.
#case2
print(Car1.model) # " . " is Attribute acces operator ,output: Mustang
print(Car1.year)
print(Car1.color)
print(Car1.for_sale)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
