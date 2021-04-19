import csv
from csv import reader

# Leemos el csv con los datos
with open('datos.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    next(csv_reader)
    tabla = list(csv_reader)
    print("----- TABLA DE DATOS LEÍDA -----")
    print(tabla)

# Extraemos los lados exteriores
lados_aux = [fila[1] for fila in tabla]
lados_ext = [lado.split("-") for lado in lados_aux]
print("----- LISTA DE LADOS EXTERIORES -----")
print(lados_aux)
print(lados_ext)

# Extraemos la envoltura
envoltura_aux = [fila[2] for fila in tabla]
envoltura = [envoltura_aux.split("-") for envoltura_aux in envoltura_aux]
print("----- LISTA DE ENVOLTURAS -----")
print(envoltura_aux)
print(envoltura)


# Clasificación de locales
def clasificador(tabla):
    lados_aux = [fila[1] for fila in tabla]
    lados_ext = [lado.split("-") for lado in lados_aux]
    orden = [orden_locales for orden_locales in lados_ext if len(lados_ext) == 3]
    return orden


print(clasificador(tabla))
# Creamos la tabla de datos inicial


# def analyzer(tabla):
