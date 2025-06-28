'''
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
'''
import zlib

string = "hello world!hello world!hello world!hello world!"
byt = bytes(string,"utf-8")
x = zlib.compress(byt)
print(x)
print(zlib.decompress(x))