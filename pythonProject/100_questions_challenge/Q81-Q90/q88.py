'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
'''

li3 = [12,24,35,24,88,120,155,88,120,155]
li2 = list(set(li3))
print(li2[::-1])

li = [12,24,35,24,88,120,155,88,120,155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)