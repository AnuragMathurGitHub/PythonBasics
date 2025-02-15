import random

print("Starting the Guess the Number game...")  # Debug print

secret_number = random.randint(1, 10)
attempts = 0

while True:
    print("Waiting for user input...")  # Debug print
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    print(f"User guessed: {guess}")  # Debug print

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
