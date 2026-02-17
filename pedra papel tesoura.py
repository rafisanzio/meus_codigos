import random as rng

rock: str = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper: str = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors: str = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
win_msg: str = "You Won!"
lose_msg: str = "You Lose!"

actions: list[str] = [rock, paper, scissors]

player_choice: int = int(input("Type 0 for rock, 1 for paper and 2 for scissors:\n"))
computer_choice: int = rng.randint(0, 2)

print("Your choice:" + actions[player_choice])
print("COM choice:" + actions[computer_choice])

match player_choice:
    case 0:
        if computer_choice == 1:
            print(lose_msg)
        elif computer_choice == 2:
            print(win_msg)
        else:
            print("draw!")
    case 1:
        if computer_choice == 2:
            print(lose_msg)
        elif computer_choice == 0:
            print(win_msg)
        else:
            print("draw!")
    case 2:
        if computer_choice == 0:
            print(lose_msg)
        elif computer_choice == 1:
            print(win_msg)
        else:
            print("draw!")