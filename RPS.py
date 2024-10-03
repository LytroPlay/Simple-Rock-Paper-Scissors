import random

Opt = ["Rock", "Paper", "Scissors"]
Run = True

while Run:
    n = 0
    player = input("1.Rock\n2.Paper\n3.Scissors\n Pick One : ")
    Bot = random.choice(Opt)

    if player == "1":
        n = 0
    elif player == "2":
        n = 1
    elif player == "3":
        n = 2
    else:
        print("Not Valid")
        break
  
    print(f"\nPlayer = {Opt[n]}")
    print(f"Bot     = {Bot}\n")

    player = Opt[n]

    if player == Bot:
        print("Tied !")
    elif player == "Rock" and Bot == "Scissors":
        print("You WIN !")
    elif player== "Paper" and Bot == "Rock":
        print("You WIN !")
    elif player == "Scissors" and Bot == "Paper":
        print("You WIN !")
    else:
        print("You LOSE !")

    x = input("\nWanna Play again ? (y/n): " ).lower()

    if x == "y":
        continue
    else:
        break

