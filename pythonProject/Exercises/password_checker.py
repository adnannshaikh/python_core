name = input("Enter your name: ")
password = input("Enter your password: ")
pass_len = len(password)
print(f"{name},your password {'*' * pass_len} is {pass_len} letters long")