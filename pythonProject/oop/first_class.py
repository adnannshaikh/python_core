# class BigObject:
#     pass
#
# obj1 = BigObject()
#
# print(obj1)

class PlayerCharacter: # Creating the template for the object
    def __init__(self,name,age):
        self.name = name # attributes
        self.age = age
    def run(self):
       return 'run'


player1 = PlayerCharacter('cindy',23) # Instantiating the Object

print(player1.age,player1.name)