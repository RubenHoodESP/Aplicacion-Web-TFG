import Analizador
import Trazador
import Generador


# Reparamos los huecos o solapamientos que haya entre
# locales adyacentes
def reparar_0(trazados):

    numero_locales = Analizador.numeroLocales()

    print("TODOS: ", trazados)
    for trazado in trazados.items():

        datos_local = Analizador.datosLocal(str(trazado[0]))
        lados = datos_local[1]
        # print(trazado)
        if len(lados) == 1:
            lado = lados

            if lado == "1":
                print(trazado)
                local_1 = trazado[0]
                coordenadas_1 = trazado[1]
                local_siguiente = (local_1 + 1) % numero_locales
                coordenadas_siguiente = trazados[local_siguiente]
                print("siguiente", coordenadas_siguiente)
                local_previo = (local_1 - 1) % numero_locales
                coordenadas_previo = trazados[local_previo]
                print("previo", coordenadas_previo)
                print(local_siguiente)
                print(local_previo)

                # Comprobar local siguiente


                # Comprobar local previo

            if lado == "2":
                print(trazado)
                local_2 = trazado[0]
                coordenadas_2 = trazado[1]

            if lado == "3":
                print(trazado)
                local_3 = trazado[0]
                coordenadas_3 = trazado[1]

            if lado == "4":
                print(trazado)
                local_4 = trazado[0]
                coordenadas_4 = trazado[1]

    

    return 

reparar_0(Generador.juntar_locales())



""" def reparar_1(variantes):

    for variante in variantes:

        print("variante", variante)

        for local in variante.items():

            print("local: ", local)
            datos_local = Analizador.datosLocal(str(local[0]))
            print("datos_local: ", datos_local)
            lado_local = datos_local[1]
            print("lado_local: ", lado_local)

            if lado_local == 1:


            if lado_local == 2:

            if lado_local == 3:

            if lado_local == 4:


        
    return variantes

print(reparar_0(Generador.juntar_variantes())) """