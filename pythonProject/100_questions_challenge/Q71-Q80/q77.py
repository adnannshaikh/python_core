'''
Please write a program to print the running time of execution of "1+1" for 100 times.
'''
import time
before = time.time()
for i in range(1000000000):
    x =  1+1
after = time.time()
et = after - before
print(et)