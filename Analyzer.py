import csv
from csv import reader

# Leemos el csv con los datos
with open('datos.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    next(csv_reader)
    filas = list(csv_reader)
    print(filas)

# Creamos la tabla de datos inicial
lados_ext = []
envoltura = [2, 7]
fila_tabla = [1, lados_ext, envoltura]
tabla = [fila_tabla]
print(tabla)

# def analyzer(tabla):
