'''
By using list comprehension, please write a program to print the list after removing
numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''

li = [12,24,35,70,88,120,155]
x = list(filter(lambda y:y%5==0 and y%7==0,li))
print(x)