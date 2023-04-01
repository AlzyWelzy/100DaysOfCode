a = input("Enter a number: ")

if a == "quit":
    print("I won't raise an error.")

elif int(a) < 5 or int(a) > 9:
    raise ValueError("The number is not between 5 and 9")
