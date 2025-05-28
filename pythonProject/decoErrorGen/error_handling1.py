while True:
    try:
        age = int(input("Please Enter your age:"))
        10/age
    except ValueError:
        print("Enter a number not a stringa")
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
    else:
        print("Thankyou!!!")
        break