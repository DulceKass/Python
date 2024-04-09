# Son funciones que modifican el comportamiento de otras funciones

# def cuadro(funcion_turno):

#     def wrapper_function(turno):

#         print("-----------------------")
#         print(f"TURNO")
#         funcion_turno(turno)
#         print(f"Gracias por esperar")
#         print("-----------------------")
#         return funcion_turno
#     return wrapper_function

def cuadro(funcion_turno):
    def wrapper_function(*args):
        print("-----------------------")
        print("TURNO")
        generador = funcion_turno(*args)
        for value in generador:  # Iterar sobre el generador para imprimir los valores
            print(value)
        print("Gracias por esperar")
        print("-----------------------")

@cuadro

def saludo(hola):
    if hola==1:
        print("hola")

saludo(1)