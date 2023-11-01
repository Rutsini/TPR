import funciones as func


def principal():
    op = "-1"
    nom = "Archivo.dat"
    v = []
    band = False
    cadena_retornada = " "

    print("Opcion 1 - Generar un arreglo de objetos que contenga los datos de todos los eventos.")
    print("Opcion 2 - Mostrar el arreglo generado")
    print("Opcion 3 - A partir del arreglo, generar un archivo binario de registros")
    print("Opcion 4 - Mostrar todos los datos del archivo")
    print("Opcion 5 - Acumulador de costo de produccion por tipo de evento.")
    print("Opcion 6 - Buscar por codigo de identificacion.")
    print("Opcion 7 - Generar matriz")
    print("Opcion 8 - Analisis de palabras.")
    print("Opcion 9 - SALIR DEL PROGRAMA.")

    while op != "9":
        func.separacion_menu()

        op = input("Ingrese la opcion que desee: ")

        if op == "1":
            func.separacion_menu()

            n = int(input("Ingrese la cantidad de eventos que desea cargar: "))
            while not func.validar_n(n):
                print("Ingrese una cantidad de eventos mayor a 0")
                n = int(input("Ingrese la cantidad de eventos que desea cargar: "))
            else:
                func.cargar_vector(v, n)
                print("Los eventos fueron cargados correctamente.")

        elif op == "2":
            func.separacion_menu()

            if v != []:
                func.mostrar_vector(v)
            else:
                print("El vector aun esta vacio.")

        elif op == "3":
            func.separacion_menu()

            monto_ingresado = int(input("Ingrese un monto que desee filtrar: "))
            func.generar_binario(nom, v, monto_ingresado)
            print("El archivo binario fue creado correctamente.")

        elif op == "4":
            func.separacion_menu()

            func.mostrar_binario(nom)

        elif op == "5":
            func.separacion_menu()

            acumulador = [0] * 20
            result = func.acum_op5(acumulador, nom)
            if result != 0:
                print("El promedio de todos los acumuladores es:", result, "$")

        elif op == "6":
            func.separacion_menu()

            identificacion_ingresada = str(input("Ingrese el codigo de identificacion que desee: "))
            cadena_retornada = func.busquedabinaria(v, identificacion_ingresada)
            if cadena_retornada == "-1":
                print("No existe.")
                band = False
            else:
                print(cadena_retornada)
                band = True

        elif op == "7":
            func.separacion_menu()

            tipo_evento = int(input("Ingrese el tipo de evento que usted desee (0 a 19): "))

            while not func.validar_numeros_ingresados(tipo_evento, 0, 19):
                print("Ingrese un valor valido. (0 a 19)")
                tipo_evento = int(input("Ingrese el tipo de evento que usted desee: "))
            else:
                func.matris(v, tipo_evento)

        elif op == "8":
            func.separacion_menu()

            if band:
                result = func.analizar_palabras(cadena_retornada)
                print("la cantidad de palabras encontradas fueron", result)
            else:
                print("No hay una oracion para analizar, pase por opcion 6.")

        elif op == "9":
            func.separacion_menu()

            print("SALIO DEL PROGRAMA.")

            func.separacion_menu()


if __name__ == "__main__":
    principal()
