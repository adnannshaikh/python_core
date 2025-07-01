'''
Please write a program which count and print the numbers of each character in a
string input by console.

Example: If the following string is given as input to the program:

abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

def strCount(str):
    c = {}
    for char in str:
        if char not in c:
            c[char]  = 1
        else:
            c[char] += 1
    for i in c:
        print(f"{i},{c[i]}")

strCount('abcdefgabc')

