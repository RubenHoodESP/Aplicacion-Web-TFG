import Analizador
import Trazador

def comparador_envolturas():

    
    tabla = Analizador.lectura_datos_csv()
    lista_lado_1 = []
    lista_lado_3 = []
    lista_resultado = []
    for fila in tabla:

        # Sacar una lista de locales de lado exterior 1
        if '1' in fila[1] and len(fila[1]) <= 3:
            lista_lado_1.append(fila)
            
        # Sacar una lista de locales de lado exterior 3
        if '3' in fila[1] and len(fila[1]) <= 3:
            lista_lado_3.append(fila)
    
    for lado_1 in lista_lado_1:
        for lado_2 in lista_lado_3:
            if lado_1[0] in lado_2[2]:
                lista_resultado.append(lado_1[0])
                lista_resultado.append(lado_2[0])

    return lista_resultado

def generador_D():
    tabla = Analizador.lectura_datos_csv()
    lista_resultado = comparador_envolturas()
    if len(lista_resultado) > 0:
        

    return

print(comparador_envolturas())