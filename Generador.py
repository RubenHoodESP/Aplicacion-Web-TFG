from types import MappingProxyType
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

    # Devolvemos una lista con los locales de distancia
    # mínima opuestos
    return lista_resultado



# Variante 1: lados 1 y 3 al medio
def generador_D_1(trazo_D):
    
    # Variables comunes
    comparador = comparador_envolturas()
    datos_local = Analizador.datosLocal(comparador[0])
    aux = Analizador.lectura_planta_csv()
    maximos = aux[0]
    max_x = int(maximos[0]) 
    

    # Compruebo si hay locales de camino mínimo
    if (len(comparador_envolturas()) > 0):

        # Saco los lados de los locales y su lado opuesto
        lado_exterior = datos_local[1]
        lado_exterior_op = str((int(lado_exterior) + 2) % 4)
        
        # Consigo los datos del lado exterior y de su opuesto
        datos_lado_exterior = Analizador.datosLadoExterior_D(lado_exterior)
        datos_lado_exterior_op = Analizador.datosLadoExterior_D(str(lado_exterior_op))

        for datos_local in datos_lado_exterior:

            if datos_local[1] == '1':

                trazo = trazo_D
                trazado = trazo_D[int(datos_local[0])]

                trazado[2] = trazado[6] = max_x / 2
                trazo[int(datos_local[0])] = trazado

                for datos_local_op in datos_lado_exterior_op:

                    trazado_1_op = trazo_D[int(datos_local_op[0])]
                    trazado_1_op[0] = trazado_1_op[4] = max_x / 2
                    trazo[int(datos_local_op[0])] = trazado_1_op

                return trazo



# Variante 2: lado 1 full
def generador_D_2(trazo_D):
    
    # Variables comunes
    comparador = comparador_envolturas()
    datos_local = Analizador.datosLocal(comparador[0])
    aux = Analizador.lectura_planta_csv()
    maximos = aux[0]
    max_x = int(maximos[0])
    n_locales = Analizador.n_locales()    
    

    # Compruebo si hay locales de camino mínimo
    if (len(comparador_envolturas()) > 0):

        # Saco los lados de los locales y su lado opuesto
        lado_exterior = datos_local[1]
        
        # Consigo los datos del lado exterior y de su opuesto
        datos_lado_exterior = Analizador.datosLadoExterior_D(lado_exterior)

        for datos_local in datos_lado_exterior:

            if (datos_local[1] == '1'):

                trazo = trazo_D
                trazado = trazo_D[int(datos_local[0])]

                trazado[2] = trazado[6] = max_x - max_x / max(int(n_locales["N2"]), int(n_locales["N4"]))
                trazo[int(datos_local[0])] = trazado

                return trazo



# Variante 3: lado 2 full
def generador_D_3(trazo_D):
    
    # Variables comunes
    locales = Analizador.consultaLocal(["2"])
    datos_local = Analizador.datosLocal(locales[0])
    aux = Analizador.lectura_planta_csv()
    maximos = aux[0]
    max_y = int(maximos[1])
    n_locales = Analizador.n_locales()
    
    
    # Consigo los datos del lado exterior y de su opuesto
    datos_lado_exterior = Analizador.datosLadoExterior_D("2")

    for datos_local in datos_lado_exterior:
        if datos_local[1] == '2':

            trazo = trazo_D
            trazado = trazo_D[int(datos_local[0])]

            trazado[5] = trazado[7] = max_y - max_y / max(int(n_locales["N1"]), int(n_locales["N3"]))
            trazo[int(datos_local[0])] = trazado

        elif datos_local[1] == '4':

            trazo = trazo_D
            trazado = trazo_D[int(datos_local[0])]

            trazado[1] = trazado[3] = max_y / max(int(n_locales["N1"]), int(n_locales["N3"]))
            trazo[int(datos_local[0])] = trazado

        return trazo



# Variante 4: lado 3 full
def generador_D_4(trazo_D):
    
    # Variables comunes
    comparador = comparador_envolturas()
    datos_local = Analizador.datosLocal(comparador[0])
    aux = Analizador.lectura_planta_csv()
    maximos = aux[0]
    max_x = int(maximos[0])
    n_locales = Analizador.n_locales()    
    

    # Compruebo si hay locales de camino mínimo
    if (len(comparador_envolturas()) > 0):

        # Saco los lados de los locales y su lado opuesto
        lado_exterior = datos_local[1]
        lado_exterior_op = str((int(lado_exterior) + 2) % 4)
        
        # Consigo los datos del lado exterior y de su opuesto
        datos_lado_exterior = Analizador.datosLadoExterior_D(lado_exterior)
        datos_lado_exterior_op = Analizador.datosLadoExterior_D(str(lado_exterior_op))

        for datos_local in datos_lado_exterior_op:

            if datos_local[1] == '3':

                trazo = trazo_D
                trazado = trazo_D[int(datos_local[0])]

                trazado[0] = trazado[4] = max_x / max(int(n_locales["N2"]), int(n_locales["N4"]))
                trazo[int(datos_local[0])] = trazado

        return trazo

def generador_D_5(trazo_D):

    return trazo_D

def juntar_variantes():
    
    variantes = [generador_D_1(Trazador.trazar_D()), generador_D_2(Trazador.trazar_D()),
    generador_D_3(Trazador.trazar_D()), generador_D_4(Trazador.trazar_D()), generador_D_5(Trazador.trazar_D())]

    return variantes


print("generador D1: \n", generador_D_1(Trazador.trazar_D())[2])
print("todas variantes: \n", juntar_variantes())