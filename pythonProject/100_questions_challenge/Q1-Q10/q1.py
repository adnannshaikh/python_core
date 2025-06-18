'''
Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included).The numbers
obtained should be printed in a comma-separated sequence on a single line.
'''

# def div_num(num1,num2):
#     for i in range(num1,num2+1):
#         if i % 7 == 0 and i % 5 != 0:
#             yield i
#
# li = []
# for i in div_num(2000,3200):
#     li.append(i)
#
# print(li)

print(*(i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0),sep=',')