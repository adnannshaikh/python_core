'''
Define a custom exception class which takes a string message as attribute
'''

class strError(Exception):
    '''Exception Raise for Custom string

    Attributes:
        Message -- Explaination of error
    '''

    def __init__(self,message):
        self.message = message


num = 'aD'

try:
    try:
        if num<10:
            raise strError("Input is less than 10")
        elif num > 10:
            raise strError("Input is greater than 10")
    except TypeError as TE:
        print(TE)
except strError as se:
    print(f"The error raised: {se.message}")




