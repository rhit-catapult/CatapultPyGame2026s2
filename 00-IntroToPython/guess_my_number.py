import random


print("Welcome to Guess my Number 1 to 100")
guess_counter = 0
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Make a guess: "))
    guess_counter += 1
    
    if guess == secret_number:
        print(f"You got it! The number was {secret_number}.")
        print(f"It took you {guess_counter} guesses!")
        break
    elif guess < secret_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
