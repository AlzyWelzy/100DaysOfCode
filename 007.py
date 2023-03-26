while True:
    num_1 = input("Enter a number: ")
    num_2 = input("Enter another number: ")

    operations = ["add", "subtract", "multiply", "divide"]
    print("Operations: " + ", ".join(operations))
    userChoice = input("Enter an operation: ")

    if (
        userChoice not in operations
        or num_1.isdigit() == False
        or num_2.isdigit() == False
    ):
        print("Invalid operation.")
        continue

    if userChoice == "add":
        result = int(num_1) + int(num_2)

    if userChoice == "subtract":
        result = int(num_1) - int(num_2)

    if userChoice == "multiply":
        result = int(num_1) * int(num_2)

    if userChoice == "divide":
        result = int(num_1) / int(num_2)

    print("Result for " + userChoice + " is " + str(result))

    if input("Do you want to continue? (y/n): ") == "n":
        exit()
