def hightest_even(li):
    li.sort()
    li2 = li[::-1]
    for i in li2:
       if i % 2 == 0:
           return i


print(hightest_even([23,10,2,11,8,6,12]))
