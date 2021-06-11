import Analizador


# Función que calcula las coordenadas de los locales de tipo A
def trazar_A():

    tabla = Analizador.lectura_datos_csv()
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    valores = Analizador.lectura_planta_csv()
    aux = valores[0]
    max_x = int(aux[0])
    max_y = int(aux[1])
    clasificacion = Analizador.clasificador()
    locales = Analizador.n_locales()
    trazo = {}
    if ["1", "2", "3"] in clasificacion["A"]:
        v3x = v1x = v1y = 0.0
        v4x = v2x = max_x
        v2y = v1y
        v4y = v3y = int(max_y) / max(int(locales["N1"]), int(locales["N3"]))

        trazo[lados_ext.index(["1", "2", "3"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["2", "3", "4"] in clasificacion["A"]:
        v1x = v3x = max_x - (max_x / max(int(locales["N2"]), int(locales["N4"])))
        v2x = v4x = max_x
        v1y = v2y = 0.0
        v3y = v4y = max_y
        trazo[lados_ext.index(["2", "3", "4"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["3", "4", "1"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x
        v3y = v4y = max_y
        v2y = v1y = max_y - (max_y / max(int(locales["N1"]), int(locales["N3"])))
        trazo[lados_ext.index(["3", "4", "1"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["4", "1", "2"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x / max(int(locales["N2"]), int(locales["N4"]))
        v1y = v2y = 0.0
        v3y = v4y = max_y
        trazo[lados_ext.index(["4", "1", "2"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    return trazo


# Función que calcula las coordenadas de los locales de tipo B
def trazar_B():

    tabla = Analizador.lectura_datos_csv()
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    valores = Analizador.lectura_planta_csv()
    aux = valores[0]
    max_x = int(aux[0])
    max_y = int(aux[1])
    clasificacion = Analizador.clasificador()
    locales = Analizador.n_locales()
    trazo = {}
    if ["1", "2"] in clasificacion["B"]:
        v1x = v3x = v1y = v2y = 0.0
        v2x = v4x = max_x / int(locales["N2"])
        v3y = v4y = max_y / int(locales["N1"])
        trazo[lados_ext.index(["1", "2"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["2", "3"] in clasificacion["B"]:
        v1x = v3x = max_x - (max_x / int(locales["N2"]))
        v1y = v2y = 0.0
        v2x = v4x = max_x
        v3y = v4y = max_y / int(locales["N3"])
        trazo[lados_ext.index(["2", "3"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["3", "4"] in clasificacion["B"]:
        v1x = v3x = max_x - (max_x / int(locales["N4"]))
        v1y = v2y = max_y - (max_y / int(locales["N3"]))
        v2x = v4x = max_x
        v3y = v4y = max_y
        trazo[lados_ext.index(["3", "4"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["4", "1"] in clasificacion["B"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x / int(locales["N4"])
        v1y = v2y = max_y - (max_y / int(locales["N1"]))
        v3y = v4y = max_y
        trazo[lados_ext.index(["4", "1"])+1] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    return trazo


# Función que calcula las coordenadas de los locales de tipo D
def trazar_D():
    
    # datos para usar
    # clasificacion = Analizador.clasificador()
    # envoltura = Analizador.getEnvoltura()
    n_locales = Analizador.n_locales()
    datos = Analizador.getDatos()
    aux = Analizador.lectura_planta_csv()
    maximos = aux[0]
    max_x = int(maximos[0])
    max_y = int(maximos[1])
    trazados = trazos()
    trazo = {}
    cont_1 = cont_2 = cont_3 = cont_4 = 0

    # Bucle que itera sobre cada fila de la tabla de datos
    for dato in datos:

        # print("Iteramos dato: ", dato)    

        if dato[1] == ["1"]:

            # print("Entramos en lado 1")

            # Guardo su número de local
            numero = int(dato[0])

            # Miro el local anterior
            local = Analizador.consultaLocal(["1"])
            aux = local[cont_1]
            aux2 = int(aux) - 1

            # Coordenadas del local anterior
            coordenadas_anterior = trazados.get(aux2)

            # Calculamos las coordenadas actuales
            v1x = v3x = 0.0
            v3y = v4y = coordenadas_anterior[1]
            v1y = v2y = v3y - max_y/int(n_locales["N1"])

            # handle
            v2x = v4x = max_x / max(int(n_locales["N2"]), int(n_locales["N4"]))

            # Guardamos las coordenadas en trazo
            trazo[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            cont_1 += 1
            
            # print("1_testeo_antes", trazados)
            trazados[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            # print("1_testeo_despues", trazados)


        if dato[1] == ["2"]:

            # print("Entramos en lado 2")

            numero = int(dato[0])
            local = Analizador.consultaLocal(["2"])
            aux = local[cont_2]
            aux2 = int(aux) - 1
            coordenadas_anterior = trazados.get(aux2)
            # print("local anterior!!!!", aux2)

            v1x = v3x = coordenadas_anterior[2]

            # handle
            v3y = v4y = max_y / max(int(n_locales["N1"]), int(n_locales["N3"]))

            v1y = v2y = 0.0
            v2x = v4x = coordenadas_anterior[2] + max_x/int(n_locales["N2"])

            # Guardamos las coordenadas en trazo
            trazo[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            cont_2 += 1

            # print("2_testeo_antes", trazados)
            trazados[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            # print("2_testeo_despues", trazados)


        if dato[1] == ["3"]:

            # print("Entramos en lado 3")

            numero = int(dato[0])

            # Miro el local anterior
            local = Analizador.consultaLocal(["3"])

            aux = local[cont_3]
            aux2 = int(aux) - 1
            coordenadas_anterior = trazados.get(aux2)

            v2x = v4x = max_x

            # handle
            v1x = v3x = max_x - (max_x / max(int(n_locales["N2"]), int(n_locales["N4"])))
            # print("AYYYLMAO", max(int(n_locales["N2"]), int(n_locales["N4"])))

            v2y = v1y = coordenadas_anterior[5]
            v3y = v4y = v2y + max_y/int(n_locales["N3"])
            
            # Guardamos las coordenadas en trazo
            trazo[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            cont_3 += 1

            # print("3_testeo_antes", trazados)
            trazados[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            # print("3_testeo_despues", trazados)


        if dato[1] == ["4"]:

            # print("Entramos en lado 4")

            numero = int(dato[0])
            # Miro el local anterior
            local = Analizador.consultaLocal(["4"])

            aux = local[cont_4]
            aux2 = int(aux) - 1
            coordenadas_anterior = trazados.get(aux2)

            v3y = v4y = max_y
            
            # handle
            v1y = v2y = max_y - (max_y/n_locales["N3"])

            v2x = v4x = coordenadas_anterior[0]
            v1x = v3x = v2x - max_x/int(n_locales["N4"])

            # Guardamos las coordenadas en trazo
            trazo[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            cont_4 += 1

            # print("4_testeo_antes", trazados)
            trazados[numero] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
            # print("4_testeo_despues", trazados)

    return trazo


# TODO
def trazar_E():

    trazo = {}

    return trazo


def trazos():

    trazo_A = trazar_A()
    trazo_B = trazar_B()
    trazos = trazo_A | trazo_B
    
    return trazos

trazar_D()