import matplotlib.pyplot as plt
import matplotlib.patches
import numpy as np
import Trazador


def dibujar(diccionario):
    for punto in diccionario:
        lista = diccionario[punto]
        anchura = lista[2] - lista[0]
        altura = lista[3] - lista[1]
        

        print(anchura)
        print(altura)
        print(diccionario[punto])
        print(punto)
        


trazo = Trazador.trazar_B()
dibujar(trazo)
# dibujar(trazo)