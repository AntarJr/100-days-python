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

shapes = [rock.strip(), paper.strip(), scissors.strip()]

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if player.isdigit():
    player = int(player)

    if player == 0:
        print(rock)
    elif player == 1:
        print(paper)
    elif player == 2:
        print(scissors)
    else:
        print("Choice invalid")
        exit()

else:
    print("Please enter a number!")
    exit()

choice = random.choice(shapes)
pc = shapes.index(choice)

print(f"Computer chooses:\n{choice}")
choice = random.choice(shapes)
pc = shapes.index(choice) 
    
print(f"Computer chooses:\n{choice}")

if player == pc:
        print("It's a draw")
elif player == 0 and pc == 2:  
        print("You win")
elif player == 1 and pc == 0:  
        print("You win")
elif player == 2 and pc == 1: 
        print("You win")
else:
        print("You lose!")

