import random


rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

your_choice = int(input(
"choose 0 for rock, 1 for paper or 2 for scissors:
\n"))
computer_choice = random.randint(0,2)
if your_choice >=3:
    print("you lose,",end="")
else:
    game_choice = [rock,paper,scissors]
    print(game_choice[your_choice])
    print("computer choose:")
    print(game_choice[computer_choice])

if your_choice >= 3:
    print(" do not go beyond 2")
elif your_choice == computer_choice:
    print("tie,choose again")
elif your_choice == 1 and computer_choice == 0:
    print("you lose")
elif your_choice == 0 and computer_choice == 1:
    print("you win")
elif your_choice == 2 and computer_choice == 1:
    print("you win")
elif your_choice == 0 and computer_choice == 2:
    print("you win")
elif your_choice < computer_choice:
    print("you lose")
elif your_choice > computer_choice:
    print("you lose")
