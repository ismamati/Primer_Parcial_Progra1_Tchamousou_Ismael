from UTN_Heroes_Dataset.utn_pp import (
    get_original_matrix, mostrar_matriz_texto_tabla, 
    clear_console, color_text
)

from auxiliares.defs import *



matriz = get_original_matrix() 
mostrar_matriz(matriz)
print(sumar_cantidades(matriz, 2))