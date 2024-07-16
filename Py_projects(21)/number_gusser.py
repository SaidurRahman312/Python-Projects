import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, top_of_range)
#randomint is lower bound inclusive and upper bound exclusive
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue
    if user_guess == random_number:
        print(f"You got it in {guesses} guesses.")
        break
    elif user_guess > random_number:
        print("Make a smaller guess")
    else:
        print("Make a larger guess")

