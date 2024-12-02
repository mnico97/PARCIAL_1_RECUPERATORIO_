
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    '''
    Función que inicializa una matriz de tamaño filas x columnas con un valor inicial.
    Recibe el número de filas, el número de columnas y el valor inicial para cada celda.
    Devuelve la matriz inicializada con los valores indicados.
    '''
    matriz = []  # Creamos la lista vacía para la matriz
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz = matriz + [fila]
    return matriz


def cargar_notas():
    '''
    Función que carga las notas de 5 participantes con validación de notas entre 1 y 100.
    No recibe parámetros.
    Devuelve la lista de participantes con sus notas y el promedio calculado.
    '''
    participantes = inicializar_matriz(5, 5, 0)

    for i in range(5):
        participantes[i][0] = i + 1  
        print(f"Participante {participantes[i][0]}:")

        # Validación de la nota entre 1 y 100 para cada jurado
        participantes[i][1] = int(input("Ingrese la nota del Jurado 1 (1-100): "))
        while participantes[i][1] < 1 or participantes[i][1] > 100:
            print("ERROR: La nota ingresada debe ser mayor o igual a 1 y menor o igual a 100.")
            participantes[i][1] = int(input("Ingrese la nota del Jurado 1 (1-100): "))

        participantes[i][2] = int(input("Ingrese la nota del Jurado 2 (1-100): "))
        while participantes[i][2] < 1 or participantes[i][2] > 100:
            print("ERROR: La nota ingresada debe ser mayor o igual a 1 y menor o igual a 100.")
            participantes[i][2] = int(input("Ingrese la nota del Jurado 2 (1-100): "))

        participantes[i][3] = int(input("Ingrese la nota del Jurado 3 (1-100): "))
        while participantes[i][3] < 1 or participantes[i][3] > 100:
            print("ERROR: La nota ingresada debe ser mayor o igual a 1 y menor o igual a 100.")
            participantes[i][3] = int(input("Ingrese la nota del Jurado 3 (1-100): "))

        # Calculo el promedio y lo guardo en la última columna
        participantes[i][4] = (participantes[i][1] + participantes[i][2] + participantes[i][3]) / 3

    return participantes


def mostrar_matriz(matriz: list) -> None:
    '''
    Función que muestra la matriz con los resultados de los participantes.
    Recibe la matriz con las notas de los participantes.
    Muestra la matriz por pantalla.
    '''
    print("Participante | Nota Jurado 1 | Nota Jurado 2 | Nota Jurado 3 | Nota Promedio")
    for participante in matriz:
        print(f"{participante[0]:>11} | {participante[1]:>14} | {participante[2]:>14} | {participante[3]:>14} | {participante[4]:>12.2f}")


def ordenar_por_promedio(matriz: list):
    '''
    Función que ordena la matriz por la nota promedio de los participantes según el orden que elija el usuario.
    Recibe la matriz con los datos de los participantes.
    Devuelve la matriz ordenada de acuerdo con el promedio.
    '''
    # Pedir el orden al usuario
    orden = input("Ingrese el orden para ordenar (asc para ascendente, desc para descendente): ").lower()
    
    if orden == 'asc':
        # Orden ascendente
        for i in range(len(matriz)):
            for j in range(i + 1, len(matriz)):
                if matriz[i][4] > matriz[j][4]:  # Compara por promedio
                    matriz[i], matriz[j] = matriz[j], matriz[i]
    elif orden == 'desc':
        # Orden descendente
        for i in range(len(matriz)):
            for j in range(i + 1, len(matriz)):
                if matriz[i][4] < matriz[j][4]:  # Compara por promedio
                    matriz[i], matriz[j] = matriz[j], matriz[i]
    else:
        print("ERROR: No se realizó ningún cambio.")
        
    return matriz


def mostrar_peores_3(matriz: list):
    '''
    Función que muestra los 3 peores participantes según su nota promedio.
    Recibe la matriz con los resultados de los participantes.
    Muestra los 3 peores participantes.
    '''
    # Ordeno la matriz por promedio de menor a mayor
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][4] > matriz[j][4]:
                matriz[i], matriz[j] = matriz[j], matriz[i]

    print("\nLos 3 peores participantes según su promedio son:")
    for i in range(3):
        print(f"Participante {matriz[i][0]} - Promedio: {matriz[i][4]:.2f}")


def mostrar_mayores_que_promedio(matriz: list):
    '''
    Función que muestra los participantes cuyo promedio es mayor que el promedio total.
    Recibe la matriz con los resultados de los participantes.
    Muestra los participantes con promedio mayor al total.
    '''
    total_promedio = 0
    for participante in matriz:
        total_promedio += participante[4]
    
    promedio_total = total_promedio / len(matriz)
    print(f"\nEl promedio total de todos los participantes es: {promedio_total:.2f}")
    
    # Mostrar los participantes con promedio mayor
    for i in range(len(matriz)):
        if matriz[i][4] > promedio_total:
            print(f"Participante {matriz[i][0]} - Promedio: {matriz[i][4]:.2f}")


def mostrar_jurado_malo(matriz: list):
    '''
    Función que muestra los jurados que pusieron las peores notas en promedio.
    Recibe la matriz con los resultados de los participantes.
    Muestra los jurados con peores notas.
    '''
    # Sumar las notas de cada jurado
    total_jurado_1 = 0
    total_jurado_2 = 0
    total_jurado_3 = 0
    
    for participante in matriz:
        total_jurado_1 += participante[1]
        total_jurado_2 += participante[2]
        total_jurado_3 += participante[3]
    
    # Se calcula los promedios de cada jurado
    promedio_jurado_1 = total_jurado_1 / len(matriz)
    promedio_jurado_2 = total_jurado_2 / len(matriz)
    promedio_jurado_3 = total_jurado_3 / len(matriz)

    # Encontrar el menor promedio
    menor_promedio = promedio_jurado_1
    jurados_malos = [1]  # Se inicializa con el jurado 1

    # Comparo los promedios para determinar el jurado/s con peor nota
    if promedio_jurado_2 < menor_promedio:
        menor_promedio = promedio_jurado_2
        jurados_malos = [2]  # Si el jurado 2 tiene el promedio más bajo, se agrega
    elif promedio_jurado_2 == menor_promedio:
        jurados_malos = [1, 2]  # Si tiene el mismo promedio bajo, los agregamos a los dos
    
    if promedio_jurado_3 < menor_promedio:
        menor_promedio = promedio_jurado_3
        jurados_malos = [3]  # Si el jurado 3 tiene el promedio más bajo, se agrega
    elif promedio_jurado_3 == menor_promedio:
        jurados_malos.append(3)  # Si tiene el mismo promedio bajo, se agrega también
    
    if len(jurados_malos) == 1:
        print(f"El jurado que puso las peores notas fue: El jurado número {jurados_malos[0]}")
    else:
        print(f"Los jurados que pusieron las peores notas fueron: El jurado número {jurados_malos[0]} y el jurado número {jurados_malos[1]}")


def sumar_notas(matriz: list, valor: int):
    '''
    Función que muestra los participantes cuya suma de notas es igual al valor ingresado.
    Recibe la matriz con los resultados de los participantes y un valor para comparar la suma de las notas.
    Muestra los participantes cuya suma de notas coincide con el valor.
    '''
    # Validación para que el valor ingresado esté entre 3 y 300
    while valor < 3 or valor > 300:
        print("ERROR: La suma de notas debe ser un número entre 3 y 300.")
        valor = int(input(f"Ingrese un nuevo valor entre 3 y 300 para la suma de notas: "))

    encontrados = False
    print(f"\nBuscando participantes cuya suma de notas sea igual a {valor}:")

    for participante in matriz:
        suma = participante[1] + participante[2] + participante[3]
        
        if suma == valor:
            print(f"El Participante {participante[0]} tiene una suma de notas de {suma}.")
            encontrados = True

    if not encontrados:
        print(f"No se encontraron participantes con una suma de notas igual a {valor}.")


import random

def definir_ganador(matriz: list):
    '''
    Función que define al ganador según el promedio, con desempate si es necesario.
    Recibe la matriz con los resultados de los participantes.
    Muestra al ganador o realiza un desempate.
    '''
    mayor_promedio = matriz[0][4]
    
    # Encuentro el mayor promedio
    for participante in matriz:
        if participante[4] > mayor_promedio:
            mayor_promedio = participante[4]
    
    # Filtro los participantes con el mayor promedio
    ganadores = []
    for participante in matriz:
        if participante[4] == mayor_promedio:
            ganadores = ganadores + [participante]
    
    if len(ganadores) == 1:
        # Si solo hay un ganador, lo muestro
        print(f"El ganador es el Participante {ganadores[0][0]} con un promedio de {mayor_promedio:.2f}")
    else:
        # Si hay más de un ganador, se realiza el desempate
        print(f"Hay un empate entre los siguientes participantes con un promedio de {mayor_promedio:.2f}:")
        for ganador in ganadores:
            print(f"Participante {ganador[0]}")

        # Desempate
        elecciones = [0, 0, 0]
        
        # Jurados eligen participante
        for i in range(3):
            print(f"\nJurado {i+1}, elija a su ganador:")
            for j in range(len(ganadores)):
                print(f"{j + 1}. Participante {ganadores[j][0]}")
            eleccion = int(input(f"Jurado {i+1}, elija el número del participante (1-{len(ganadores)}): "))
            elecciones[eleccion - 1] = elecciones[eleccion - 1] + 1

        # Verifico ganador claro
        max_elecciones = elecciones[0]
        for eleccion in elecciones:
            if eleccion > max_elecciones:
                max_elecciones = eleccion
        
        # Conteo votos participantes
        cantidad_maxima = 0
        for eleccion in elecciones:
            if eleccion == max_elecciones:
                cantidad_maxima = cantidad_maxima + 1
        
        if cantidad_maxima == 1:
            #Si hay ganador claro se muestra el q tiene mas votos
            for i in range(len(ganadores)):
                if elecciones[i] == max_elecciones:
                    ganador_final = ganadores[i]
                    print(f"\nEl ganador es el Participante {ganador_final[0]} con un promedio de {ganador_final[4]:.2f}")
        else:
            # Si no hay acuerdo claro se hace aleatoriamente.
            ganador_final = random.choice(ganadores)
            print(f"\nEl ganador se ha elegido aleatoriamente: Participante {ganador_final[0]} con un promedio de {ganador_final[4]:.2f}")

