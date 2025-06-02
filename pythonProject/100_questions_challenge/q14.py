'''
Write a program that accepts a sentence and calculate the number of upper case
letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''
def case_sent_check(sent):
    upper = 0
    lower = 0
    for char in sent:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return print(f"UPPER CASE {upper}\nlower case {lower}")

case_sent_check("Hello World!")