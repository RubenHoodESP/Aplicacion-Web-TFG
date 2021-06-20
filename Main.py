import Analizador
import Dibujar


def main():
    if (Analizador.checkLocalesD() == False):
        Dibujar.dibujar_sin_D()
    
    elif (Analizador.checkLocalesE() == False):
        Dibujar.dibujar_con_D()

    else:
        Dibujar.dibujar_final()

main()
