class User():
    def sign_in(self):
        print('logged in')



class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of{self.power}")

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking with arrows : {self.arrows}")

wizard1 = Wizard('mo',50)
archer1 = Archer('robin',100)

print(wizard1.attack())
print(archer1.attack())

print(isinstance(wizard1,object))


#__________________Polymorphism

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)