'''
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.

Example: If the following n is given as input to the program:

7
Then, the output of the program should be:

0,1,1,2,3,5,8,13
'''

def fibo(m):
    if m<2:
        return fibo(m)
    else:
        return fibo(m-1)+fibo(m-2)

n = 7
list = [fibo(n) for i in range(0,n+1)]
print(list)