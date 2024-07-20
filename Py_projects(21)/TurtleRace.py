"""
This program simulates a turtle race using the Turtle graphics module in Python.
The user is prompted to enter the number of turtles (racers) participating in the race.
Each turtle is assigned a random color from a predefined list of colors.
The turtles race upwards across the screen, and the first turtle to cross the finish line at the top wins.
The winning turtle's color is then displayed on the screen.
"""
import turtle
import time
import random

# Set the dimensions of the screen
WIDTH, HEIGHT = 700, 600
# List of possible colors for the turtles
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'cyan']

def get_number_of_racers():
    # Function to get the number of racers from the user
    racers = 0
    while True:
        racers = input("Enter the number of turtles (2-10): ")
        if racers.isdigit():  # Check if the input is a digit
            racers = int(racers)
        else:
            print("Please enter a numeric value.")
            continue
        if 2 <= racers <= 10:  # Ensure the number of racers is between 2 and 10
            return racers
        else:
            print("Number not in range (2-10), try again!")

def race(colors):
    # Function to conduct the race
    turtles = create_turtles(colors)  # Create turtle racers

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)  # Move the turtle a random distance
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:  # Check if the turtle has crossed the finish line
                # Return the color of the winning turtle
                return colors[turtles.index(racer)]

def create_turtles(colors):
    # Function to create turtles and set their initial positions
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)  # Calculate spacing between turtles
    for i, color in enumerate(colors):
        racer = turtle.Turtle()  # Create a new turtle
        racer.color(color)  # Set the color of the turtle
        racer.shape("turtle")  # Set the shape of the turtle
        racer.left(90)  # Turn the turtle to face upwards
        racer.penup()
        # Set the initial position of the turtle
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)  # Add the turtle to the list
    return turtles

def init_turtle():
    # Function to initialize the turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)  # Set up the screen dimensions
    screen.title("Turtle Racing!")  # Set the screen title

racers = get_number_of_racers()  # Get the number of racers from the user
init_turtle()  # Initialize the turtle screen

# Shuffle the colors and select the number of colors equal to the number of racers
random.shuffle(COLORS)
colors = COLORS[:racers]
# Conduct the race and get the winner
winner = race(colors)
time.sleep(2)  # Pause the screen for 2 seconds
print(f"The winner is the turtle with the color: {winner}.")  # Print the winner's color
