"""1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა, მაგალითად მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10"""

def calculator():
    num1=int(input("enter number 1: "))
    num2=int(input("enter number 2: "))
    math_operation=input("enter operation: ")

    if math_operation == "+":
        print(num1 + num2)
    elif math_operation == "-":
        print(num1 - num2)
    elif math_operation == "*":
        print(num1 * num2)
    elif math_operation == "/":
        print(num1 / num2)
    else:
        print("wrong operation")

calculator()
