print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
print("5. Elevate")
print("6. Exit")

calculator = {
    1: "Add",
    2: "Substact",
    3: "Multiply",
    4: "Divide",
    5: "Elevate",
    6: "Exit"
}
while True:
    Option = input("Please select one of the next option to perform an operation:")
    if Option == "":
        print("You didnt choose any option, please try again and choose an option!")
    else:
        Option = int(Option)
        if Option in calculator:
            print(f"You chose the option of {Option}: {calculator[Option]}")
        else:
            print("You need to chose a value in between 1-5")
        result = 0
        if Option == 1:
        #   perform add operation
            num1 = int(input("Please enter the first number "))
            num2 = int(input("Please enter the second number "))
            result += num1 + num2
            print(f"Result : {result}")
        elif Option == 2:
            #perform substract operation
            num1 = int(input("Please enter the first number "))
            num2 = int(input("Please enter the second number "))
            result += num1 - num2
            print(f"Result : {result}")
        elif Option == 3:
            #perform multiply operation
            num1 = int(input("Please enter the first number "))
            num2 = int(input("Please enter the second number "))
            result += num1 * num2
            print(f"Result: {result}")
        elif Option == 4:
            #perform divide operation
            num1 = int(input("Please enter the first number "))
            num2 = int(input("Please enter the second number "))
            result += num1 / num2
            print(f"Result: {result}")
        elif Option == 5:
            #perform elevate operation
            num1 = int(input("Please enter the first number "))
            num2 = int(input("Please enter the second number "))
            result += num1 ** num2
            print(f"Result: {result}")
        elif Option == 6:
            #perform exit operation
            break