from UTN_Heroes_Dataset.utn_pp import (
    mostrar_matriz_texto_tabla, 
    clear_console, color_text, get_original_matrix
)

def matriz_maker(matriz:list[list]) -> list[list]:
    """_summary_
        Esta funcion cambia el formato de matrices paralelas y las
        encapsula a todas en listas independientes una de la otra

    Args:
        matriz (_type_): _description_
    """
    matriz_nueva = []
    lista = []
    for items in range(len(matriz[0])):
        lista.append(items + 1) 
        for cosas in range(len(matriz)):
            lista.append(matriz[cosas][items])
        matriz_nueva.append(lista)
        lista = []
    return(matriz_nueva)


def mostrar_matriz(matriz:list[list]) -> None:
    
    """Mostrar: mostrara una matriz en columnas

    Args:
        matriz (list): Matriz ingresada que se desea mostrar
    """
    encabezados = ['Indice Garage', 'Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']

    mostrar_matriz_texto_tabla(matriz_maker(matriz), encabezados, "grid")

def sumar_cantidades(matriz:list[list], indice:int) -> int:
    """_summary_

    Args:
        matriz (list[list]): _description_
        indice (int): _description_

    Returns:
        int: _description_
    """

    total = 0
    for items in matriz[indice]:
        total += items
    return total

def menor_cantidad(matriz:list[list], indice:int)-> int:
    """_summary_
        la funcion el dato de menor valor de el indice indicadol
    Args:   
        matriz (list[list]): matriz en la cual se buscara
        indice (int): indice en el que se buscara

    Returns:
        int: resultado de menor valor
    """
    menor = None
    for items in range(len (matriz[indice])):
        if menor == None or (menor > matriz[indice][items]):
            menor = matriz[indice][items]
    return menor

def coincidencias(matriz: list[list], indice:int, dato:int)-> None:
    """_summary_
        busca coincidencias en una matriz con un dato pre-selecto
    Args:
        matriz (list[list]): matriz en la cual se buscara
        indice (int): indice en el que se buscara
        dato (int): dato con el que se busca coincidir
    """
    texto = ""
    for cosas in range (len(matriz[indice])):
        if matriz[indice][cosas] == dato:
            for items in range(len(matriz)):
                if type(matriz[items][cosas]) == str:
                    texto += f"{matriz[items][cosas]:15} |" 
                else:
                    texto += f"{matriz[items][cosas]:5} |" 
            print(texto)
            texto = ""

def mayor_cantidad(matriz:list[list], indice:int)-> int:    

    """_summary_
        la funcion el dato de mayor valor de el indice indicadol
    Args:   
        matriz (list[list]): matriz en la cual se buscara
        indice (int): indice en el que se buscara

    Returns:
        int: resultado de mayor valor
    """
    mayor = None
    for items in range(len (matriz[indice])):
        if mayor == None or (mayor < matriz[indice][items]):
            mayor = matriz[indice][items]
    return mayor

def recaudaciones(matriz:list[list])-> list[list]:
    matriz_nueva = matriz_maker(matriz)
    for items in range(len(matriz_nueva)):
        recaudaciones = matriz_nueva[items][3] * matriz_nueva[items][4]
        matriz_nueva[items][5] = recaudaciones
    return matriz_nueva

def mayor_que(matriz:list[list], numero:int, indice:int)-> int:
    total = 0
    for items in matriz[indice]:
        if items >= numero:
            total += 1
    return total

def porcentajes(matriz: list[list])-> None:
    mensaje = ""
    total = sumar_cantidades(matriz, 2)
    for items in range(len(matriz[2])):
        porcentaje = (matriz[2][items] * 100)/total
        porcentaje = str(porcentaje)[:5]
        mensaje += f"Porcentaje del garaje N°{items+1} = {porcentaje} % \n"
        print(mensaje)
        mensaje = ""

def ordenar(matriz: list[list], posicion:int):
    for indice in range(len(matriz) - 1 ):
        indice_2 = indice
        for items in range(indice + 1, len(matriz[posicion])):
            if int(matriz[posicion][items]) > int(matriz[posicion][indice_2]):
                indice_2 = items
        if indice_2 != indice:

            for listas in range(len(matriz)):
                matriz[listas][indice], matriz[listas][indice_2] = matriz[listas][indice_2], matriz[listas][indice]
    return matriz


    


