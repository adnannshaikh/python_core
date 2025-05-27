some_list = ['a','b','c','b','d','m','n','n']
new_list = []
for i in some_list:
    if some_list.count(i)>1 and i not in new_list:
        new_list.append(i)


print(new_list)