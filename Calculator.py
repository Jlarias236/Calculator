print("This is a calculator!")

number_1 = float(input("Type the first number: "))
number_2 = float(input("Type the second number: "))
operation = input("Type the operation (+, -, *, /): ")

if operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    print(number_1 / number_2)
elif operation == "+":
    print(number_1 + number_2)
else:
    print(number_1 - number_2)


