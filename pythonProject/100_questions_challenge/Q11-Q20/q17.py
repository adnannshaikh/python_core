'''
Write a program that computes the net amount of a bank account based a transaction
log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
'''

def trasaction():
    total = 0
    while True:
        response = input("Enter D for deposite or Enter W for withdrawal: ").split()
        if not response:
            break
        dw,num = map(str,response)

        if dw == 'D':
            total+=int(num)
        if dw == 'W':
            total-=int(num)

    return print(total)


trasaction()