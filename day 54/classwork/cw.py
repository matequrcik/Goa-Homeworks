"""შექმენით პროგრამა რომელშიც გექნებათ ხილის სია კალათა (list),
შემდეგ მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი (input),
for ციკლის საშვალებით შეამოწმეთ არის თუ არა ეს ხილი სიაში პირობითი
 განცხადების საშვალებით (if-else), თუ არის დაუბეჭდეთ "Good choice" 
 თუ არ არის "Fruit not in basket"""


bascet=["apple" ,"pineapple", "lemon", "pear"]

favorite= input("what is your favorite fruit?: ")
for fruit in bascet:
    if favorite == bascet:     
        print("good choise")
    else:
        print("Fruit not in basket")


"""შექმენით პროგრამა რომელშიც მომხმარებელს შემოატანინებთ 2 რიცხვს (input),
 შემდეგ პირობითი განცხადებების საშვალებით (if-else) შეამოწმებთ რომელია 
 უდიდესი, შემდეგ უმცირესიდან უდიდესამდე for ციკლის გამოყენებით (for loop) 
 დაბეჭდეთ ყველა რიცხვი და თითეულს გვერდზე მიუწერეთ ლუწია თუ კენტი"""

num=input("enter number: ")
num2=input("enter number: ")

if num < num2 is even :
    print("num < num2 is even")