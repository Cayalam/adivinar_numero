("//ADIVINA//EL//NUMERO//")

from random import randint 

r=randint(0,18)
ae=input("Quieres jugar: ")
while (0,18):
    usuario=int(input("Ingresa un numero entre el 0 al 18: "))
    if usuario == r:
        f2=("Digiste el numero correcto")
    elif usuario != r:
        f2= ("No querrer@ ese no era el numero")
    print("El resultado es: " + str(f2))
print("Fin del juego")
