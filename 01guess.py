import random

maxNum = input("Ingrese el numero maximo: ")


if maxNum.isdigit():
    maxNum = int(maxNum)
    if maxNum <= 0:
        print("Ingresar un numero mayor a 0")
        quit()
else: 
    print("Ingresar un numero")
    quit()


numeroRandom = random.randint(0 ,maxNum)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Adivina el numero: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else: 
        print("Ingresar un numero")
        continue
    
    if userGuess == numeroRandom:
        print("Adivinaste!")
        break
    elif numeroRandom > userGuess:
            print("Es mas grande que", userGuess)
    else: 
        print("Es mas chico que", userGuess)
        
        
print("Lo sacaste en", guesses, "intentos")