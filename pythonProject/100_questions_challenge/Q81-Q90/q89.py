'''
Define a class Person and its two child classes: Male and Female. All classes have a
method "getGender" which can print "Male" for Male class and "Female" for Female class.
'''

class Person:
    def __init__(self):
        self.gender =  "unknown"

    def getGender(self):
        print(self.gender)

class Male(Person):
     def __init__(self):
         self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"

human = Male()
human2 = Female()

human.getGender()
human2.getGender()