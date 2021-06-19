from numpy import result_type
import Reparador
from types import MappingProxyType
import Analizador
import Trazador
import Variantes

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
def generador_D_1():
    
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

                    trazado_1_op = reparado[int(datos_local_op[0])]
                    trazado_1_op[0] = trazado_1_op[4] = max_x / 2
                    trazo[int(datos_local_op[0])] = trazado_1_op

                return trazo



# Variante 2: lado 1 full
def generador_D_2():
    
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
def generador_D_3():
    
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

            trazo = reparado
            trazado = reparado[int(datos_local[0])]

            trazado[1] = trazado[3] = max_y / max(int(n_locales["N1"]), int(n_locales["N3"]))
            trazo[int(datos_local[0])] = trazado

        return trazo



# Variante 4: lado 3 full
def generador_D_4():
    
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
def generador_D_5():

    resultado = Reparador.reparar_0(Trazador.juntar_locales())

    return resultado
    # return trazo_D


# Función que devuelve las coordenadas de todas las variantes de locales D
def juntar_variantes():
    
    variantes = [generador_D_1(), generador_D_2(), generador_D_3(), generador_D_4(),
                generador_D_5()]

    return variantes

        
     
# Le paso el local adyacente al que le meto el local interior,
# el local nuevo y la variante
def generador_E_1(local, envoltura, variante):

    print("envoltura", envoltura)

    trazos_finales = variante
    trazado_nuevo = [0,0,0,0,0,0,0,0]
    trazado_adyacente = variante[int(local)]
    resultado = {}

    datos = Analizador.datosLocal(local)
    lado = datos[1]

    if lado == '1':

        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[2] / 2
        
        trazado_adyacente[2] = trazado_adyacente[6] =  trazado_nuevo[0]

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        trazos_finales.update(resultado)

        return trazos_finales

    elif lado == '2':
        
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[5] / 2

        trazado_adyacente[5] = trazado_adyacente[7] =  trazado_nuevo[1]

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        trazos_finales.update(resultado)

        return trazos_finales


    elif lado == '3':

        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[0] + ((trazado_adyacente[2] -
                                                        trazado_adyacente[0]) / 2)
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
        trazado_adyacente[0] = trazado_adyacente[4] = trazado_adyacente[0] + ((trazado_adyacente[2] -
                                                        trazado_adyacente[0]) / 2)

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        trazos_finales.update(resultado)

        return trazos_finales

    elif lado == '4':

        trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[1] + ((trazado_adyacente[5] -
                                                        trazado_adyacente[1]) / 2)
        trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
        trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
        trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0]
        trazado_adyacente[1] = trazado_adyacente[3] =  trazado_adyacente[1] + ((trazado_adyacente[5] -
                                                        trazado_adyacente[1]) / 2)

        resultado[int(envoltura)] = trazado_nuevo
        resultado[int(local)] = trazado_adyacente

        trazos_finales.update(resultado)

        return trazos_finales
    
    else: 
        anchura_adyacente = trazado_adyacente[2] - trazado_adyacente[0]
        altura_adyacente = trazado_adyacente[5] - trazado_adyacente[1]

        if anchura_adyacente >= altura_adyacente:

            trazado_nuevo[1] = trazado_nuevo[3] = trazado_adyacente[1]
            trazado_nuevo[5] = trazado_nuevo[7] = trazado_adyacente[5]
            trazado_nuevo[2] = trazado_nuevo[6] = trazado_adyacente[2]
            trazado_nuevo[0] = trazado_nuevo[4] = trazado_adyacente[0] + ((trazado_adyacente[2] -
                                                        trazado_adyacente[0]) / 2)
            trazado_adyacente[2] = trazado_adyacente[6] = trazado_nuevo[0]

            resultado[int(envoltura)] = trazado_nuevo
            resultado[int(local)] = trazado_adyacente

            trazos_finales.update(resultado)

            return trazos_finales

        if altura_adyacente >= anchura_adyacente:

            return trazos_finales


def juntar_variantes_E(envoltura):

    todos = []
    resultado_final = []
    local = envoltura[0]
    for local_env in envoltura[1]:
        print(local_env)
        i = 0
        print("longitud", len(juntar_variantes()))
        while i < len(juntar_variantes()):

            print("iteracion", i)

            # variantes_aux = variantes
            # variante = variantes_aux[i]
            
            variantes = juntar_variantes()
            variante = variantes[i]
            trazado = generador_E_1(local_env, local, variante)
            i += 1
            todos.append(trazado)
    
    return todos


def ejecutar_E():
    envolturas = Trazador.tratar_envoltura_E()
    result = []
    envoltura = list(envolturas.items())[0]
    # for envoltura in envolturas.items():
    # print("envoltura", envoltura)
    result = juntar_variantes_E(envoltura)
  
    return result


def ejecutar_E_2():
    envolturas = Trazador.tratar_envoltura_E()

    print("----- TODAS LAS ENVOLTURAS_2 -----\n", envolturas)

    print("envoltura", envolturas.items())
    # print("envoltura", envoltura)

    envoltura = list(envolturas.items())[1]
    # for envoltura in envolturas.items():
    print("envoltura", envoltura)
    result = juntar_variantes_E_2(envoltura)
    
    return result


def juntar_variantes_E_2(envoltura):

    todos = []
    local = envoltura[0]
    for local_env in envoltura[1]:
        variantes = ejecutar_E()
        print(local_env)
        i = 0
        print("longitud", len(variantes))
        while i < len(variantes):

            print("iteracion", i)

            # variantes_aux = variantes
            # variante = variantes_aux[i]
            
            # variantes = juntar_variantes()
            variante = variantes[i]
            print("--- ESTA ES LA VARIANTE QUE COJO ----\n", variante)
            trazado = generador_E_1(local_env, local, variante)
            i += 1
            todos.append(trazado)
    
    return todos

# generador_E_1()
# juntar_variantes_E()
# ejecutar_E()
ejecutar_E_2()