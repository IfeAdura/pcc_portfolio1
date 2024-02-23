#number guessing game

import random

def number_guessing_game():

    secret_number = random.randint(1,100)

    print("Welcome to the number guessing game!")
    print("Guess a number between 1 and 100.")

    attempts = 0

    while True:
        guess = int(input("Enter your guess(between 1 and 100): "))

        attempts += 1


        if guess == secret_number:
            print(f"Congratulations! you have guessed the secret number {secret_number} correctly")
            print(f"It took you {attempts} attempts to guess")
            break
        elif guess > secret_number:
            print("too high! Try again.")
        else:
            print("Too low! Try again.")

        if attempts == 5:
            print("You have passed attempts limit.")
            print("Game over!!")
            break

if __name__ == "__main__":
    number_guessing_game()