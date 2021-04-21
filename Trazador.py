import Analizador


def trazar_A():
    valores = Analizador.lectura_planta_csv()
    aux = valores[0]
    max_x = int(aux[0])
    max_y = int(aux[1])
    clasificacion = Analizador.clasificador()
    locales = Analizador.n_locales()
    if ["1", "2", "3"] in clasificacion["A"]:
        v3x = v1x = v1y = 0.0
        v4x = v2x = max_x
        v2y = v1y
        v4y = v3y = int(max_y) / max(int(locales["N1"]), int(locales["N3"]))
        print("\n RESULTADOS 1,2,3")
        print(v1x), print(v2x), print(v3x), print(v4x), print(v1y), print(v2y), print(v3y), print(v4y)

    elif ["2", "3", "4"] in clasificacion["A"]:
        v1x = v3x = max_x - (max_x / max(int(locales["N2"]), int(locales["N4"])))
        v2x = v4x = max_x
        v1y = v2y = 0.0
        v3y = v4y = max_y
        print("\n RESULTADOS 2,3,4")
        print(v1x), print(v2x), print(v3x), print(v4x), print(v1y), print(v2y), print(v3y), print(v4y)

    elif ["3", "4", "1"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x
        v3y = v4y = max_y
        v2y = v1y = max_y - (max_y / max(int(locales["N1"]), int(locales["N3"])))
        print("\n RESULTADOS 3,4,1")
        print(v1x), print(v2x), print(v3x), print(v4x), print(v1y), print(v2y), print(v3y), print(v4y)

    elif ["4", "1", "2"] in clasificacion["A"]:
        v1x = v3x = 0.0
        v2x = v4x = max_x / max(int(locales["N2"]), int(locales["N4"]))
        v1y = v2y = 0.0
        v3y = v4y = max_y
        print("\n RESULTADOS 4,1,2")
        print(v1x), print(v2x), print(v3x), print(v4x), print(v1y), print(v2y), print(v3y), print(v4y)


def trazar_B():
    valores = Analizador.lectura_planta_csv()
    aux = valores[0]
    max_x = int(aux[0])
    max_y = int(aux[1])
    clasificacion = Analizador.clasificador()
    locales = Analizador.n_locales()
    if ["1", "2"] in clasificacion["B"]:
        v1x = v3x = 0.0
        v1y = v2y = 0.0
    elif ["2", "3"] in clasificacion["B"]:

    elif ["3", "4"] in clasificacion["B"]:

    elif ["4", "1"] in clasificacion["B"]:

trazar_A()
