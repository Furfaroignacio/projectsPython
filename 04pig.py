import random

def roll(): 
    minValue = 1
    maxValue = 6
    roll = random.randint(minValue, maxValue)
    
    return roll

while True:
    players = input("Ingresar la cantidad de jugadores (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else: print("Debe estar entre 2 y 4 jugadores")
    else: 
        print("Invalid, try again")
        
        
maxScore = 50
playerScores = [0 for _ in range(players)]

while max(playerScores)  < maxScore:
    for playerIndex in range(players):
        print("\nComenzo el turno del jugador ", playerIndex + 1)
        print("Tu score total es:", playerScores[playerIndex], "\n")
        currentScore = 0
        while True:
            shouldRoll = input("Te gustaria tirar el dado (y)? ")
            if shouldRoll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("Tiraste un 1, termina el turno!")
                currentScore = 0
                break
            else: 
                currentScore += value   
                print("Tiraste un: ", value, " ")    
            
            print("Tu score actual es: ", currentScore)  
        playerScores[playerIndex] += currentScore  
        print("Tu score total es: ", playerScores[playerIndex])
        
maxScore = max(playerScores)
winningIdx = playerScores.index(maxScore)

print("Jugador numero", winningIdx + 1, "es el ganador con un score de ", maxScore)