"""
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú que permita acceder a cada uno de los puntos por separado.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
"""
from Funciones_parte_1 import*
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M

def filtrar_heroes_masculinos(lista:list):
    """
    Filtra la lista de superhéroes para obtener solo los de género masculino.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        list: Lista filtrada de superhéroes masculinos.
    """
    return filtrar_lista(lambda heroe : heroe["genero"] == "M", lista)
    

def imprimir_heroes_masculinos(lista:list)->None:
    """
    Imprime por consola el nombre de cada superhéroe masculino.

    Args:
        lista (list): Lista de superhéroes masculinos.
    """
    imprimir_personajes_nombre(filtrar_heroes_masculinos(lista))



# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F

def filtrar_heroes_femeninos(lista:list):
    """
    Filtra la lista de superhéroes para obtener solo los de género femenino.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        list: Lista filtrada de superhéroes femeninos.
    """
    return filtrar_lista(lambda heroe : heroe["genero"] == "F", lista)
    

def imprimir_heroes_femeninos(lista:list)->None:
    """
    Imprime por consola el nombre de cada superhéroe femenino.

    Args:
        lista (list): Lista de superhéroes femeninos.
    """
    imprimir_personajes_nombre(filtrar_heroes_femeninos(lista))


# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

def heroe_mas_alto_masculino(lista: list):
    """
    Determina el superhéroe más alto de género masculino.

    Args:
        lista (list): Lista de superhéroes masculinos.

    Returns:
        dict: Diccionario con la información del superhéroe más alto.
    """
    lista_masculino = filtrar_heroes_masculinos(lista)
    heroe_mas_alto = heroe_mas_alto_bajo(lista_masculino)
    return heroe_mas_alto



# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

def heroe_mas_alto_femenino(lista: list):
    """
    Determina el superhéroe más alto de género femenino.

    Args:
        lista (list): Lista de superhéroes femeninos.

    Returns:
        dict: Diccionario con la información del superhéroe más alto.
    """
    lista_femenino = filtrar_heroes_femeninos(lista)
    heroe_mas_alto = heroe_mas_alto_bajo(lista_femenino)
    return heroe_mas_alto



# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M

def heroe_mas_bajo_masculino(lista: list):
    """
    Determina el superhéroe más bajo de género masculino.

    Args:
        lista (list): Lista de superhéroes masculinos.

    Returns:
        dict: Diccionario con la información del superhéroe más bajo.
    """
    lista_masculino = filtrar_heroes_masculinos(lista)
    heroe_mas_bajo = heroe_mas_alto_bajo(lista_masculino, False)
    return heroe_mas_bajo


# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def heroe_mas_bajo_femenino(lista: list):
    """
    Determina el superhéroe más bajo de género femenino.

    Args:
        lista (list): Lista de superhéroes femeninos.

    Returns:
        dict: Diccionario con la información del superhéroe más bajo.
    """
    lista_femenino = filtrar_heroes_femeninos(lista)
    heroe_mas_bajo = heroe_mas_alto_bajo(lista_femenino, False)
    return heroe_mas_bajo

# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
def promedio_altura_masculino(lista)->float:
    """
    Calcula la altura promedio de los superhéroes de género masculino.

    Args:
        lista (list): Lista de superhéroes masculinos.

    Returns:
        float: Altura promedio.
    """
    stark_normalizar_datos(lista)
    lista_masculino = filtrar_heroes_masculinos(lista)
    return promedio_altura(lista_masculino)


# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
def promedio_altura_femenino(lista)->float:
    """
    Calcula la altura promedio de los superhéroes de género femenino.

    Args:
        lista (list): Lista de superhéroes femeninos.

    Returns:
        float: Altura promedio.
    """
    stark_normalizar_datos(lista)
    lista_femenino = filtrar_heroes_femeninos(lista)
    return promedio_altura(lista_femenino)

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def lista_sin_repetidos(lista_repetidos:list)->list:
    """Quita los elementos repetidos de una lista

    Args:
        lista_repetidos (list):lista con elementos repetidos

    Returns:
        list: lista sin repetidos
    """
    return list(set(lista_repetidos))

def mapear_key(lista:list, key: str)->list:
    """
    Extrae los valores de una clave específica de una lista de diccionarios.

    Args:
        lista (list): Lista de diccionarios.
        key (str): Clave cuyos valores se extraerán.

    Returns:
        list: Lista de valores correspondientes a la clave especificada.
    """
    lista_mapeada = []
    for el in lista:
        lista_mapeada.append(el[key])

    return lista_sin_repetidos(lista_mapeada)

def heroes_tipo_ojos(lista: list):
    """
    Determina cuántos superhéroes tienen cada tipo de color de ojos.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de color de ojos.
    """
    colores_ojos = mapear_key(lista, "color_ojos")
    conteo_ojos = {color: 0 for color in colores_ojos}
    
    for heroe in lista:
        color = heroe["color_ojos"]
        if color in conteo_ojos:
            conteo_ojos[color] += 1
    
    return conteo_ojos
            
def heroes_tipo_pelo(lista: list):
    """
    Determina cuántos superhéroes tienen cada tipo de color de pelo.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de color de pelo.
    """
    colores_pelos = mapear_key(lista, "color_pelo")
    conteo_pelos = {color: 0 for color in colores_pelos}
    
    for heroe in lista:
        color = heroe["color_pelo"]
        if color in conteo_pelos:
            conteo_pelos[color] += 1
    
    return conteo_pelos

def heroes_tipo_inteligencia(lista):
    """
    Determina cuántos superhéroes tienen cada tipo de inteligencia.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario con el conteo de cada tipo de inteligencia.
    """
    
    inteligencias = mapear_key(lista, "inteligencia")
    for i in range(len(inteligencias)):
        if inteligencias[i] == "":
            inteligencias[i] = "No Tiene"
    
    
    conteo_inteligencias = {inteligencia: 0 for inteligencia in inteligencias}
    
    
    for heroe in lista:
        
        inteligencia = heroe.get("inteligencia", "No Tiene")
        if inteligencia == "":
            inteligencia = "No Tiene"
        
        
        conteo_inteligencias[inteligencia] += 1
    
    return conteo_inteligencias

def listar_agrupados(lista, key):
    """
    Agrupa los superhéroes según un atributo específico.

    Args:
        lista (list): Lista de superhéroes.
        key (str): Clave por la cual se agruparán los superhéroes.

    Returns:
        dict: Diccionario que contiene la lista de superhéroes agrupados por el atributo especificado.
    """
    agrupados = {}
    for heroe in lista:
        valor = heroe[key] if key in heroe and heroe[key] else "No Tiene"
        if valor not in agrupados:
            agrupados[valor] = []
        agrupados[valor].append(heroe["nombre"])
    return agrupados

def imprimir_agrupados(agrupados):
    """
    Imprime por consola los superhéroes agrupados según un atributo específico.

    Args:
        agrupados (dict): Diccionario que contiene la lista de superhéroes agrupados por un atributo.
    """
    for key, nombres in agrupados.items():
        print(f"{key}:")
        for nombre in nombres:
            print(f"  - {nombre}")
        print()

def listar_heroes_por_color_ojos(lista):
    """
    Agrupa los superhéroes por el color de ojos.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario que contiene la lista de superhéroes agrupados por color de ojos.
    """
    return listar_agrupados(lista, "color_ojos")

def listar_heroes_por_color_pelo(lista):
    """
    Agrupa los superhéroes por el color de pelo.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario que contiene la lista de superhéroes agrupados por color de pelo.
    """
    return listar_agrupados(lista, "color_pelo")

def listar_heroes_por_inteligencia(lista):
    """
    Agrupa los superhéroes por el tipo de inteligencia.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        dict: Diccionario que contiene la lista de superhéroes agrupados por tipo de inteligencia.
    """
    return listar_agrupados(lista, "inteligencia")

def imprimir_conteo(conteo):
    """
    Imprime por consola el conteo de elementos en un diccionario.

    Args:
        conteo (dict): Diccionario que contiene el conteo de elementos.
    """
    for key, count in conteo.items():
        print(f"{key}: {count}")
    print()
# Menú

def main_desafio_01(lista: list):
    """hace un menu de opciones con todas las funciones del programa

    Args:
        lista (list): toma la la lista de personajes para complir con todas las funciones
    """
    

    while True:
        print("\nMenú de Opciones:")
        print("A) Imprimir nombres de superhéroes de género M")
        print("B) Imprimir nombres de superhéroes de género F")
        print("C) Superhéroe más alto de género M")
        print("D) Superhéroe más alto de género F")
        print("E) Superhéroe más bajo de género M")
        print("F) Superhéroe más bajo de género F")
        print("G) Altura promedio de superhéroes de género M")
        print("H) Altura promedio de superhéroes de género F")
        print("I) Nombre del superhéroe asociado a C a F")
        print("J) Cantidad de superhéroes por color de ojos")
        print("K) Cantidad de superhéroes por color de pelo")
        print("L) Cantidad de superhéroes por tipo de inteligencia")
        print("M) Listar superhéroes agrupados por color de ojos")
        print("N) Listar superhéroes agrupados por color de pelo")
        print("O) Listar superhéroes agrupados por tipo de inteligencia")
        print("Q) Salir")

        opcion = input("Seleccione una opción: ").upper()

        match opcion:
            case "A":
                imprimir_heroes_masculinos(lista)
            case "B":
                imprimir_heroes_femeninos(lista)
            case "C":
                mostrar_heroes(heroe_mas_alto_masculino(lista))
            case "D":
                mostrar_heroes(heroe_mas_alto_femenino(lista))
            case "E":
                mostrar_heroes(heroe_mas_bajo_masculino(lista))
            case "F":
                mostrar_heroes(heroe_mas_bajo_femenino(lista))
            case "G":
                print(f"El promedio de la altura de los heroes masculinos es: {promedio_altura_masculino(lista):0.2f}")
            case "H":
                print(f"El promedio de la altura de los heroes femeninos es: {promedio_altura_femenino(lista):0.2f}")
            case "I":
                print("El heroe/s más alto/s masculino/s: ")
                imprimir_personajes_nombre(heroe_mas_alto_masculino(lista))
                print("La/s heroina/s más alta/s femeninas: ")
                imprimir_personajes_nombre(heroe_mas_alto_femenino(lista))
                print("El heroe/s más bajo/s masculino/s: ")
                imprimir_personajes_nombre(heroe_mas_bajo_masculino(lista))
                print("La/s heroina/s más baja/s femenina/s: ")
                imprimir_personajes_nombre(heroe_mas_bajo_femenino(lista))
            case "J":
                print("Conteo de tipos de ojos:")
                imprimir_conteo(heroes_tipo_ojos(lista))
                
            case "K":
                
                print("Conteo de tipos de pelo:")
                imprimir_conteo(heroes_tipo_pelo(lista))
            case "L":
                print("Conteo de tipos de inteligencia:")
                imprimir_conteo(heroes_tipo_inteligencia(lista))
            case "M":
                print("Héroes agrupados por color de ojos:")
                imprimir_agrupados(listar_heroes_por_color_ojos(lista))
            case "N":
                print("Héroes agrupados por color de pelo:")
                imprimir_agrupados(listar_heroes_por_color_pelo(lista))
            case "O":
                print("Héroes agrupados por tipo de inteligencia:")
                imprimir_agrupados(listar_heroes_por_inteligencia(lista))
            case "Q":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del menú.")



