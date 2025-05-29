import sys
import random
rand = random.randint(1,10)
while True:
    print("Enter the correct number:")
    num = int(input(sys.argv))
    if num == rand:
        print("Congratulations!!!")
        break
    elif num < rand:
        print("your guess is low")
    elif num > rand:
        print("Your guess is higher")