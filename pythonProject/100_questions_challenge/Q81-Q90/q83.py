'''
By using list comprehension, please write a program to print the list after removing
the 2nd - 4th numbers in [12,24,35,70,88,120,155].
'''

li = [12,24,35,70,88,120,155]
l = [li[i] for i in range(len(li)) if i<3 or i>4]
print(l)