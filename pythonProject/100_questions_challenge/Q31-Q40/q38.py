'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half
values in one line and the last half values in one line.
'''

tup = (1,2,3,4,5,6,7,8,9,10)
half_length = round(len(tup)/2)
print(tup[0:half_length])
print(tup[half_length:])