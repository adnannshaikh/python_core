'''
Please write a program to generate a list with 5 random numbers between 100 and 200
inclusive.
'''
import random

li = random.sample(range(100,201),5)
print(li)