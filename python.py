import random

def game():
    intentos = 0
    adivinado = False
    number_adv = random.randint(1, 100)

    print("Bienvenido al juego de adivinanza mother fucker!!")
    print("Escribe un numero del 1 al 100 pinche vato")

    while not adivinado:
        adivinanza = input("Introduce tu pinche numero putito : ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < number_adv:
                print("El número secreto es MÁS GRANDE que ese, puto")
            elif adivinanza > number_adv:
                print("El número secreto es MÁS CHICO que ese")
            else:
                adivinado = True
                print(f"Lo lograste wachin, el número era {adivinanza} y lo hiciste en {intentos} intentos")
        else:
            print("Poné un número válido, forro")

game()            
