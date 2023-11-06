import random
import time
# we need operators
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


# this is going to generate operators for us
def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    #choice will randomly pick an operator for us
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
# We ask the player to press enter to start the code
input("Press enter to start!")
print("----------------------")

start_time = time.time()

# Generating the number of total problems to solve
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        
        #guessing the problem to solve
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1
# This side explain the time the player starts and end
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")