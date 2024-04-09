#  AHORCADO

#El programa escogera una palabra secreta y el jugador debera adivinar. 
# Se le mostrara en guiones cuantas letras son, si el jugador acierta apareceran las letras acertadas, en caso contrario se le quitara una vida (6 en total)

#Se crea el metodo choice para que el programa escoja una palabra dentro de una lista de palabras creadas al comienzo
# Crear funciones, 

from random import choice

def escoger_palabra(opcion1: list, opcion2: list, opcion3: list):

    seccion = [opcion1,opcion2,opcion3]
    seccion = choice(seccion)

    if seccion == opcion1:
        pista = ('Pista, es un animal')
        palabra = choice(opcion1)
    elif seccion == opcion2:
        pista =  ('Pista, es una fruta')
        palabra = choice(opcion2)
    elif seccion == opcion3:
        pista =  ('Pista, es un pais')
        palabra = choice(opcion3)

    return str(palabra), pista

def cambiar_guiones(palabra: str):

    lista  = []
    lista2 = []
    for letra in palabra:
        lista.append(letra)
        lista2.append('_')
 
    return lista, lista2 


print("Bienvenido al juego del ahorcado, tienes que adivinar la palabra secreta en 6 intentos")

#Definiciones
animales = ['gato','perro','salmon', 'garza', 'pajaro', 'leon', 'pez']
frutas = ['fresa', 'manzana', 'platano', 'mandarina', 'naranja', 'sandia', 'melon']
paises = ['mexico', 'canada', 'brasil', 'colombia', 'argentina', 'peru', 'chile']

#Escoger palabra
palabra, pista = escoger_palabra(animales, frutas, paises)

print(pista)

#Convertir palabra en guiones
lista_letras, lista_guiones = cambiar_guiones(palabra)

longitud = len(lista_letras)

print(f"La palabra que debes adivinar tiene {longitud} letras:)")
print(lista_guiones)
#print(lista_letras)

#Ciclo mientras vidas mayora o igual a 6 o palabra completa
intentos = 0
flag = True #Se le llama flag/bandera y significa en este caso que se acabo el juego
resultado = False

while(intentos < 6 and flag == True):

    letra = input("Dime una letra: ").lower()
    
    #Comparar palabra con lista
    if letra in lista_letras: #Sustituir guiones por letras
        #print('sustiuir')
        indices = [indice for indice, dato in enumerate(lista_letras) if dato == letra]
        #print(indices)

        for i in indices:
            lista_guiones[i] = letra

        print('Muy bien sigue asi')
        print(lista_guiones)

    else: #Restar vida
        intentos = intentos + 1
        print(f'ERROR te quedan {6-intentos}')
    
    #Condicion de victoria
    if lista_guiones == lista_letras:
        flag = False
        resultado = True

#Termino del juego
if resultado == True:
    print(f"Felicidades ganaste el juego tu palabra es {palabra.upper()}")
else:
    print(f"Perdiste puñetas, tu palabra era {palabra.upper()}")