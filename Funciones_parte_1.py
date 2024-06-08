'''
Desafío #00:

A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
la altura del mismo
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
F. Recorrer la lista y determinar la altura promedio de los superhéroes
(PROMEDIO)
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (MÁXIMO, MÍNIMO)
H. Calcular e informar cual es el superhéroe más y menos pesado.
I. Ordenar el código implementando una función para cada uno de los valores
informados.
J. Construir un menú que permita elegir qué dato obtener
'''

def mostrar_heroes(lista: list) -> None:
    """
    Muestra una lista de héroes con sus características formateadas en una tabla.

    Args:
        lista (list): Lista de diccionarios con información de los héroes.
    """
    print("           ***Listado de heroes*** ")
    print(" Nombre               Identidad                       Empresa          Genero   Altura      Peso               Color de ojos   Color de pelo  Fuerza  Inteligencia ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for heroe in lista:
        mostrar_heroe_item(heroe)


def stark_normalizar_datos(lista):
    """
    Normalizar la lista de diccionarios stark convirtiendo los valores str en float con dos decimales y/o int de ser necesario

    Parametros:
        lista(list): la lista de diccionarios stark
    Retorna: 
        retorna True si se realizo al menos una normalizacion, False de lo contrario
    """

    normalizar = False
    for diccionario in lista:
        for valor in diccionario:

            if valor == "fuerza" and type(diccionario[valor]) != int:
                diccionario[valor] = int(diccionario[valor])
                normalizar = True
            elif type(diccionario[valor]) != float and (valor == "peso" or valor == "altura"):
                diccionario[valor] = float(diccionario[valor])
                normalizar = True

def mostrar_heroe_item(heroe: dict):
    """
    Muestra los detalles de un héroe en una línea formateada.

    Args:
        heroe (dict): Diccionario con información de un héroe.
    """
    nombre = heroe['nombre']
    identidad = heroe['identidad']
    empresa = heroe['empresa']
    genero = heroe['genero']
    altura = float(heroe['altura'])
    peso = float(heroe['peso'])
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']
    fuerza = int(heroe['fuerza'])
    inteligencia = heroe['inteligencia']

    print(f"{nombre:20} {identidad:30} {empresa:20} {genero:4} {altura:8.2f} {peso:10.2f} {color_ojos:>25} {color_pelo:>15} {fuerza:6} {inteligencia:>10}")


def mostrar_heroe(heroe:dict):
    """
    Muestra los detalles de un héroe en líneas separadas.

    Args:
        heroe (dict): Diccionario con información de un héroe.
    """
    print(f"Nombre: {heroe['nombre']}\nIdentidad: {heroe['identidad']}\nEmpresa: {heroe['empresa']}\nGenero: {heroe['genero']}\nAltura: {heroe['altura']}\nPeso: {heroe['peso']}\nColor de ojos: {heroe['color_ojos']}\nColor de pelo: {heroe['color_pelo']}\nFuerza: {heroe['fuerza']}\nInteligencia: {heroe['inteligencia']}")



def encontrar_extremo_manual(lista: list, clave: str, buscar_maximo: bool = True):
    """
    Encuentra el diccionario con el valor máximo o mínimo de una clave específica en una lista de diccionarios.

    Args:
        lista (list): Lista de diccionarios.
        clave (str): La clave por la cual buscar el valor extremo.
        buscar_maximo (bool): Indica si se busca el valor máximo (True) o mínimo (False). Por defecto es True.

    Returns:
        el valor extremo del diccionario que se pidio
    """
    if not lista:
        return None
    
    # Inicializar con el primer elemento de la lista
    extremo = lista[0][clave]
    
    # Iterar sobre la lista a partir del segundo elemento
    for item in lista[1:]:
        if buscar_maximo:
            if item[clave] > extremo:
                extremo = item[clave]
        else:
            if item[clave] < extremo:
                extremo = item[clave]
    
    return extremo

def filtrar_lista(filtadora, lista:list):
    """
    Filtra una lista de acuerdo a una función dada.

    Args:
        filtadora (function): Función que determina si un elemento debe ser incluido en la lista filtrada.
        lista (list): Lista a filtrar.

    Returns:
        Lista filtrada.
    """
    lista_filtrada = []
    for el in lista:
        if filtadora(el):
            lista_filtrada.append(el)
    return lista_filtrada

def mapear_lista(mapeadora,lista:list):
    """
    Aplica una función a cada elemento de una lista.

    Args:
        mapeadora (function): Función a aplicar.
        lista (list): Lista a mapear.

    Returns:
        Lista mapeada.
    """
    lista_mapeada = []
    for el in lista:
        x = mapeadora(el)
        lista_mapeada.append(x)
    return lista_mapeada


#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def imprimir_personajes_nombre(lista: list)->None:
    """
    Imprime por consola el nombre de cada superhéroe en la lista.

    Args:
        lista (list): Lista de superhéroes.
    """
    for datos in lista:
        nombre = datos["nombre"]
        print(f"Nombre: {nombre}")

#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
#la altura del mismo
def imprimir_personajes_2_claves(lista: list, clave_1: str, clave_2: str)->None:
    """
    Imprime por consola dos claves de cada superhéroe en la lista.

    Args:
        lista (list): Lista de superhéroes.
        clave_1 (str): Primera clave a imprimir.
        clave_2 (str): Segunda clave a imprimir.
    """
    print(f"{clave_1:<25}|{clave_2}")
    for datos in lista:
        primer_clave = datos[clave_1]
        segunda_clave = datos[clave_2]
        print("-----------------------------------------------------")
        print(f"{primer_clave:<25}|{segunda_clave}")

def imprimir_personajes_2_claves(lista: list, clave_1: str, clave_2: str)->None:
    """
    Imprime por consola dos claves de cada superhéroe en la lista.

    Args:
        lista (list): Lista de superhéroes.
        clave_1 (str): Primera clave a imprimir.
        clave_2 (str): Segunda clave a imprimir.
    """

    print(f"{'Nombre':<25}|  Altura")
    for datos in lista:
        nombre = datos["nombre"]
        altura = float(datos["altura"])
        print(f"{nombre:<25}|  {altura:0.2f}")

#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_mas_alto_bajo(lista: list, maximo: bool = True)->dict:
    """busca al heroe o heroes mas alto/s o mas bajos de una lista

    Args:
        lista (list): toma la lista de heroes para recorrerla y buscar al heroe mas alto o bajo
        maximo (bool) = True: si es true por defecto busca al heroe mas alto, si es false busca al heroe mas bajo

    Returns:
        dict: retorna un diccionario con todos los datos del heroe mas alto o bajo depende de lo que busques
    """
    stark_normalizar_datos(lista)
    maximo_minimo = encontrar_extremo_manual(lista,"altura", maximo)
    heroe_max_altura = filtrar_lista(lambda heroe: heroe["altura"] == maximo_minimo, lista)
    return heroe_max_altura

# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
def promedio_campo_heroes(lista:list, campo:str)->float:  
    """
    Calcula el promedio de un campo específico en una lista de héroes.

    Args:
        lista (list): Lista de héroes.
        campo (str): Campo sobre el cual se calculará el promedio.

    Returns:
        Promedio del campo especificado.
    """
    acumulador = 0
    cantidad = len(lista)
    if cantidad > 0:
        for heroe in lista:
            acumulador += heroe[campo]
        return acumulador / cantidad
    return 0

def promedio_altura(lista:list)->float:
    """
    Calcula el promedio de la altura de los superhéroes en una lista.

    Args:
        lista (list): Lista de superhéroes.

    Returns:
        Promedio de la altura de los superhéroes.
    """
    return promedio_campo_heroes(lista,"altura")


# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)

def informar_nombre_max_min(lista:list)->None:
    """
    Imprime por consola los nombres de los superhéroes asociados a los valores extremos de altura.

    Args:
        lista (list): Lista de superhéroes.
    """
    maximo = heroe_mas_alto_bajo(lista)
    minimo = heroe_mas_alto_bajo(lista, False)

    print("Los heroes mas altos son:")
    imprimir_personajes_nombre(maximo)
    print("-------------------------------------")
    print("Los heroes mas bajos son:")
    imprimir_personajes_nombre(minimo)



# H. Calcular e informar cual es el superhéroe más y menos pesado.
def heroe_max_min_peso(lista:list)->None:
    """
    Imprime por consola los nombres de los superhéroes más y menos pesados en una lista.

    Args:
        lista (list): Lista de superhéroes.
    """
    stark_normalizar_datos(lista)
    maximo = encontrar_extremo_manual(lista,"peso")
    minimo = encontrar_extremo_manual(lista,"peso", False)
    heroe_min = heroe_max_altura = filtrar_lista(lambda heroe: heroe["peso"] == minimo, lista)
    heroe_max = heroe_max_altura = filtrar_lista(lambda heroe: heroe["peso"] == maximo, lista)

    print("El/los heroe/s mas pesado/s son:")
    imprimir_personajes_nombre(heroe_max)
    print("-------------------------------------")
    print("El/los heroe/s mas pesado/s son:")
    imprimir_personajes_nombre(heroe_min)
    
    


# I. Ordenar el código implementando una función para cada uno de los valores
# informados.



# J. Construir un menú que permita elegir qué dato obtener
def mostrar_menu():
    """
    Muestra un menú de opciones por consola.
    """
    print("\n*** Menú de opciones ***")
    print("1. Mostrar todos los héroes")
    print("2. Mostrar nombres de los héroes")
    print("3. Mostrar nombres y alturas de los héroes")
    print("4. Mostrar el héroe más alto")
    print("5. Mostrar el héroe más bajo")
    print("6. Mostrar el promedio de altura de los héroes")
    print("7. Mostrar héroes asociados a valores extremos de altura")
    print("8. Mostrar héroes más y menos pesados")
    print("9. Salir")

def main_desafio_00(lista_heroes: list):
    """
    Función principal para el desafío #00.

    Args:
        lista_heroes (list): Lista de héroes.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case '1':
                mostrar_heroes(lista_heroes)
            case '2':
                imprimir_personajes_nombre(lista_heroes)
            case '3':
                imprimir_personajes_nombre_altura(lista_heroes)
            case '4':
                heroe_mas_alto = heroe_mas_alto_bajo(lista_heroes)
                print("El/los héroe/s más alto/s es/son:")
                imprimir_personajes_nombre(heroe_mas_alto)
            case '5':
                heroe_mas_bajo = heroe_mas_alto_bajo(lista_heroes, False)
                print("El/los héroe/s más bajo/s es/son:")
                imprimir_personajes_nombre(heroe_mas_bajo)
            case '6':
                promedio = promedio_campo_heroes(lista_heroes, "altura")
                print(f"El promedio de altura de los héroes es: {promedio:.2f}")
            case '7':
                informar_nombre_max_min(lista_heroes)
            case '8':
                heroe_max_min_peso(lista_heroes)
            case '9':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")




    










    
