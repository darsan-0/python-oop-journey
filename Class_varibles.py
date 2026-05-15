# class variables = Shared among all instances of a class
#Defined outside the constructor
#Allow you to share data among all objects created from that class
class Student:

    passedout_year = 2028 # class variable
    def __init__ (self, name, age):
        self.name = name #instance varibles
        self.age = age #instance varibles
student1 = Student("Spongebob",30)
print(f"{student1.name} \n{student1.age}")
print(student1.passedout_year)
student2 = Student("BatMan",19)
print("---------------------------")
print(f"{student2.name} \n{student2.age}")
print(student2.passedout_year)


#Best acces of class varible is trough class name 
print(Student.passedout_year)