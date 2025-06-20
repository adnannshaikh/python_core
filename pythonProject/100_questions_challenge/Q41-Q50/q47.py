'''
Define a class named Circle which can be constructed by a radius. The Circle class
has a method which can compute the area.
'''

class Circle():
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    def area(self,):
        return self.pi*(self.radius**2)


c = Circle(5)
print(c.area())

