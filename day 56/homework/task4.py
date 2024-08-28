"""4) შექმენით კალკულატორის ფუნქცია რომელიც მომხმარებელს ეკითხება ორ რიცხვს და ასევე რა მათემატიკური მოქმედება სურს რომ შესრულდეს, შემდეგ კი ასრულებს მომხმარებლის შემოტანილ რიცხვებზე იმ მოქმედებას რაც მან თქვა"""
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


