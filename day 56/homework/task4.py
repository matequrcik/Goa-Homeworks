def calculator ():
    num1 = int(input("enter num: "))
    num2 = int(input("enter num2: "))
    math_operation=input("choose mathematical operation: ")

    if math_operation == "+":
        print(num1 + num2)
        if math_operation == "-":
            print(num1 - num2)
    if math_operation == "*":
            print(num1 * num2)
    if math_operation == "/":
            print(num1 / num2)
    if math_operation == "**":
            print(num1 ** num2)
    if math_operation == "//":
            print(num1 // num2)
    else:
          print("wrong sintax")


