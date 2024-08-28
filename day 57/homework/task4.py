"""4) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს და შემდეგ კი დააბრუნებს დაბეჭდავს მომხმარებლის შემოტანილი რიცხვი კენტია თუ ლუწი"""

def number():
    numa=int(input("number:"))
    if numa % 2 == 0:
        print("number is even")
    else:
        print("number is odd")