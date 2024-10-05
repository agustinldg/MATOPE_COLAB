

import builtins
from crea_hoja import crea_hoja


builtins.built_in_no_usage = set(dir(__builtins__)+['built_in_no_usage']) # Set of all built-in names



Nombre_de_la_hoja_Excel="2a_Excel_test"
Lista_de_operaciones="  42:3 123+4 279992*1 327:1 12+23+45+4344 12:3 12345:6"








builtins.NOMBRE_FICHERO=Nombre_de_la_hoja_Excel
builtins.OPERACIONES =Lista_de_operaciones


builtins.OPERACIONES_POR_FILA=5
builtins.CELDAS_POR_OPERACION=12


builtins.MARGEN_DERECHO=20




builtins.MARGEN_X=4
builtins.MARGEN_Y=3







crea_hoja()
