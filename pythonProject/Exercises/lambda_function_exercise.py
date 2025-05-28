my_list =[ 1,2,3]

#square
print(list(map(lambda item:item**2,my_list)))

#list sorting 2nd value
a = [(0,2),(4,3),(9,9),(10,-1)]
a.sort(key=lambda x:x[1])
print(a)

