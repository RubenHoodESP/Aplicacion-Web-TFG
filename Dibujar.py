import matplotlib.pyplot as plt
import matplotlib.patches as rec
import numpy as np
import Trazador
import Generador
import Analizador


def dibujar_sin_D():

    max_x = int(Analizador.get_max_x())
    max_y = int(Analizador.get_max_y())
    diccionario = [Trazador.trazar_A(), Trazador.trazar_B()]
    figure = 0
    fig = plt.figure(figure)
    ax = fig.add_subplot()
    ax.plot([0, max_x], [0, max_y],
            visible=False)
    plt.gca().invert_yaxis()
    for i in diccionario:
        for j in i:
            lista = i[j]
            x = lista[0]
            y = lista[1]
            anchura = lista[2] - lista[0]
            altura = lista[5] - lista[1]
            borde = rec.Rectangle((0, 0), max_x, max_y,
                                edgecolor='black',
                                fill=False)
            rect = rec.Rectangle((x, y), anchura, altura,
                                edgecolor='black',
                                fill=True)
            ax.add_patch(borde)
            ax.add_patch(rect)
    fig.savefig('FlaskApp/static/imagenes/my_plot_' + str(figure) + '.png')
    figure += 1

    # plt.show()    



def dibujar_con_D():

    max_x = int(Analizador.get_max_x())
    max_y = int(Analizador.get_max_y())
    variantes = Generador.juntar_variantes()
    diccionario = [Trazador.trazar_A(), Trazador.trazar_B(), Generador.generador_D_5()]
    figure = 0
    for variante in variantes:
        diccionario[2] = variante

        fig = plt.figure(figure)
        ax = fig.add_subplot()
        ax.plot([0, max_x], [0, max_y],
                visible=False)
        plt.gca().invert_yaxis()
        for i in diccionario:
            for j in i:
                lista = i[j]
                x = lista[0]
                y = lista[1]
                anchura = lista[2] - lista[0]
                altura = lista[5] - lista[1]
                borde = rec.Rectangle((0, 0), max_x, max_y,
                                    edgecolor='black',
                                    fill=False)
                rect = rec.Rectangle((x, y), anchura, altura,
                                    edgecolor='black',
                                    fill=True)
                ax.add_patch(borde)
                ax.add_patch(rect)
        fig.savefig('FlaskApp/static/imagenes/my_plot_' + str(figure) + '.png')
        figure += 1

# plt.show() 



def dibujar_final():

    max_x = int(Analizador.get_max_x())
    max_y = int(Analizador.get_max_y())
    variantes = Generador.ejecutar_E()
    diccionario = [Trazador.trazar_A(), Trazador.trazar_B(), Generador.generador_D_5()]
    figure = 0
    for variante in variantes:
        diccionario[2] = variante

        fig = plt.figure(figure)
        ax = fig.add_subplot()
        ax.plot([0, max_x], [0, max_y],
                visible=False)
        plt.gca().invert_yaxis()
        for i in diccionario:
            for j in i:
                lista = i[j]
                x = lista[0]
                y = lista[1]
                anchura = lista[2] - lista[0]
                altura = lista[5] - lista[1]
                borde = rec.Rectangle((0, 0), max_x, max_y,
                                    edgecolor='black',
                                    fill=False)
                rect = rec.Rectangle((x, y), anchura, altura,
                                    edgecolor='black',
                                    fill=True)
                ax.add_patch(borde)
                ax.add_patch(rect)
        fig.savefig('FlaskApp/static/imagenes/my_plot_' + str(figure) + '.png')
        figure += 1

    # plt.show()


# dibujar()
# dibujar_final()


