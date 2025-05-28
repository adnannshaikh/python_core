def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(10)
next(g)
next(g)
next(g)
print(next(g))

# print(generator_function(100))

# for i in generator_function(100):
#     print(i)

def make_list(num):
    result =[]
    for i in range(num):
        result.append(i)
    return result

# print(make_list(100))