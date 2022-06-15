import streamlit as st

import random


def cargar_lista(name):
    datos=[]
    with open(name, encoding="UTF8") as lista:
        lineas = lista.readlines()
        for linea in lineas:
            datos.append(linea)
    return datos
@st.cache
def cargar_palabras() :
    adjetivos = cargar_lista("listas/adjetivos.txt")
    adverbios = cargar_lista("listas/adverbios.txt")
    preposiciones = cargar_lista("listas/preposiciones.txt")
    sustantivos = cargar_lista("listas/sustantivos.txt")

    adjetivo = adjetivos[random.choice(range(0, len(adjetivos)))]
    sustantivo = sustantivos[random.choice(range(0, len(sustantivos)))]
    adverbio = adverbios[random.choice(range(0, len(adverbios)))]
    preposicion = preposiciones[random.choice(range(0, len(preposiciones)))]

    palabras = [adjetivo, sustantivo, adverbio, preposicion]

    return palabras

@st.cache
def cargar_palabras_mix(palabras):
    palabras_mix = random.sample(palabras, len(palabras))
    palabras_mix.insert(0,'')
    return palabras_mix
@st.cache
def cargar_posicion(tipos):
    posicion = random.choice(range(0, len(tipos)))
    return posicion

@st.cache
def elige_opcion(options, tipo):
    st.title("Adivina el tipo de palabra")
    option = st.radio(
        f"¿Cual de todas las palabras es un/a {tipo}?",options, index=0)
    return option

@st.cache
def add_empty_value_to_list(lista):
    out = []
    out.append('')
    for elem in lista:
        a=str(elem)
        print(type(a))
        out.append(a)
    return out
if __name__ == '__main__':


    tipos = ["adjetivo", "sustantivo", "adverbio", "preposición"]
    descripciones = [
        "El adjetivo es una clase de palabra que califica al sustantivo en la oración, aporta información \n adicional o complementa su significado.",
        "Los sustantivos, también conocidos como nombres, son palabras variables que designan personas, \n animales, cosas, ideas, etc., es decir, seres materiales e inmateriales.",
        "Los adverbios son palabras invariables que nombran circunstancias de lugar, tiempo, modo o \n cantidad, o expresan negación, afirmación o duda.",
        "Las preposiciones son aquellas palabras que se utilizan para poder formar las oraciones y para \n relacionar las ideas que por lo general encontramos dentro de la misma."]

    palabras = cargar_palabras()

    palabras_mix = cargar_palabras_mix(palabras)
    posicion =cargar_posicion(tipos)
    tipo = tipos[posicion]
    descripcion = descripciones [posicion]

    st.title("Adivina el tipo de palabra")
    st.markdown("Recuerda que si el botón PRUEBA DE NUEVO está bordeado en rojo una vez que lo has usado, deberas tocar sobre un espacio en blanco . ")
    opcion = st.radio(f"¿Cual de todas las palabras es un/a {tipo}?", palabras_mix, index=0)
    if (opcion == palabras[posicion]):
        st.success("BIEEEEEENNNNNNNNNNN")
        st.video("https://www.youtube.com/watch?v=bi2v08KUbNQ")
    elif (len(opcion)> 0):
        st.error("Estudia más o vuelve a intantarlo.")
        st.warning(descripciones[posicion])
    if st.button("Prueba de nuevo"):
        #st.legacy_caching.clear_cache()
    #if my_slot1.button("Clear"):
