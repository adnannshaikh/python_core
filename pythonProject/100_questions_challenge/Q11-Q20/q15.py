'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106
'''

num = input("Enter a number: ")
total,temp = 0,str()
for i in range(4):
    temp+=num
    total+=int(temp)

print(total)
