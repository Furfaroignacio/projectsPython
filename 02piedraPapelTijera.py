import random

userWins = 0
computerWins = 0 
options = ["piedra", "papel", "tijera"]
while True:
    userInput = input("Escribir Piedra/Papel/Tijera or Q para finalizar: ").lower()
    if userInput == "q":
        break
    #Si no esta en la lista les vuelve a pedir
    if userInput not in options:
        continue 
    
    randomNumber = random.randint(0, 2)
    # piedra: 0 , papel 1, tijera 2
    computerPick = options[randomNumber]
    print("La compuitadora elijio", computerPick + ".")
    
    if userInput == computerPick: 
        print("Empate, se repite")
    elif userInput == "piedra" and computerPick == "tijeras":
        print("Ganaste")
        userWins += 1
        continue
    elif userInput == "papel" and computerPick == "piedra":
        print("Ganaste")
        userWins += 1
        continue
    elif userInput == "tijera" and computerPick == "papel":
        print("Ganaste")
        userWins += 1
        continue
    
    else: 
        print("Perdiste")
        computerWins += 1
        
     
    
print("Ganaste un total de: ", userWins)
print("La computadora gano un total de: ", computerWins)
print("Chau")