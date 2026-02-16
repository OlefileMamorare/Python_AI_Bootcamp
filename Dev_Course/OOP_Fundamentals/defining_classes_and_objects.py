# OOP: Defining Classes and Objects

from car import Car

class Robot:
    """This class implements a Robot."""

    # Defining class attributes:

    population = 0 # class attribute

    # this is a constructor:
    def __init__(self, name, year): #this is a constructor (a special method)
        self.name = name
        self.year = year
        Robot.population += 1 # increment by 1 each time a new instance is created


    # destructor:
    #is a special function __del__() that is automatically called when the lifetime of an object ends.
    #the purpose of the destructor is to free the resources that the object may have acquired during its lifetime
    #in Python, destructors aka finalizers are less used, because Python has a garbage collector that handles memory management

    # Magic Methods (dunder methods) are always surrounded by double underscores(__)
    # They are special because you do not have to call them directly.
    # The invocation is automatically done by the Python interpreter behind the scenes.

    # defining methods:
    def setEnergy(self, energy):
        self.energy = energy


r1 = Robot('Robert', 2023) # r1 is an object of the Robot class
r2 = Robot('Antonio', 2040)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)

r1.setEnergy(500)
print(r1.energy)

# another way of getting the attribute of an object:
print(getattr(r1, 'energy', 'N/A'))


#Accessing the class attributes:
print(f'Robots alive: {Robot.population}')


# creating a Car Class:



car1 = Car("Toyota", 2025, "red", False)
car2 = Car("Mazda", 2023, "pink", False)


car2.drive()