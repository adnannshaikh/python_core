'''
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
'''


print(str.__doc__)

def run(dist,speed):
    '''

    :param dist: This is the distance of the run
    :param speed: This is the speed for the run
    :return: distance * Speed
    '''

    return dist * speed

print(run(10,5))
print(run.__doc__)