import os
import pickle
import random

import clase as clasesita


def separacion_menu():
    print("-" * 100)


def validar_numeros_ingresados(valor, izq, der):
    if izq <= valor <= der:
        return True
    return False


def validar_n(n):
    if n > 0:
        return True
    return False


def codigos():
    codig = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
    return "Codigo" + " " + random.choice(codig)


def titulos():
    titul = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
    return "Titulo" + " " + random.choice(titul)


def descrpciones():
    descrip = ("El terremoto tuvo su epicentro en San Juan y se siNtió en todo el norte Argentino.",
               "El terremoto tuvo su epicentro en San Juan y se Sintió en todo el norte Venezolano.",
               "El terremoto tuvo su epicentro en San Juan y se SiNtió en todo el norte Portugues.",
               "El terremoto tuvo su epicentro en San Juan y se sintió en todo el norte Italiano.",
               "El terremoto tuvo su epicentro en San Juan y se SINTIO en todo el norte Español.")
    return random.choice(descrip)


def cargar_vector(v, n):
    for i in range(n):
        identificacion = codigos() + str(i)
        titulo = titulos()
        descripcion = descrpciones()
        costo_produccion = round(random.uniform(500, 50000), 2)
        tipo_evento = random.randint(0, 19)
        segmento_diario = random.randint(0, 9)

        dato = clasesita.Eventos(identificacion, titulo, descripcion, costo_produccion, tipo_evento, segmento_diario)
        add_in_order(v, dato)


def mostrar_vector(v):
    for i in v:
        print(i)


def add_in_order(v, dato):
    n = len(v)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if v[c].identificacion == dato.identificacion:
            pos = c
            break
        if v[c].identificacion > dato.identificacion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [dato]


def generar_binario(nom, v, p):
    archivo_b = open(nom, "wb")

    for i in v:
        if i.costo_produccion > p:
            dato = i
            pickle.dump(dato, archivo_b)

    archivo_b.close()


def mostrar_binario(nom):
    if os.path.exists(nom):
        tam = os.path.getsize(nom)
        if tam > 0:
            archivo_b = open(nom, "rb")
            while tam > archivo_b.tell():
                dato = pickle.load(archivo_b)

                print("Identificacion:", f"{dato.identificacion:10}",
                      "Titulo:", f"{dato.titulo:9}",
                      "Costo de produccion: ", f"{dato.costo_produccion:9}",
                      "Tipo de evento: ", f"{dato.tipo_evento:2}",
                      "Segmento diario: ", f"{dato.segmento_diario:2}",
                      "Descripcion: " + dato.descripcion)
            archivo_b.close()
        else:
            print("No hay eventos en el archivo para mostrarlos.")


def acum_op5(acumulador, nom):
    result = 0
    cont = 0
    acum = 0
    if os.path.exists(nom):
        tam = os.path.getsize(nom)
        archivo_b = open(nom, "rb")
        while tam > archivo_b.tell():
            dato = pickle.load(archivo_b)

            if dato.tipo_evento >= 5:
                pos = dato.tipo_evento
                acumulador[pos] += float(dato.costo_produccion)
        for i in range(len(acumulador)):
            acum += acumulador[i]
            if acumulador[i] != 0:
                print("Tipo de evento: ", i, "Monto:", acumulador[i])
                cont += 1

        archivo_b.close()
        if cont > 0:
            result = promedio(acum, cont)
        else:
            print("La cantidad de archivos es 0, por lo que no se puede calcular el promedio.")
        return result


def promedio(v1, v2):
    prom = v1 / v2
    return round(prom, 2)


def busquedabinaria(v, cod):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    banderin = False
    while izq <= der:
        c = (izq + der) // 2

        if v[c].identificacion == cod:
            pos = c
            banderin = True
            des = v[c].descripcion
            break
        if v[c].identificacion > cod:
            der = c - 1
        else:
            izq = c + 1
    if banderin == True:
        print(v[pos])
        return des
    else:
        return "-1"


def matris(v, te):
    cc, cf = 20, 10
    matrix = [[0] * cc for i in range(cf)]
    for i in v:
        c = i.tipo_evento
        f = i.segmento_diario
        if c > te:
            matrix[f][c] += 1
    for f in range(cf):
        for j in range(cc):
            if matrix[f][j] != 0:
                print("Segmento_diario", f, "tipo_evento", j,
                      "Cantidad de enventos entre tipo de eventos y segmento diario", matrix[f][j])


def analizar_palabras(texto):
    mayusculas = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"
    letra_t = "t"
    letra_s = "s"
    cont_pal = 0
    cont_car = 0
    bandera_mayus = False
    bandera_letra_s = False
    bandera_letra_t = False
    cont = 0

    for car in texto:
        if car == " " or car == ".":
            cont_pal += 1
            if bandera_mayus and bandera_letra_t and bandera_letra_s:
                cont += 1

            cont_car = 0
            bandera_mayus = False
            bandera_letra_s = False
            bandera_letra_t = False


        else:
            cont_car += 1

            if car in mayusculas and cont_car == 1:
                bandera_mayus = True

            if car in letra_s:
                bandera_letra_s = True

            if car in letra_t:
                bandera_letra_t = True

    return cont
