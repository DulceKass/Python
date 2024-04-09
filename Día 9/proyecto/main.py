from datetime import *
import os
from time import *
import shutil

#Explorar la carpeta Mi Gran Proyecto, recorrer cada carpeta y cada archivo para encontrar numeros de serie. La manera en  la que se entregara el resultado es: Nombre del archivo : numero de serie, así por cada archivo
# por último se dará el tiempo en que se hizo la busqueda redondeado hacia arriba y la cantidad de numeros de serie encontrados. 

# Para hacer el recorrido de las carpetas y archivos se utilizará la libreria "Shutil" y "OS"
# Para reconocer qué es un número de serie, utilizaremos la libreria "RE" que es para buscar expresiones regulares. 
# Para contabilizar el tiempo en que tardó en hacer la busqueda utilizaremos la librería "Datetime"
#  Para contabilizar la cantidad de numeros de serie localizados utilizaremos la librería Collection

"Usaré diferentes módulos para presentar cada librería, en este caso, este módulo será el MAIN."