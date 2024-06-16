import random
import time


OPERATORS = ["+", "-", "*"]
MINOPERAND = 3
MAXOPERAND = 12
TOTALPROBLEMS = 10


def generateProblem ():
    left = random.randint(MINOPERAND, MAXOPERAND)
    rigth = random.randint(MINOPERAND, MAXOPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(rigth)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Apretar enter para arrancar!")
print("----------------------------")

startTime = time.time()

for i in range(TOTALPROBLEMS):
    expr, answer = generateProblem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr+ " = ")
        if guess == str(answer):
            break
        wrong += 1
        
        
endTime = time.time()

totalTime = round(endTime - startTime, 2)
print("----------------------------")
print("Buen trabajo terminaste en: ", totalTime, " segundos")