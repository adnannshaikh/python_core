'''
Please write a program which prints all permutations of [1,2,3]
'''
from itertools import permutations
k = [1,2,3]
for i in permutations(k):
    print(list(i))