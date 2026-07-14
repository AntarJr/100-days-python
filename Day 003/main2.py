print(r'''

                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""` 
 ''')

print(
    "Welcome to Treasure Island!\n"
    "Your mission is to find the treasure.\n"
    "You're at a crossroads. Where do you want to go?"
)
direction= input('Type "left" or "right" \n').lower()
if direction == "left" :
    print("You've come to a lake, there is an island in the middle of the lake")
    decision = input('Type "wait" to wait for a boat. Type "Swim" to swim across. \n').lower()
    if decision == "wait" :
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose? \n").lower()
        if door == "yellow":
            print("🎉 Congratulations! You've found the treasure!")
        elif door == "red" :
            print("It's a room full of fire. Game Over.")
        elif door == "blue" : 
            print("You enter a room of beasts. Game Over.")
        else:
            print("Invalid door. GAME OVER")

    elif decision == "swim":
        print("You were eaten by an alligator. GAME OVER")
    else:
        print("Invalid option, GAME OVER")
elif direction == "right":
    print("You fell into a hole. GAME OVER")
else:
    print("Invalid way, GAME OVER")