'''
Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.

'''

def b_search(li,element):
    i = 0
    while i < len(li):
        if element == li[i]:
            return i
        i+=1


li=[2,5,7,9,11,17,222]
print(b_search(li,11))