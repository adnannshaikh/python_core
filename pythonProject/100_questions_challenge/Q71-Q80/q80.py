'''
Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
'''

li =  [5,6,77,45,22,12,24]

li2 = [i for i in li if i%2 != 0]

print(li2)


def odd(n):
    return n%2!=0

li_f = list(filter(odd,li))

print(li_f)