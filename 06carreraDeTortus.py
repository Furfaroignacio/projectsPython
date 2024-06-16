import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def getNumberOfRacers():
    racers =  0
    while True:
        racers = input("Cuantas tortugas van a participar (2-10):  ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Ingrese un numero... ")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else: 
             print("Numero fuera del rango (2-10). Intentar devuelta")
          
def race(colors):
    turtles = createTurtles(colors)
    
    while True: 
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    
    
def createTurtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        # racer.speed(1)
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
          
def initTurtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Carrera de tortugas")       
   
racers = getNumberOfRacers()
initTurtle()
random.shuffle(COLORS)
colors = COLORS[:racers]


winner = race(colors)

print("EL GANADOR ES EL COLOR: ", winner)
time.sleep(5)


