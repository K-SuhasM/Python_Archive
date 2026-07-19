
import random
l= ["1","2","3"]
while True:
    print("Choose:   1. Rock    2. Paper    3. Scissors \nInput any other number to stop.")
    choice=input("Enter your choice: ")
    if choice not in ("1","2","3"):
        raise ValueError("Please choose from the given options.\n 1. Rock    2. Paper    3. Scissors")
#Human choses rock
    if choice=="1":
        com=random.choice(l)
        if com=="1":
            print("\nComputer chose ROCK\nUser chose ROCK\nIts a Draw!!!\n")
        elif com=="2":
            print("\nComputer chose PAPER\nUser chose ROCK\nComputer Wins!!!\n")
        elif com=="3":
            print("\nComputer chose SCISSORS\nUser chose ROCK\nUser Wins!!!!!!\n")
#Human choses paper
    if choice=="2":
        com=random.choice(l)
        if com=="2":
            print("\nComputer chose PAPER\nUser chose PAPER\nIts a Draw!!!\n")
        elif com=="1":
            print("\nComputer chose ROCK\nUser chose PAPER\nUser Wins!!!\n")
        elif com=="3":
            print("\nComputer chose SCISSORS\nUser chose PAPER\nComputer Wins\n")   
#Human choses scissors
    if choice=="3":
        com=random.choice(l)
        if com=="3":
            print("\nComputer chose SCISSORS\nUser chose SCISSORS\nIts a Draw!!!\n")
        elif com=="1":
            print("\nComputer chose ROCK\nUser chose SCISSORS\nComputer Wins,\n")
        elif com=="2":
            print("\nComputer chose PAPER\nUser chose SCISSORS\nUser Wins!!!!!!\n") 

