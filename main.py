import random

def cargar_lista(name):
    datos=[]
    with open(name, encoding="UTF8") as lista:
        lineas = lista.readlines()
        for linea in lineas:
            datos.append(linea)
    return datos

def elige_opcion(options):
    print(f"¿Cual de todas las palabras es un/a {tipo}?")
    print("Elige una opción:")
    for idx, element in enumerate(options):
        print("{}) {}".format(idx+1,element))
    i = input("Escribe el número correspondiente a tu respuesta -> ")
    try:
        if 0<int(i)<=len(options):
            return int(i)
        else:
            print("Escoge un número entre 1 y 4, no lo que tu quieras. Vuelve a empezar")
    except:
        print("Escoge un número entre 1 y 4, no lo que tu quieras. Vuelve a empezar")
    return None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    adjetivos = cargar_lista("listas/adjetivos.txt")
    adverbios = cargar_lista("listas/adverbios.txt")
    preposiciones = cargar_lista("listas/preposiciones.txt")
    sustantivos = cargar_lista("listas/sustantivos.txt")

    tipos = ["adjetivo", "sustantivo", "adverbio", "preposición"]
    descripciones =["El adjetivo es una clase de palabra que califica al sustantivo en la oración, aporta información \n adicional o complementa su significado.",
                    "Los sustantivos, también conocidos como nombres, son palabras variables que designan personas, \n animales, cosas, ideas, etc., es decir, seres materiales e inmateriales.",
                    "Los adverbios son palabras invariables que nombran circunstancias de lugar, tiempo, modo o \n cantidad, o expresan negación, afirmación o duda.",
                    "Las preposiciones son aquellas palabras que se utilizan para poder formar las oraciones y para \n relacionar las ideas que por lo general encontramos dentro de la misma."]

    adjetivo = adjetivos[random.choice(range(0, len(adjetivos)))]
    sustantivo = sustantivos[random.choice(range(0, len(sustantivos)))]
    adverbio = adverbios[random.choice(range(0, len(adverbios)))]
    preposicion = preposiciones[random.choice(range(0, len(preposiciones)))]
    posicion=random.choice(range(0, len(tipos)))
    tipo = tipos[posicion]

    palabras = [adjetivo, sustantivo, adverbio, preposicion]
    palabras_mix = random.sample(palabras, len(palabras))
    opcion = elige_opcion(palabras_mix)
    if opcion is not None:
        palabra_correcta =palabras[posicion]
        resultado_numero = palabras_mix.index(palabra_correcta)
        print(f"Resultado correcto: {resultado_numero+1}")
        if opcion == resultado_numero+1:
            print("BIEEEEEEEEEN :)    https://www.youtube.com/shorts/05_CExLff2A")
        else:
            print("Vaya basura de persona, no sabes hacer nada")
            print(descripciones[resultado_numero])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
