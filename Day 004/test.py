import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
 '''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
wins = 0
losses = 0
draws = 0

shapes = [rock.strip(), paper.strip(), scissors.strip()]

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if player.isdigit():
    player = int(player)

    if player == 0 or player == 1 or player == 2:
        hand = ["rock", "paper", "scissors"][player]
        print("You chose:")
        print(shapes[player])
    else:
        print("Choice invalid")
        exit()

else:
    print("Please enter a number!")
    exit()

computer = random.randint(0, 2)

pc = shapes[computer]
computer_hand = ["rock", "paper", "scissors"][computer]
 
print(f"Computer chooses:\n{pc}")
  
if player == computer:
        draws += 1
        print("\n====================\n"
            "\nGame Over\n"
              "\n"
              f"You chose : {hand}\n"
              f"computer chose : {computer_hand}\n"
              "\n"
            "It's a draw 🤝"
            "\n====================\n")
elif player == 0 and computer == 2:  
        wins += 1
        print("\n====================\n"
            "\nGame Over\n"
              "\n"
              f"You chose : {hand}\n"
              f"computer chose : {computer_hand}\n"
              "\n"
            "🏆 You win"
            "\n====================\n")
elif player == 1 and computer == 0:  
        wins += 1
        print("\n====================\n"
            "\nGame Over\n"
              "\n"
              f"You chose : {hand}\n"
              f"computer chose : {computer_hand}\n"
              "\n"
            "🏆 You win"
            "\n====================\n")
elif player == 2 and computer == 1: 
        wins += 1
        print("\n====================\n"
            "\nGame Over\n"
              "\n"
              f"You chose : {hand}\n"
              f"computer chose : {computer_hand}\n"
              "\n"
            "🏆 You win"
            "\n====================\n")
else:
        losses +=1
        print("\n====================\n"
            "\nGame Over\n"
        "\n"
              f"You chose : {hand}\n"
              f"computer chose : {computer_hand}\n"
              "\n"
            "💔 You Lose "
            "\n====================\n")

print(f"wins = {wins}\n"
f"losses = {losses}\n"
f"draws = {draws}\n")
