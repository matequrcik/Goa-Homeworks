#3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.
answer=7
guess=1
guess=int(input("guess the number: "))
while guess != 7:
    guess=int(input("guess the number: "))
print("answer is correct")