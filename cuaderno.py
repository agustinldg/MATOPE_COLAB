

import builtins
import re



# builtins.built_in_no_usage = set(dir(__builtins__)+['built_in_no_usage']) # Set of all built-in names



Nombre_de_la_hoja_Excel="test_resta_div40"
Lista_de_operaciones=" 12/3 12345/6 327/1 12:3 12345:6 327:1 17+19+16  34-1 12345*7"
# Lista_de_operaciones=" 12/3 123/6 327/1 12:3 123:6 327:1 17+19+16  34-1 12345*7"
#Lista_de_operaciones=" 4-3 9-6 3-1 4-3 1+6 3*1 1+6  3-1 1+7"
#Lista_de_operaciones=" 4/3 9-6 3-1 4-3 6:6 3*1 1+6  3-1 1+7"
# Lista_de_operaciones=" 4/3 9-6 3-1 4-3 6:6 3*1 123456789012345678901/12  3-1 1+7 123456789012345678901:12"
Tamano_tipo_de_letra=26  # font size 11

Color_Respuesta_Final_Correcta='2EFE2E'    #2EFE2E darkgreen (el de la primera versin)

Color_Respuesta_Intermedia_Correcta='04B431'    #E0F8E6 green (el de la lprimera version) (afecta a tinta pero facilmente cambiable a fondo)

Color_Respuesta_Intermedia_Incorrecta='FF0000'    #'FF0000' rojo 

Color_Escrito_Fuera='FF6666'   # escrito fuera de sitio rojo claro FF6666


Modos_Disponibles="Fácil,Pro"


Modo_Seleccionado="SuperPro"


Lineas_restas_auxiliares_en_divisiones_fijas=False

Minimo_celdas_por_operacion=4     #poner 4 por lo mmenso 

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
builtins.CFG_COLOR_INTERMEDIO_KO=Color_Respuesta_Intermedia_Incorrecta
builtins.CFG_COLOR_ESCRITO_FUERA=Color_Escrito_Fuera  

builtins.CFG_OPERACIONES_POR_FILA=3
builtins.CFG_MIN_CELDAS_POR_OPERACION=Minimo_celdas_por_operacion 




builtins.CFG_LINEAS_RESTA_AUX_DIVI_FIJAS=Lineas_restas_auxiliares_en_divisiones_fijas




builtins.CFG_MARGEN_DERECHO=20




builtins.CFG_MARGEN_X=4
builtins.CFG_MARGEN_Y=3

builtins.CFg_USER="Developer"


test_CFG_COLOR_FINAL_OK=bool(re.match(r"^[A-Fa-f0-9]{6}$", CFG_COLOR_FINAL_OK))
test_CFG_COLOR_INTERMEDIO_OK=bool(re.match(r"^[A-Fa-f0-9]{6}$", CFG_COLOR_INTERMEDIO_OK))
test_CFG_COLOR_INTERMEDIO_KO=bool(re.match(r"^[A-Fa-f0-9]{6}$", CFG_COLOR_INTERMEDIO_KO))
test_CFG_COLOR_ESCRITO_FUERA=bool(re.match(r"^[A-Fa-f0-9]{6}$", CFG_COLOR_ESCRITO_FUERA))


from crea_hoja import crea_hoja

if  test_CFG_COLOR_FINAL_OK and test_CFG_COLOR_INTERMEDIO_OK and test_CFG_COLOR_INTERMEDIO_KO and test_CFG_COLOR_ESCRITO_FUERA :
    crea_hoja()
else:
    print ('')
    print (f'ERROR EN LA DEFINICION de "Color_Respuesta_Final_Correcta" = {CFG_COLOR_FINAL_OK} ' if not test_CFG_COLOR_FINAL_OK else "" )
    print (f'ERROR EN LA DEFINICION de "Color_Respuesta_Intermedia_Correcta" = {CFG_COLOR_INTERMEDIO_OK} ' if not test_CFG_COLOR_INTERMEDIO_OK else "" )
    print (f'ERROR EN LA DEFINICION de "Color_Respuesta_Intermedia_Incorrecta" = {CFG_COLOR_INTERMEDIO_KO} ' if not test_CFG_COLOR_INTERMEDIO_KO else "" )
    print (f'ERROR EN LA DEFINICION de "Color_Escrito_Fuera = {CFG_COLOR_ESCRITO_FUERA} ' if not test_CFG_COLOR_ESCRITO_FUERA else "" )

    print ('Los colores se definen con 6 carácteres de 0 a 9 ó de A a F.  Ejemplo 2EFE2E')
    print ('Vuelve a ejecutar el proceso despues hacer la correción')
    print ('')


# TO_DO comprobar google formatos , margenes con el escrito fuera, tamño (por el recalculo para probela de excel que no deja ver)
#       celdas por operacion calcularlo dinamicamente