'''
Write a program which can map() to make a list whose elements are square of elements
in [1,2,3,4,5,6,7,8,9,10].
'''
import math
li = [1,2,3,4,5,6,7,8,9,10]
sqr = list(map(lambda i:i**2,li))

print(sqr)