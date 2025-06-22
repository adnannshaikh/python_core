'''
Write a program to read an ASCII string and to convert it to a unicode string encoded
by utf-8.

Write a special comment to indicate a Python source code file is in unicode.
'''

#-*- coding: utf-8 -*-

s = input()
u = s.encode('utf-8')
print(u)