# WORDLE

def verificador_de_letras_y_posiciones (palabra_secreta,intento_adivinanza):

    for posicion in range(cantidad_de_letras):

        letras_iguales = palabra_secreta[posicion] == intento_adivinanza [posicion]

        existencia_letra = intento_adivinanza[posicion] in palabra_secreta

        if letras_iguales:
            lista_almacenamiento_palabras.append("[" + intento_adivinanza[posicion] + "]")
        elif existencia_letra:
            lista_almacenamiento_palabras.append("(" + intento_adivinanza[posicion] + ")")
        else:
            lista_almacenamiento_palabras.append(intento_adivinanza[posicion])
    return lista_almacenamiento_palabras

def verificador_de_victoria(palabra_secreta,intento_adivinanza):
    return palabra_secreta == intento_adivinanza



print("Bienvenido al juego. Hay una palabra secreta de 5 letras, la cual tenes que intentar adivinar.")
print("Tranqui que a medida que vayas intentando, te vamos a dar pistas. TENES 6 INTENTOS, no los desperdicies.")
print("Las pistas son las siguientes:")
print("- Las letras que esten en (), significa que la letra esta en la palabra, pero no en esa posicion")
print("- Las letras que esten en [], significa que la letra esta en la posicion correcta.")
print("- Las que no tengan nada, significa que la letra no esta en la palabra.")
print("Exitos!!")

intentos = 6
cantidad_de_letras = 5

while True:
    palabra_secreta = input("Ingrese una palabra secreta de 5 letras para el juego.")
    palabra_secreta = palabra_secreta.lower()
    if cantidad_de_letras != len(palabra_secreta):
        palabra_secreta = input("Ingrese una palabra de 5 letras")
    else:
        break

while intentos > 0:

    lista_almacenamiento_victoria = []
    lista_almacenamiento_palabras = []

    intento_adivinanza = input("Ingrese una palabra de 5 letras")
    if len(intento_adivinanza) != cantidad_de_letras:
        print('Ingresa una palabra de 5 letras. Ya perdiste una oportunidad por boludo.')
        continue
    
    intento_adivinanza = intento_adivinanza.lower()

    pistas = verificador_de_letras_y_posiciones(palabra_secreta, intento_adivinanza)
    print(pistas)

    if verificador_de_victoria(palabra_secreta, intento_adivinanza):
        print(f"Felicidades, ganaste!! La palabra secreta era {palabra_secreta}")
        break

    intentos = intentos -1
    print(f"Te quedan {intentos} intentos.")

    if intentos == 0:
        print("Te quedaste sin intentos.")