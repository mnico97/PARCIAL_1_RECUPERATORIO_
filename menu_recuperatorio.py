
from funciones_recuperatorio import *

def ejecutar_menu():
    participantes = cargar_notas()
    
    while True:
        print(''' 
        MENÚ DE OPCIONES

        1 - Mostrar votos de los participantes
        2 - Ordenar votos por nota promedio
        3 - Mostrar los peores 3 participantes
        4 - Mostrar los participantes con mayor promedio que el total
        5 - Mostrar el jurado con las peores notas
        6 - Mostrar participantes con una suma específica de notas
        7 - Definir ganador
        8 - Salir
        ''')

        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            mostrar_matriz(participantes)
        elif opcion == 2:
            participantes = ordenar_por_promedio(participantes)
            mostrar_matriz(participantes)
        elif opcion == 3:
            mostrar_peores_3(participantes)
        elif opcion == 4:
            mostrar_mayores_que_promedio(participantes)
        elif opcion == 5:
            mostrar_jurado_malo(participantes)
        elif opcion == 6:
            valor_suma = int(input("Ingrese el valor para la suma de notas: "))
            sumar_notas(participantes, valor_suma)
        elif opcion == 7:
            definir_ganador(participantes)
        elif opcion == 8:
            print("Saliendo del programa...")
            break
        else:
            print("La opción elegida no es válida. Ingrese una opción correcta.")

ejecutar_menu()
