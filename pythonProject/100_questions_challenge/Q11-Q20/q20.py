'''
Define a class with a generator which can iterate the numbers, which are divisible
by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14
'''

class RangeDivisible:
    def div_func(self,n):
        for i in range(0,n+1):
            if i % 7 == 0:
                yield i

obj = RangeDivisible()

for i in obj.div_func(14):
    print(i)