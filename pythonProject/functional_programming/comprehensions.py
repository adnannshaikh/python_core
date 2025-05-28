#List Comprehensions

my_list = [char for char in 'hello']
my_list2 = [i for i in range(100)]
my_list3 = [i*2 for i in range(100)] # Multiplying the expression
my_list4 = [i**2 for i in range(100) if i % 2 != 0]
# print(my_list)
# print(my_list4)

# Set Comprehension

my_set = {i for i in range(10)}
my_set.add(19)
print(my_set)

# Dictionary comprehension

simple_dict = {
    'a':1,
    'b':2
}
my_dict = {k:v * 2 for k,v in simple_dict.items()}

print(my_dict)