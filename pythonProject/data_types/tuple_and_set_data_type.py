# my_tuple = (1,2,3,4,5)
# new_tuple = my_tuple[0:3]
# print(new_tuple )


# my_set = {1,2,3,4,5,5}
# my_set.add(2)
# my_set.add(100)
# print(my_set)


my_set = {4,5}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard())
# print(my_set.difference_update(your_set))

# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
print(my_set.union(your_set))

print(my_set.issubset(your_set))
print(your_set.issuperset(my_set))