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


# Función que devuelve un diccionario con los tipos de locales y sus lados
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


# Función que devuelve un diccionario con cada local y su envoltura
def getEnvoltura():
    tabla = lectura_datos_csv()
    locales = {}
    envoltura_aux = [fila[2] for fila in tabla]
    envoltura = [envoltura.split("-") for envoltura in envoltura_aux]
    for i, item in enumerate(envoltura):

        locales[i+1] = item

    return locales    


def getDatos():
    tabla = lectura_datos_csv()
    locales = []
    for item in tabla:
        n_locales = item[1].split("-")
        item.remove(item[1])
        item.insert(1, n_locales)
        envoltura = item[2].split("-")
        item.remove(item[2])
        item.insert(2, envoltura)
        locales.append(item)

    return locales  


def consultaLocal(lados_exteriores):
    datos = getDatos()
    locales = []
    for dato in datos:
        if dato[1] == lados_exteriores:
            locales.append(dato[0])

    return locales
