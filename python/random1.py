import random
random_number = int(random.randint(1, 100))
print(random_number)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1;
    if guess == random_number:
        print("You won")
        break
    else:
        print("You failed")

