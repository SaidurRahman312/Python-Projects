name = input("What's your name? ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road, it has come to an end and you can go left or right. Where would you want to go? ").lower()

if answer == "left":
    answer = input("You come to a river, You can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()
    if answer == "swim":
        print("you swam across and were eaten by alligator.")
    elif answer == "walk":
        print("You walk for many miles and ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ")
    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and do u talk to a stranger. Do u talk, yes/no?")
        if answer == "yes":
            print("You talk to the stranger and he gives you Gold. tada! you won.")
        elif answer == "no":
            print("You ignore the stranger and it offends him and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for playing {name}.")

