#Nos va dndo un valor que se va a ir guardando, pero sin guardar espacio en el ordenador. 
# Va a seguir una secuencia, y va soltando los valores a medida que se vayan solicitando. 

#Generador de turnos. 

from decorators import *

@cuadro
def turn(option:int):
    
    for x in range(1,1001):

        if option == 1:
            if x in range(1,10):
                yield print(f"P-00{x}")
            elif x in range(10,100):
                yield print(f"P-0{x}")
            elif x in range(100,1000):
                yield print(f"P-{x}")
        if option == 2:
            if x in range(1,10):
                yield print(f"F-00{x}")
            elif x in range(10,100):
                yield print(f"F-0{x}")
            elif x in range(100,1000):
                yield print(f"F-{x}")
        if option == 3:
            if x in range(1,10):
                yield print(f"M-00{x}")
            elif x in range(10,100):
                yield print(f"M-0{x}")
            elif x in range(100,1000):
                yield print(f"M-{x}")
            
perfume = turn(1)
farmacia  = turn(2)
maquillaje  = turn(3)

next(perfume)
next(farmacia)
next(maquillaje)
next(perfume)
next(farmacia)
next(maquillaje)
next(perfume)
next(farmacia)