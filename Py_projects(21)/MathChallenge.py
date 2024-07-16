"""
This script generates a simple arithmetic quiz consisting of 10 problems with random operands (between 3 and 12) 
and operators (+, -, *). The user is prompted to solve each problem, and the script tracks the number of wrong 
attempts and the total time taken to complete the quiz. The quiz starts upon pressing Enter, and the results 
are displayed at the end.
"""

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right= random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press Enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round((end_time - start_time),2)

print("---------------------------")
print(f"no. of wrong attemps = {wrong}")
print(f"Nice work! You finished in {total_time} Seconds!")


