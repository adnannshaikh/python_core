'''
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.The numbers
obtained should be printed in a comma-separated sequence on a single line.
'''

eve_num = list(filter(lambda i: i % 2 ==0,(i for i in range(2000,3001) )))
for i in eve_num:
    print(i,end=',')