'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods
'''

class StringClass:
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

st = StringClass()
st.getString()
st.printString()