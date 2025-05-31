'''
Write a program that accepts a sentence and calculate the number of letters and
digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
'''

sent = input()
letter = 0
digits = 0

for char in sent:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digits +=1

print(f"Letters {letter}\ndigits {digits}")