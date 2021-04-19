from csv import reader


def lectura_csv():
    with open('datos.csv', 'r') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)
        tabla = list(csv_reader)
        return tabla


# Ordena lista con los locales A, B, D y E
def ordenar():
    tabla = lectura_csv()
    n_local = 0
    orden_locales = []
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
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


# Calcula el número de locales que tienen un mismo lado
# exterior para cada uno de los lados exteriores existentes
def n_locales():
    tabla = lectura_csv()
    num_locales = [0, 0, 0, 0]
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    print(lados_ext)
    for i in lados_ext:
        if "1" in i:
            num_locales[0] += 1
        elif "2" in i:
            num_locales[1] += 1
        elif "3" in i:
            num_locales[2] += 1
        elif "4" in i:
            num_locales[3] += 1
    return num_locales


print(n_locales())
