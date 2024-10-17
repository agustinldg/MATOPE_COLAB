

import builtins


from crea_hoja import crea_hoja

# builtins.built_in_no_usage = set(dir(__builtins__)+['built_in_no_usage']) # Set of all built-in names



Nombre_de_la_hoja_Excel="4a_Excel_test"
Nombre_de_la_hoja_Excel="4a_Excel_test"
Lista_de_operaciones="  42:3 123+4 279992*1 327:1 12+23+45+4344 12:3 12345:6"

Tamano_tipo_de_letra=26  # font size 11

Color_Respuesta_Final_Correcta='2EFE2E'    #2EFE2E darkgreen (el de la primera versin)

Color_Respuesta_Intermedia_Correcta='FF77FF'    #E0F8E6 green (el de la lprimera version)
 


Modos_Disponibles="Fácil,Pro"
Modos_Disponibles="Fácil,Pro"

Modo_Seleccionado="SuperPro"

# @title Texto de título predeterminado
# @markdown **das d as**
# modo = "super_pro,facil" # @param ["super_pro,facil,dificil","super_pro,facil","facil"]






builtins.CFG_NOMBRE_FICHERO=Nombre_de_la_hoja_Excel
builtins.CFG_OPERACIONES =Lista_de_operaciones

builtins.CFG_FONT_SIZE =Tamano_tipo_de_letra

builtins.CFG_MODOS_DISPO=Modos_Disponibles
builtins.CFG_MODO_SELEC=Modo_Seleccionado


builtins.CFG_COLOR_FINAL_OK=Color_Respuesta_Final_Correcta
builtins.CFG_COLOR_INTERMEDIO_OK=Color_Respuesta_Intermedia_Correcta

builtins.CFG_COLOR_FINAL_OK=Color_Respuesta_Final_Correcta
builtins.CFG_COLOR_INTERMEDIO_OK=Color_Respuesta_Intermedia_Correcta

builtins.CFG_OPERACIONES_POR_FILA=4
builtins.CFG_CELDAS_POR_OPERACION=12


builtins.CFG_MARGEN_DERECHO=20




builtins.CFG_MARGEN_X=4
builtins.CFG_MARGEN_Y=3






crea_hoja()
