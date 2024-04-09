import re

texto = 'Si necesitas ayuda llama al (658)-589-9977 las 24 horas al servicio de ayuda online'

palabra = 'ayuda' in texto

patron = 'ayuda'

busqueda = re.findall(patron, texto)

texto2 = 'Llama al 555-345-3487 ya mismo'

#Buscaremos si existe un numero telefonico en el texto, en este caso haremos un patron donde haya 3digitos al inicio, ext. 

patron2 = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron2, texto2)

print(resultado)
print(resultado.group())

#Práctica Módulo RE 1

"""Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" 
(entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, 
debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
"""
def verificar_email(email):
    patron = r'\b\w+@\w+(.com)'
    matches = re.search(patron, email)
    
    if matches:
            print('Ok')
    else:
          print('La dirección de email es incorrecta')

email = 'kassandra_21_2@live.com'
verificar_email(email)


#Práctica Módulo RE 2

"""Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". 
Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", 
debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla."""

def verificar_saludo(frase):
    patron = r'^Hola'
    matches = re.search(patron, frase)
    
    if matches:
        print("Ok")
    else:
        print("No has saludado")

frase = 'Hola, me llamo Dulce'

verificar_saludo(frase)

#Práctica Módulo RE 3

"""El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). 
Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto"."""

def verificar_cp(cp):
    patron = r'\D\D\d\d\d\d'
    matches = re.search(patron, cp)
    if matches:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

cp = 'CR0110'

verificar_cp(cp)