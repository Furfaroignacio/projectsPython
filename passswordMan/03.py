from cryptography.fernet import Fernet

'''
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


masterPwd = input("Ingrese la contraseña maestra: ")

key = loadKey() + masterPwd.encode()
fer = Fernet(key)
 



def ver():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Usuario:", user, "| Contraseña:", fer.decrypt(passw.encode()).decode())


#Usamos with para que se cierre automatico el archivo
    #  open('Nombre del archivo', 'modo de abrir w/r/a') 
    #Modos de abrir archivos: w(sobreescribe el archivo), r(Lee el archivo), a(Nos permite agregar algo si exsiste y si no lo crea)
def agregar():
    name = input("Nombre de la cuenta: ")
    pwd = input("Contraseña: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode())
        
        

while True:
    mode = input("Elegir entre ver o agregar contraseñas (ver // agregar)? presionar q para finalizar: ").lower()
    if mode == "q":
        break
    
    if mode == "ver": 
        ver()
    elif mode == "agregar":
        agregar()
  
    else: 
        print("Ingrese una modadalidad correcta.")
        continue