dictionary = {
    'a' : 1,
    'b' : 2
}
d2 = [
    {
    'a' : 1,
    'b' : 2,
    'x' : 3
    },
    {
    'a' : 7,
    'b' : [8,2,3],
    'x' : 9
    }
]
print(dictionary['a'])

print(d2[1]['b'][0])

# Dictionary Methods
print(dictionary.get('b'))

print( dictionary.items())