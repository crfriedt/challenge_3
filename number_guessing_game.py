# **** Number Guessing Game ****

# Import random library
import random

# Greet user and explain the game
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in 7 attempts.\n")

# Set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# Guessing loop
while guess != the_number and tries < 7:
  if guess > the_number:
    print("Lower...")
  else:
    print("Higher...")
  guess = int(input("Take a guess: "))
  tries += 1

if guess == the_number:
  print("You guessed it! The number was", the_number)
  print("And it only took you", tries, "tries!\n")
  input("\n\nPress the enter key to exit.")
else:
  print("You ran out of tries, the number was", the_number)