from auxiliares.menu import *

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