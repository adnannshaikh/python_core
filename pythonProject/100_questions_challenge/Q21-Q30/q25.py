'''
Define a class, which have a class parameter and have a same instance parameter.
'''

class dog:
    legs = 4
    def __init__(self,name=None,color=None):
        self.name = name
        self.color = color



my_dog = dog('ramesh','blue')

print(my_dog.name)
print(my_dog.color)
print(my_dog.legs)
