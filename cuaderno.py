

import builtins


from crea_hoja import crea_hoja

# builtins.built_in_no_usage = set(dir(__builtins__)+['built_in_no_usage']) # Set of all built-in names



Nombre_de_la_hoja_Excel="2a_Excel_test"
Lista_de_operaciones="  42:3 123+4 279992*1 327:1 12+23+45+4344 12:3 12345:6"

Tamano_numeros=22  # font size 11







builtins.CFG_NOMBRE_FICHERO=Nombre_de_la_hoja_Excel
builtins.CFG_OPERACIONES =Lista_de_operaciones

builtins.CFG_FONT_SIZE =Tamano_numeros


builtins.CFG_OPERACIONES_POR_FILA=5
builtins.CFG_CELDAS_POR_OPERACION=12


builtins.CFG_MARGEN_DERECHO=20




builtins.CFG_MARGEN_X=4
builtins.CFG_MARGEN_Y=3






crea_hoja()
