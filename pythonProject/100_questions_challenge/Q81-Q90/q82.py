'''
By using list comprehension, please write a program to print the list after removing
the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''

li = [12,24,35,70,88,120,155]
new_li = []
for i in range(len(li)):
    if i % 2 !=0:
        new_li.append(li[i])

print(new_li)

# sol 2
li = [li[i] for i in range(len(li)) if i%2 != 0 and i <= 6]
print(li)