'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
'''

def divByZero():
   return 5/0


try:
    divByZero()
except ZeroDivisionError as z:
    print("0 can't divide anything bRUHHHH")
except:
    print("Any other exception")
finally:
    print("Try Again")