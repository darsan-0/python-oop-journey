#super() = Function used in a child class to call methods from a parent class (superclass).
#          Allows you to extend the functionality of the inherited methods
class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.is_filled else 'Not filled'}")  

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"It is the circle with area of {3.14 * self.radius**2}cm^2")

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"It is the Square with area of {self.width**2}cm^2")

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"It is the Square with area of {(self.width * self.height)/2}cm^2")

circle = Circle(color="Red",is_filled=True,radius=5)
print(f"{circle.color}\n{circle.is_filled}\n{circle.radius} Cm")
circle.describe()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
square = Square("Blue",False,6)
print(f"{square.color}\n{square.is_filled}\n{square.width} Cm")
square.describe()
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
triangle = Triangle("Yellow",True,5,6)
print(f"{triangle.color}\n{triangle.is_filled}\n{triangle.width} Cm X {triangle.height} Cm")
triangle.describe()
