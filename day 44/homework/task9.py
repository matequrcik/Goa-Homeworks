"""5) Write a while loop that repeatedly asks the user to enter a password 
until the correct password "password123" is entered."""

password="password123"
guess=input("enter password: ")
while guess != password:
    guess=input("enter password: ")
print("correct!")