'''
Define a class named American which has a static method called printNationality.
'''

class American:

    @staticmethod
    def printNationality():
        return print("American")



am = American()
am.printNationality()
American.printNationality()