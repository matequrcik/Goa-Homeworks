import random
option=["rock","paper","scissors"]
rps=input("rock, paper, or scissors?: ")

computer=random.choice(option)

print(computer)
if computer == "paper" and rps == "rock":
    print("computer wins")

elif computer == "paper" and rps == "paper":
    print("tie")

elif computer == "paper" and rps == "scissors":
    print("you win")

elif computer == "rock" and rps == "scissors":
    print("computer wins")

elif computer == "rock" and rps == "paper":
    print("you win")

elif computer == "rock" and rps == "rock":
    print("tie")

elif computer == "scissors" and rps == "scissors":
    print("tie")

elif computer == "scissors" and rps == "rock":
    print("you win")

elif computer == "scissors" and rps == "paper":
    print("computer wins")
else:
    print("wrong option")