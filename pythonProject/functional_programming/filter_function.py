my_list = [2,3,4,5]
def is_odd(li):
    return li % 2 !=0

print(list(filter(is_odd,my_list)))