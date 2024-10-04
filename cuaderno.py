

import builtins
from crea_hoja import crea_hoja


builtins.built_in_no_usage = set(dir(__builtins__)+['built_in_no_usage']) # Set of all built-in names








builtins.NOMBRE_FICHERO="2a_Excel_test"
builtins.OPERACIONES ="  123+4 279992*1 327:1 12+23+45+4344 12:3 12345:6"


builtins.OPERACIONES_POR_FILA=5
builtins.CELDAS_POR_OPERACION=12


builtins.MARGEN_DERECHO=20




builtins.MARGEN_X=4
builtins.MARGEN_Y=3







crea_hoja()
