import matplotlib.pyplot as plt
import matplotlib.patches as rec
import numpy as np
import Trazador
import Generador


def dibujar():

    variantes = Generador.juntar_variantes()
    print("aaaaayyy", variantes)
    diccionario = [Trazador.trazar_A(), Trazador.trazar_B(), Generador.generador_D_5(Trazador.trazar_D())]
    figure = 0
    for variante in variantes:
        diccionario[2] = variante

        print("variante \n", variante)

        fig = plt.figure(figure)
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
        fig.savefig('my_plot_' + str(figure) + '.png')
        figure += 1

    plt.show()    


dibujar()
