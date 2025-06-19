'''
Write a program which accepts a string as input to print "Yes" if the string is "yes"
or "YES" or "Yes", otherwise print "No".
'''

incoming = input("yes or no")

if incoming=='YES' or incoming == 'yes' or incoming=='Yes':
    print("Yes")
else:
    print("No")