# OOP: Defining Classes and Objects

class Robot:
    """This class implements a Robot."""

    # this is a constructor:
    def __init__(self, name, year): #this is a constructor (a special method)
        self.name = name
        self.year = year



    # destructor:
    #is a special function __del__() that is automatically called when the lifetime of an object ends.
    #the purpose of the destructor is to free the resources that the object may have acquired during its lifetime
    #in Python, destructors aka finalizers are less used, because Python has a garbage collector that handles memory management


r1 = Robot('Robert', 2023) # r1 is an object of the Robot class
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)