'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)
'''

def rangoli(N):
    alph = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    for i in range(N):
        left = alph[N-1:i:-1]
        right = alph[i:N]
        line = '-'.join(left+right)
        lines.append(line.center(4*N-3,'-'))

    print('\n'.join(lines[::-1] + lines[1:]))

rangoli(5)