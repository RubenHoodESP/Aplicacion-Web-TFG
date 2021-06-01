import matplotlib.pyplot as plt
import matplotlib.patches as rec
import numpy as np
import Trazador


def dibujar():
    diccionario = [Trazador.trazar_A(), Trazador.trazar_B(), Trazador.trazar_D()]
    print("Diccionario:", diccionario)
    print("Diccionario A:", diccionario[0])
    print("Diccionario B:", diccionario[1])

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot([0, 100], [0, 50],
            visible=False)
    plt.gca().invert_yaxis()
    for i in diccionario:
        for j in i:
            lista = i[j]
            x = lista[0]
            y = lista[1]
            anchura = lista[2] - lista[0]
            altura = lista[5] - lista[1]
            borde = rec.Rectangle((0, 0), 100, 50,
                                  edgecolor='black',
                                  fill=False)
            rect = rec.Rectangle((x, y), anchura, altura,
                                 edgecolor='black',
                                 fill=True)
            ax.add_patch(borde)
            ax.add_patch(rect)
    plt.show()


dibujar()
