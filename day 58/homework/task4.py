"""4) დაწერეთ ფუნქცია სადაც მომხმარებელს გამოაცნობინებთ რიცხვს თუ რიცხვს გამოიცნობს დაუწერეთ “სწორია ყოჩაღ!” სხვა შემთხვევაში “არასწორია, თავიდან სცადე”"""
def stgj():
    num1=int(input("enter 1 digit code: "))
    if num1 == 7:
        print("correct password")
    else:
        print("incorrect password try again")

stgj()
