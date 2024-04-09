from collections import *
#Nos ayuda con la estructura de datos de manera más eficiente. 

#De collection tenemos una funcion llamada counter, ayuda a contar las ocurrencias de un elemento, y lo regresa como0 diccionario. 

numero = [1,2,3,4,5,7,5,4,3,2,1,2,3,4,5,7,8,6,5,4,3,2]

count = Counter(numero)


# Nos ordena el numero más comun al inicio, en caso de poner un argumento dentro de los parentesis, nos dará de resultado las primeras apariciones, como un len de esa lista. 
elmascomun = count.most_common(2)


"Ahora vamos a ocupar una forma de diccionario"

exception = defaultdict(lambda: 'NoEstá')

mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}

