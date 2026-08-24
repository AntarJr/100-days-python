import random

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

stages = [

    # 0 lives
    """  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",

    # 1 life
    """  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",

    # 2 lives
    """  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",

    # 3 lives
    """  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",

    # 4 lives
    """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",

    # 5 lives
    """  +---+
  |   |
  O   |
      |
      |
      |
=========""",

    # 6 lives
    """  +---+
  |   |
      |
      |
      |
      |
========="""
]

word_list = ["adventure", "playground", "hoop"]

print("\n" + "=" * 45)
print(logo)
print("=" * 45)
print("              🎮 HANGMAN 🎮")
print("=" * 45)
print("\nWelcome to Hangman!")
print("Guess the word before you run out of lives!")
print()

placeholder = ""

lives = 6

chosen_word = random.choice(word_list)

# print(chosen_word)

count = len(chosen_word)

for i in range(0, count):
    placeholder += "_"

print("WORD:")
print(" ".join(placeholder))
print()
print(f"❤️  Lives: {lives}")
print()

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print("-" * 45)

    guess = input("🎯 Guess a letter: ").strip().lower()

    # Don't lose a life for guessing the same letter again
    if guess in guessed_letters:
        print()
        print("⚠️  You already guessed that letter!")
        print(f"❤️  Lives remaining: {lives}")
        print()
        print(stages[lives])
        continue

    guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:

        if letter == guess:
            display += guess

            if guess not in correct_letters:
                correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print()
    print("WORD:")
    print(" ".join(display))
    print()

    if guess not in chosen_word:
        lives -= 1
        print("❌ Wrong guess!")

    else:
        print("✅ Nice guess!")

    print(f"❤️  Lives remaining: {lives}")
    print()
    print(stages[lives])

    if "_" not in display:
        game_over = True

        print()
        print("=" * 45)
        print("          🎉 YOU WIN! 🎉")
        print("=" * 45)
        print(f"🏆 The word was: {chosen_word}")
        print("Congratulations! You guessed it!")
        print("=" * 45)

    elif lives == 0:
        game_over = True

        print()
        print("=" * 45)
        print("          💀 GAME OVER 💀")
        print("=" * 45)
        print(f"💡 The word was: {chosen_word}")
        print("Better luck next time!")
        print("=" * 45)
        
