from auxiliares.funciones import *
from UTN_Heroes_Dataset.utn_pp import clear_console
matriz = get_original_matrix() 

encabezados = ['Indice Garage', 'Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']


def validar(opciones:str, mensaje: str, rango_maximo:int, rango_minimo:int) -> int:
    """_summary_
       Se ingresa un STR de las opciones a elegir y un mensaje que se quiera mostrar
       tanto como los rangos y se espera un numero entre los rangos preseleccionados
       si lo ingresado no es un numero o no esta en rango se reinicia
    Args:
        opciones (str): Opciones para seleccionar
        mensaje (str): mensaje a mostrar para seleccionar
        rango_maximo (int): rargo maximo posible para seleccionar
        rango_minimo (int): rango minimo posible para seleccionar

    Returns:
        int: seleccion correcta ya hecha
    """
    print(opciones)
    seleccion = input(mensaje)
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if rango_maximo >= seleccion >= rango_minimo:
            return(seleccion)
        else:
            clear_console()
            return validar(opciones, mensaje, rango_maximo, rango_minimo)
    else:
        clear_console()
        return validar(opciones, mensaje, rango_maximo, rango_minimo)
    
def menu(opcion: int) -> None:

    """_summary_
        Ejecuta diferentes funciones en base a una seleccion ya hecha.
    
    Args:
        opcion (int): la opcion seleccionada de entre las anteriormente mostradas
    """
    match opcion:
        case 1:
            mostrar_matriz(matriz)
        case 2:
            cantidad = sumar_cantidades(matriz, 2)
            print(f"la cantidad total de unidades vehiculares almacenadas es de {cantidad}")
        case 3:
            menor = menor_cantidad(matriz, 2)
            print("la/las coincidencias de el/los garages con menos cantidad es :")
            coincidencias(matriz, 2, menor)
        case 4:
            mayor = mayor_cantidad(matriz, 2)
            print(f"La cantidad maxima de autos que hay en un garage es de {mayor}")
        case 5:
            matriz_nueva = recaudaciones(matriz)
            mostrar_matriz_texto_tabla(matriz_nueva, encabezados, "grid")
        case 6:
            resultado = mayor_que(matriz, 6, 2)
            print(f"la cantidad de garages que almacenaron por lo menos 6 vehiculos es de {resultado}")
        case 7:
            porcentajes(matriz)
        case 8:
            nueva_matriz = recaudaciones(matriz)
            matriz_ordenada = ordenar(nueva_matriz, 4)
            mostrar_matriz_texto_tabla(matriz_ordenada, encabezados, "grid")


opciones = """

1_Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes y mostrarlos.

2_Calcular la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.

3_Datos completos del garaje que almacena menos unidades de vehículos.

4_Máxima cantidad de unidades que almacena el garaje con más unidades.

5_Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.

6_Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.

7_Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz.
Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.

8_Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.


"""

mensaje = "seleccione una de las opciones del menu siguiente"

while True:
    opcion = validar(opciones, mensaje, 8, 1)
    menu(opcion)
    clear_console()