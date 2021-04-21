from csv import reader


# Función que lee una tabla de datos de un fichero CSV
def lectura_datos_csv():
    with open('datos.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)
        tabla = list(csv_reader)
        return tabla


# Función que lee una tabla de datos de un fichero CSV
def lectura_planta_csv():
    with open('planta.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)
        tabla = list(csv_reader)
        return tabla


# Función que devuelve una lista con las posiciones de los locales
# en orden. Primero A, B, D y finalmente E
"""def ordenar():
    tabla = lectura_csv()
    n_local = 0
    orden_locales = []
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    print(lados_ext)
    for i in lados_ext:
        if len(i) == 3:
            orden_locales.append(n_local)
        n_local += 1
    n_local = 0
    for i in lados_ext:
        if len(i) == 2:
            orden_locales.append(n_local)
        n_local += 1
    n_local = 0
    for i in lados_ext:
        if len(i) == 1:
            orden_locales.append(n_local)
        n_local += 1
    return orden_locales
    """


def clasificador():
    tabla = lectura_datos_csv()
    clasificacion = {}
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    locales_A = [i for i in lados_ext if len(i) == 3]
    locales_B = [i for i in lados_ext if len(i) == 2]
    locales_D = [i for i in lados_ext if len(i) == 1 and "0" not in i]
    locales_E = [i for i in lados_ext if len(i) == 1 and "0" in i]
    clasificacion["A"] = locales_A
    clasificacion["B"] = locales_B
    clasificacion["D"] = locales_D
    clasificacion["E"] = locales_E
    return clasificacion


# Función que calcula el número de locales que tienen un mismo lado
# exterior para cada uno de los lados exteriores existentes
def n_locales():
    tabla = lectura_datos_csv()
    num_locales = [0, 0, 0, 0]
    locales = {}
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    for i in lados_ext:
        for j in i:
            if "1" in j:
                num_locales[0] += 1
            elif "2" in j:
                num_locales[1] += 1
            elif "3" in j:
                num_locales[2] += 1
            elif "4" in j:
                num_locales[3] += 1
    locales["N1"] = num_locales[0]
    locales["N2"] = num_locales[1]
    locales["N3"] = num_locales[2]
    locales["N4"] = num_locales[3]
    return locales


print("LEEMOS TABLA DE DATOS:")
print(lectura_datos_csv())
print("\n Nº LOCALES POR LADO: N1, N2, N3 Y N4")
print(n_locales())
print("\n CLASIFICAMOS LOS DATOS:")
print(clasificador())

