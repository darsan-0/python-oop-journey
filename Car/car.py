#This is class
class Car:
    def __init__(self,model,year,color,for_sale): #Dunder method--> Double underscore method
        #__init__()==> It is constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print("You Drive the car!")

    def stop(self):
        print("You Stop the car!")