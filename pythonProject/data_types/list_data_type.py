li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]

amazon_cart = ['notebooks','sunglasses','toys','grapes']
print(amazon_cart[1])

# list slicing
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'

print(amazon_cart)

# Matrix -> array inside another array

matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
]

print(matrix[0][1])

# List Methods...
# 1) Adding

amazon_cart.append("cars")
amazon_cart.insert(1,2)
amazon_cart.extend(["pen","pencil"])

amazon_cart.pop(1)
amazon_cart.remove("toys")
# amazon_cart.clear()

print(amazon_cart.count('pen'))
print(amazon_cart.index('grapes'))
amazon_cart.sort()
# print(sorted(amazon_cart))
print(amazon_cart)

#---------------------------------------------
regex = "!"

new_sent = regex.join(['hi','my','name','is','jojo'])

print(new_sent)

# List Unpacking

a,b,*c = [1,2,3,4,5,6]
print(a)
print(b)
print(c)
