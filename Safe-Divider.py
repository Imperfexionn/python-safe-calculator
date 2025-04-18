# Basically, a mid-calculator which is "safe".

try:
    # Getting the first number.
    choice = input("Enter a number: ")
    while choice == "" or choice in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a valid first number.")
        choice = input("Enter a number: ")
    choice = int(choice)  # Converting it to number AFTER checking it

    # Getting the second number.
    choice_latter = input("Enter latter number: ")
    while choice_latter == "" or choice_latter in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a valid latter number.")
        choice_latter = input("Enter latter number: ")
    choice_latter = int(choice_latter)  # Convert after checking

    # Getting the operation.
    choice_operation = input("What mathematical operation do you want to perform? [add, sub, multiply, division]: ")
    while choice_operation == "":
        print("Please enter a valid choice selection.")
        choice_operation = input("What mathematical operation do you want to perform? [add, sub, multiply, division]: ")

    # Performing the operation based on user input.
    if choice_operation.lower() == "add":
        choice_add = choice + choice_latter
        print(choice_add)

    elif choice_operation.lower() == "sub":
        choice_sub = choice - choice_latter
        print(choice_sub)

    elif choice_operation.lower() == "multiply":
        choice_mul = choice * choice_latter
        print(choice_mul)

    elif choice_operation.lower() == "division":
        if choice_latter == 0:
            print("You cannot divide by zero.")
        else:
            choice_div = choice / choice_latter
            print(choice_div)
    else:
        print("Invalid operation selected.")

except ValueError:
    print("You cannot enter alphabets or invalid symbols.")

except ZeroDivisionError:
    print("You cannot divide by zero.")