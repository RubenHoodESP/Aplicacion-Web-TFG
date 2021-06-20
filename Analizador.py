from csv import reader


# Función que lee una tabla de datos de un fichero CSV
def lectura_datos_csv():
    with open('datos/datos.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)
        tabla = list(csv_reader)
        
        return tabla


# Función que lee una tabla de datos de un fichero CSV
def lectura_planta_csv():
    with open('datos/planta.csv', 'r') as csv_file:
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


# Devuelve los datos del local consultado
def datosLocal(local):
    tabla = lectura_datos_csv()
    for item in tabla:
        
        if local in item[0]:
            datos = item

    return datos


# Devuelve los datos de los locales de un lado
# exterior concreto
def datosLadoExterior_D(lado):
    tabla = lectura_datos_csv()
    datos = []
    for item in tabla:
        if lado in item[1] and len(item[1]) == 1:
            datos.append(item)

    return datos


# Devuelve el número de locales exteriores totales
def numeroLocales():
    tabla = lectura_datos_csv()
    cont = 0
    for fila in tabla:
        if '0' not in fila [1]:
            cont += 1

    return cont


# Devuelve una lista con los datos de los locales interiores
def datosLocalesInteriores():
    tabla = lectura_datos_csv()
    datos = []
    for fila in tabla:
        if (len(fila[1]) == 1) and ('0' in fila[1]):
            datos.append(fila)

    return datos


# Función que devuelve el tipo de local
def getTipoLocal(local):
    datos = datosLocal(local)
    envoltura = datos[1]
    if len(envoltura) == 5:
        return "A"
    
    elif len(envoltura) == 3:
        return "B"

    elif ((len(envoltura) == 1) and ('0' not in envoltura)):
        return "D"

    elif ((len(envoltura) == 1) and ('0' in envoltura)):
        return "E"


def checkLocalesD():
    tabla = lectura_datos_csv()
    for fila in tabla:
        lados = fila[1]
        if len(lados) == 1:
            return True

    return False


def checkLocalesE():
    tabla = lectura_datos_csv()
    for fila in tabla:
        lados = fila[1]
        if ((len(lados) == 1) and ('0' in lados)):
            return True

    return False

def get_max_x():
    aux = lectura_planta_csv()
    result = aux[0]
    return result[0]

def get_max_y():
    aux = lectura_planta_csv()
    result = aux[0]
    return result[1]

print(get_max_x())
print(get_max_y())