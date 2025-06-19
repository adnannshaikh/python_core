'''
Write a program which can map() and filter() to make a list whose elements are square
of even number in [1,2,3,4,5,6,7,8,9,10].
'''

li = [1,2,3,4,5,6,7,8,9,10]
sqr_even = list(filter(lambda i:i%2==0,map(lambda i:i**2,li)))

print(sqr_even)


