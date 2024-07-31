num = int(input("Ingresar num: "))
contador = 1
i = 2
while i <= num:
    if num % i == 0: 
        contador += 1
        i += 1
    else: 
        i +=1
    
if num == 1: 
    print("NO PRIMO")
elif contador == 2: 
    print("PRIMO")
else : 
    print("NO PRIMO")

    