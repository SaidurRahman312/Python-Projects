print("Welcome to my Computer quiz!")

playing = input("Do u want to play? ").lower()
if playing != 'yes':
    quit()
print("Okay! let's play :) ")

Score = 0

answer = input("What does CPU stand for? ").lower()
if answer == 'central processing unit':
    print("Correct! ")
    Score+=1
else:
    print('Incorrect!')

answer = input("What does GPU stands for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct! ")
    Score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stands for? ").lower()
if answer == 'random access memory':
    print("Correct! ")
    Score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stands for? ").lower()
if answer == 'power supply unit':
    print("Correct! ")
    Score += 1
else:
    print('Incorrect!')

print(f"You got {Score} questions correct!")
print(f"You got {(Score / 4) * 100} % questions correct!")
