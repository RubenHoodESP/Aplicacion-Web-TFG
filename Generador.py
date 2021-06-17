import Reparador
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
    reparado = Reparador.reparar_0(Trazador.juntar_locales())
   
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

                # trazo = trazo_D
                # trazado = trazo_D[int(datos_local[0])]
                trazo = reparado
                trazado = reparado[int(datos_local[0])]

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
    reparado = Reparador.reparar_0(Trazador.juntar_locales())
    
    # Compruebo si hay locales de camino mínimo
    if (len(comparador_envolturas()) > 0):

        # Saco los lados de los locales y su lado opuesto
        lado_exterior = datos_local[1]
        
        # Consigo los datos del lado exterior y de su opuesto
        datos_lado_exterior = Analizador.datosLadoExterior_D(lado_exterior)

        for datos_local in datos_lado_exterior:

            if (datos_local[1] == '1'):

                # trazo = trazo_D
                # trazado = trazo_D[int(datos_local[0])]
                trazo = reparado
                trazado = reparado[int(datos_local[0])]

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
    reparado = Reparador.reparar_0(Trazador.juntar_locales())

    # Consigo los datos del lado exterior y de su opuesto
    datos_lado_exterior = Analizador.datosLadoExterior_D("2")

    for datos_local in datos_lado_exterior:
        if datos_local[1] == '2':

            # trazo = trazo_D
            # trazado = trazo_D[int(datos_local[0])]
            trazo = reparado
            trazado = reparado[int(datos_local[0])]

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
    reparado = Reparador.reparar_0(Trazador.juntar_locales())
    
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

                # trazo = trazo_D
                # trazado = trazo_D[int(datos_local[0])]
                trazo = reparado
                trazado = reparado[int(datos_local[0])]

                trazado[0] = trazado[4] = max_x / max(int(n_locales["N2"]), int(n_locales["N4"]))
                trazo[int(datos_local[0])] = trazado

        return trazo


# Variante 5: Estándar
def generador_D_5(trazo_D):

    resultado = Reparador.reparar_0(Trazador.juntar_locales())

    return resultado
    # return trazo_D


# Función que devuelve las coordenadas de todas las variantes de locales D
def juntar_variantes():
    
    variantes = [generador_D_1(Trazador.trazar_D()), generador_D_2(Trazador.trazar_D()),
                generador_D_3(Trazador.trazar_D()), generador_D_4(Trazador.trazar_D()),
                generador_D_5(Trazador.trazar_D())]

    return variantes


# Le paso el local adyacente al que le meto el local interior,
# el local nuevo y la variante

def generador_E_1(parametro):

    local = parametro[0]
    envoltura = parametro[1]
    variante = parametro[2]

    print("VALORES DE PARAMETRO:", local, envoltura, variante)

    trazos_finales = variante
    trazado_nuevo = [0,0,0,0,0,0,0,0]
    trazado_adyacente = variante[int(local)]
    resultado = {}

    print("trazado_adyacente del local: ", local, trazado_adyacente)

    # Comprobamos en qué lado está el local adyacente
    datos = Analizador.datosLocal(local)
    lado = datos[1]

    if lado == '1':

        print("El local", local, "está en el lado 1")
        # Metemos el trazado del local interior nuevo desde la mitad
        # del trazado adyacente al final

        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[2] / 2
        
        # Modificamos el trazado del local adyacente para que
        # quepa el local interior nuevo (mitad)
        trazado_adyacente[2] = trazado_adyacente[6] =  trazado_nuevo[0]

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        print("Resultado de trazos_finales", resultado)
        return resultado

    elif lado == '2':

        print("El local", local, "está en el lado 2")
        # Metemos el trazado del local interior nuevo desde la mitad
        # del trazado adyacente al final
        
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[5] / 2
        
        # Modificamos el trazado del local adyacente para que
        # quepa el local interior nuevo (mitad)
        trazado_adyacente[5] = trazado_adyacente[7] =  trazado_nuevo[1]

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        print("Resultado de trazos_finales", resultado)
        return resultado


    elif lado == '3':

        print("El local", local, "está en el lado 3")
        # Metemos el trazado del local interior nuevo desde la mitad
        # del trazado adyacente al final
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[0] + ((trazado_adyacente[2] -
                                                        trazado_adyacente[0]) / 2)
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]

        # Modificamos el trazado del local adyacente para que
        # quepa el local interior nuevo (mitad)
        trazado_adyacente[0] = trazado_adyacente[4] = trazado_adyacente[0] + ((trazado_adyacente[2] -
                                                        trazado_adyacente[0]) / 2)

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        print("Resultado de trazos_finales", resultado)
        return resultado

    elif lado == '4':

        print("El local", local, "está en el lado 4")
        # Metemos el trazado del local interior nuevo desde la mitad
        # del trazado adyacente al final
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[1] + ((trazado_adyacente[5] -
                                                        trazado_adyacente[1]) / 2)
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]

        # Modificamos el trazado del local adyacente para que
        # quepa el local interior nuevo (mitad)
        trazado_adyacente[1] = trazado_adyacente[3] =  trazado_adyacente[1] + ((trazado_adyacente[5] -
                                                        trazado_adyacente[1]) / 2)

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        print("Resultado de trazos_finales", resultado)
        return resultado
    
    # Devolvemos el nuevo trazado E y trazado de envoltura
    # modificado
    

""" def juntar_variantes_E():
    variantes = juntar_variantes()
    envolturas = Trazador.tratar_envoltura_E()
    todos = []

    for envoltura in envolturas.items():
        print("Añado local: ", envoltura[0])
        
        for local in envoltura[1]:
            i = 0
            print("Estoy en local adyacente: ", local)

            for variante in variantes:
                i += 1
                print("Todas las variantes", variantes)
                print("Estoy en la variante: ", i)
                print("Esta es la variante ->", variante)

                trazado = generador_E_1(local, envoltura[0], variante)
                z = trazado | variante
                print("Trazado resultado:", z)
                todos.append(z)

    return todos """


# Recorro cada local interior y su envoltura para luego
# juntar todos los posibles parámetros y llamar a la función
# generadora de E
def juntar_variantes_E(envoltura, variantes):

    todos = []
    parametros = []

    for local in envoltura[1]:
            # print("Estoy en local adyacente: ", local)
            n_variante = 0

            while n_variante < len(variantes):

                variante = variantes[n_variante]

                # print("Estoy en la variante: ", n_variante + 1)
                # print("Esta es la variante ->", variante)
                parametros.append([envoltura[0], local, variante])
                n_variante += 1

    for parametro in parametros:

        trazado = generador_E_1(parametro)
        z = trazado | variante
        # print("Trazado resultado:", z)

    return z


def ejecutar_E():

    variantes = juntar_variantes()
    envolturas = Trazador.tratar_envoltura_E()

    for envoltura in envolturas.items():
        print("envoltura", envoltura)
        result = juntar_variantes_E(envoltura, variantes)

    return result

# generador_E_1()
# juntar_variantes_E()
ejecutar_E()