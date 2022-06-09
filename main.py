import random

player_name = input("Hi, What is your name? ").title()
greeting = print(f'''Ok {player_name}, Welcome to Rock, Paper, Scissors game\n         by Habib Hakeem for Zuri\n
Tips: Rock beats Scissors, Paper beats Rock,\nand Scissors beats paper.\nAre you ready?!\n''')


# Character functions
def cpu_character():
    CPU_choice = random.choice(list(choices.values()))
    if CPU_choice == choices["R"]:
        return "Rock"
    elif CPU_choice == choices["P"]:
        return "Paper"
    elif CPU_choice == choices["S"]:
        return "Scissors"


def player_character():
    while True:
        player_choice = input(f'''Ok {player_name}, It's your move!\nPress:
    'R' for {choices["R"]}
    'P' for {choices["P"]}
    'S' for {choices["S"]}\nWhat is your choice?: ''').upper()
        for choice in player_choice:
            if player_choice == "R":
                choice = choices["R"]
                return choice
            elif player_choice == "P":
                choice = choices["P"]
                return choice
            elif player_choice == "S":
                choice = choices["S"]
                return choice
                # Error Handling
            else:
                if choice != "R" or "P" or "S":
                    print("\nYour entry is invalid, please try again, press 'R', 'P', or 'S'.\n")


while True:
    # List of Choices: I used a dictionary because it is a type of list in python.
    choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    # Player Choices
    player_choices = player_character()
    # CPU choices
    CPU_choices = cpu_character()
    # Moves by player and CPU
    moves = f"Moves:\n{player_name} ({player_choices}) : CPU ({CPU_choices})"
    print(moves)
    # Moves Checker (TIE)
    if player_choices == CPU_choices:
        print(f"{player_name} & CPU chose: (%s), it's a TIE!\nlet's go again for the tie breaker!\n" % CPU_choices)


        def tie_breaker():
            cpu_character()
            player_character()
            if player_choices == "Rock" and CPU_choices == "Scissors":
                print(f"Nice one {player_name}!, You WON the CPU: Rock beats Scissors.")
            elif player_choices == "Paper" and CPU_choices == "Rock":
                print(f"Nice one {player_name}!, You WON the CPU: Paper beats Rock")
            elif player_choices == "Scissors" and CPU_choices == "Paper":
                print(f"Nice one {player_name}!, You WON the CPU: Scissors beats Paper.")
            elif player_choices == "Rock" and CPU_choices == "Paper":
                print(f"Sorry {player_name}, You LOST to the CPU: Paper beats Rock.")
            elif player_choices == "Paper" and CPU_choices == "Scissors":
                print(f"Sorry {player_name}, You LOST to the CPU: Scissors beats Paper")
            elif player_choices == "Scissors" and CPU_choices == "Rock":
                print(f"Sorry {player_name}, You LOST to the CPU: Rock beats Scissors.")
    else:
        # Move Checker (WIN)
        if player_choices == "Rock" and CPU_choices == "Scissors":
            print(f"Nice one {player_name}!, You WON the CPU: Rock beats Scissors.")
        elif player_choices == "Paper" and CPU_choices == "Rock":
            print(f"Nice one {player_name}!, You WON the CPU: Paper beats Rock")
        elif player_choices == "Scissors" and CPU_choices == "Paper":
            print(f"Nice one {player_name}!, You WON the CPU: Scissors beats Paper.")
        # Move Checker (LOSE)
        elif player_choices == "Rock" and CPU_choices == "Paper":
            print(f"Sorry {player_name}, You LOST to the CPU: Paper beats Rock.")
        elif player_choices == "Paper" and CPU_choices == "Scissors":
            print(f"Sorry {player_name}, You LOST to the CPU: Scissors beats Paper")
        elif player_choices == "Scissors" and CPU_choices == "Rock":
            print(f"Sorry {player_name}, You LOST to the CPU: Rock beats Scissors.")
        # Restart Game
        restart = input("\nPlay again? Press 'Y' for Yes, 'any button' for No. __")
        if restart != "Y".lower():
            print(f"\nOk {player_name}, That was an awesome game,\nhope to play with you again soon!\nThe End. ")
            break
