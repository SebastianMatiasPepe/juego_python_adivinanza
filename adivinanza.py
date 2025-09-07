import random

def games():
    intentos = 0
    adivinado = False
    number_adv = random.randint(1,100)

    print("Bienvenido al juego de adivinanza mother fucker!!")
    print("Escribe un numero del 1 al 100 pinche vato")

    while not adivinado:

        adivinanza = input("Introduce tu pinche numero :  ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < number_adv :
                 print("El numero secreto es mayor del que pusiste puto")

            elif adivinanza > number_adv:
                 print("el numero secreto es menor ")

            else: 
                print(f"lo Lograste wachin el numero es {adivinanza} y lo hiciste en {intentos} intentos")
    
        else:
          print("Pone un numero forro")        
games()

