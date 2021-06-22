import Analizador


# Reparamos los huecos o solapamientos que haya entre
# locales adyacentes
def reparar_0(trazados):

    numero_locales = Analizador.numeroLocales()

    resultado = {}
    for trazado in trazados.items():
        print("Trazado: \n", trazado)
        datos_local = Analizador.datosLocal(str(trazado[0]))
        lados = datos_local[1]
        if len(lados) == 1:
            lado = lados
            print("Estoy en lado: ", lado)
            if lado == "1":

                local_1 = trazado[0]
                coordenadas_1 = trazado[1]
                local_siguiente_1 = (local_1 + 1) % numero_locales
                if local_siguiente_1 == 0:
                    local_siguiente_1 += 1
                print("Local siguiente: ", local_siguiente_1)
                
                local_previo_1 = (local_1 - 1) % numero_locales
                coordenadas_siguiente_1 = trazados[local_siguiente_1]
                # coordenadas_previo_1 = trazados[local_previo]

                # Comprobar local siguiente
                if ((coordenadas_1[1] != coordenadas_siguiente_1[5]) and
                (coordenadas_1[3] != coordenadas_siguiente_1[7])):

                    coordenadas_1[1] = coordenadas_siguiente_1[5]
                    coordenadas_1[3] = coordenadas_siguiente_1[7]

                    resultado[local_1] = coordenadas_1
                
                else:
                    resultado[local_1] = coordenadas_1

            if lado == "2":

                local_2 = trazado[0]
                coordenadas_2 = trazado[1]
                local_siguiente_2 = (local_2 + 1) % numero_locales
                if local_siguiente_2 == 0:
                    local_siguiente_2 += 1
                print("Local siguiente: ", local_siguiente_2)
                local_previo_2 = (local_2 - 1) % numero_locales
                coordenadas_siguiente_2 = trazados[local_siguiente_2]
                # coordenadas_previo_2 = trazados[local_previo_2]

                # Comprobar local siguiente
                if ((coordenadas_2[2] != coordenadas_siguiente_2[0]) and
                (coordenadas_2[6] != coordenadas_siguiente_2[4])):

                    coordenadas_2[2] = coordenadas_siguiente_2[0]
                    coordenadas_2[6] = coordenadas_siguiente_2[4]

                    resultado[local_2] = coordenadas_2
                
                else:
                    resultado[local_2] = coordenadas_2

            if lado == "3":

                local_3 = trazado[0]
                coordenadas_3 = trazado[1]
                local_siguiente_3 = (local_3 + 1) % numero_locales
                if local_siguiente_3 == 0:
                    local_siguiente_3 += 1
                print("Local siguiente: ", local_siguiente_3)
                local_previo_3 = (local_3 - 1) % numero_locales
                coordenadas_siguiente_3 = trazados[local_siguiente_3]
                # coordenadas_previo_3 = trazados[local_previo_3]

                # Comprobar local siguiente
                if ((coordenadas_3[5] != coordenadas_siguiente_3[1]) and
                (coordenadas_3[7] != coordenadas_siguiente_3[3])):

                    coordenadas_3[5] = coordenadas_siguiente_3[1]
                    coordenadas_3[7] = coordenadas_siguiente_3[3]

                    resultado[local_3] = coordenadas_3

                else:
                    resultado[local_3] = coordenadas_3

            if lado == "4":

                local_4 = trazado[0]
                coordenadas_4 = trazado[1]
                local_siguiente_4 = (local_4 + 1) % numero_locales
                if local_siguiente_4 == 0:
                    local_siguiente_4 += 1
                print("Local siguiente: ", local_siguiente_4)
                local_previo_4 = (local_4 - 1) % numero_locales
                coordenadas_siguiente_4 = trazados[local_siguiente_4]
                # coordenadas_previo_4 = trazados[local_previo_4]

                # Comprobar local siguiente
                if ((coordenadas_4[0] != coordenadas_siguiente_4[2]) and
                (coordenadas_4[4] != coordenadas_siguiente_4[6])):

                    coordenadas_4[0] = coordenadas_siguiente_4[2]
                    coordenadas_4[4] = coordenadas_siguiente_4[6]

                    resultado[local_4] = coordenadas_4

                else:
                    resultado[local_4] = coordenadas_4

    return resultado
