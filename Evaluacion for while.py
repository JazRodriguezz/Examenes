import random 

print("En este juego tendras que adivinar un numero entre el 1 y el 100, solo tienes 6 intentos")

num1=random.randint(1,100)   

for i in range (6):
    num2=int(input("ingrese el numero: "))

    if num1==num2:
        print("¡Has adivinado! fin del juego")
        exit()
    elif num1<num2:
        print("demasiado alto")
    elif num1>num2:
        print("demasiado bajo")
    
print("Perdiste, fin del juego")
print ("La respuesta era:",num1)