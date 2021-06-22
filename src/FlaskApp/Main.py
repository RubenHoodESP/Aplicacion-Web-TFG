import Analizador
import Dibujar


def main():
    if (Analizador.checkLocalesD() == False):
        print("Ejecuto sin D\n")
        main = Dibujar.dibujar_sin_D()
    
    elif (Analizador.checkLocalesE() == False):
        print("Ejecuto sin E\n")
        main = Dibujar.dibujar_con_D()

    else:
        print("Ejecuto con E")
        main = Dibujar.dibujar_final()

    return main

main()