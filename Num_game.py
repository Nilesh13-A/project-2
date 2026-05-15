import random

print("Number Guessing Game")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess > number:
        print("Too high!")

    elif guess < number:
        print("Too low!")

    else:
        print("Correct! 🎉")
        print("Total attempts:", attempts)
        break

print("Secret number:", number)
