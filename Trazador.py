import Analizador


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

        trazo[lados_ext.index(["1", "2", "3"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["2", "3", "4"] in clasificacion["A"]:
        v1x = v3x = max_x - (max_x / max(int(locales["N2"]), int(locales["N4"])))
        v2x = v4x = max_x
        v1y = v2y = 0.0
        v3y = v4y = max_y
        trazo[lados_ext.index(["2", "3", "4"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["3", "4", "1"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x
        v3y = v4y = max_y
        v2y = v1y = max_y - (max_y / max(int(locales["N1"]), int(locales["N3"])))
        trazo[lados_ext.index(["3", "4", "1"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["4", "1", "2"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x / max(int(locales["N2"]), int(locales["N4"]))
        v1y = v2y = 0.0
        v3y = v4y = max_y
        trazo[lados_ext.index(["4", "1", "2"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
    return trazo


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
        trazo[lados_ext.index(["1", "2"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["2", "3"] in clasificacion["B"]:
        v1x = v3x = max_x - (max_x / int(locales["N2"]))
        v1y = v2y = 0.0
        v2x = v4x = max_x
        v3y = v4y = max_y / int(locales["N3"])
        trazo[lados_ext.index(["2", "3"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["3", "4"] in clasificacion["B"]:
        v1x = v3x = max_x - (max_x / int(locales["N4"]))
        v1y = v2y = max_y - (max_y / int(locales["N3"]))
        v2x = v4x = max_x
        v3y = v4y = max_y
        trazo[lados_ext.index(["3", "4"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["4", "1"] in clasificacion["B"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x / int(locales["N4"])
        v1y = v2y = max_y - (max_y / int(locales["N1"]))
        v3y = v4y = max_y
        trazo[lados_ext.index(["4", "1"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]
    return trazo


def trazar_D():
    valores = Analizador.lectura_planta_csv()
    aux = valores[0]
    max_x = int(aux[0])
    max_y = int(aux[1])
    tabla = Analizador.lectura_datos_csv()
    clasificacion = Analizador.clasificador()
    locales = Analizador.n_locales()
    trazo_A = trazar_A()
    trazo_B = trazar_B()
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    trazo = {}
    # print(trazo_A["A"])

    # print("clasificacion =", clasificacion)
    # print("locales =", locales)
    print("trazo B =", trazo_B)
    print(trazo_B[0])
    print(locales)
    print(lados_ext)
    # print("trazo B =", trazo_B)

    if ["1"] in clasificacion["D"]:
        N1 = locales["N1"]
        aux = trazo_A[5]
        v1_local6_x = aux[0]
        v1_local6_y = aux[1]
        v2_local6_x = aux[2]
        v2_local6_y = aux[3]
        v3_local6_y = aux[5]
        v3x = v1x = 0.0
        v3y = v4y = v1_local6_y
        v1y = v2y = max_y/N1
        v2x = v4x = max_x/N1
        trazo[lados_ext.index(["1"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["2"] in clasificacion["D"]:
        N2 = locales["N2"]
        aux = trazo_B[0]
        v1_local1_x = aux[0]
        v1_local1_y = aux[1]
        v2_local1_x = aux[2]
        # v2_local1_y = aux[3]
        v3_local1_y = aux[5]
        print(v1_local1_x)
        print(v1_local1_y)
        print(v2_local1_x)
        v1x = v3x = v2_local1_x
        v1y = v2y = 0.0
        v2x = v4x = v2_local1_x + max_x/N2
        v3y = v4y = v3_local1_y
        trazo[lados_ext.index(["2"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    if ["3"] in clasificacion["D"]:
        N3 = locales["N3"]
        aux = trazo_B[2]
        v1_local3_x = aux[0]
        v1_local3_y = aux[1]
        v2_local3_x = aux[2]
        v2_local3_y = aux[3]
        v3_local3_x = aux[4]
        v3_local3_y = aux[5]
        v4_local3_x = aux[6]
        v4_local3_y = aux[7]
        v1x = v3x = v1_local3_x
        v2x = v4x = max_x
        v2y = v1y = v4_local3_y
        v4y = v3y = v2y + max_y/N3
        trazo[lados_ext.index(["3"])] = [v1x, v1y, v2x, v2y, v3x, v3y, v4x, v4y]

    # if ["4"] in clasificacion["D"]:

    return trazo


print(trazar_D())
