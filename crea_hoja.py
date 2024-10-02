from hojaexcel import *

def crea_hoja ():


    a=HojaExcel(f'{NOMBRE_FICHERO}.xlsx',OPERACIONES_POR_FILA,CELDAS_POR_OPERACION)

    opes=OPERACIONES.split()
    errores=""
    for i in range(len(open)):
         ope=opes[i]
         b=None 
         
         terminos=ope.split("*")
         if len(terminos)==2:
            b=Multiplicacion() 
            b.LoadTerminos(terminos)
            a.add_operacion(b)
         
         terminos=ope.split(":")
         if len(terminos)==2:
            if terminos[0] < terminos[1]:
                  errores+=f"En la operacion {i+1}ª ' {terminos} '  el divisor es mayor que el dividendo."+"\n"
            else:
                  b=Division() 
                  b.LoadTerminos(terminos)
                  a.add_operacion(b)
            
         if b is None:
                   errores+=f"Ls operacion {i+1}ª ' {terminos} ' no se puede incorporar '."+"\n"
    
    if errores !="" :
             


    b=Suma()
    b.LoadTerminos([3478,2496])
    a.add_operacion(b)

    b=Suma()
    b.LoadTerminos([23,44,17,3,2])
    a.add_operacion(b)

    b=Resta()
    b.LoadTerminos([234578,22235])
    a.add_operacion(b)

    b=Resta()
    b.LoadTerminos([897623,127266])
    a.add_operacion(b)

    b=Multiplicacion()
    b.LoadTerminos([98012,23])
    a.add_operacion(b)

    b=Multiplicacion()
    b.LoadTerminos([62345,123])
    a.add_operacion(b)



    b=Division()
    b.LoadTerminos([574345,2351])
    a.add_operacion(b)


    b=Division()
    b.LoadTerminos([133456,235])
    a.add_operacion(b)





    a.carga_operaciones()
    a.graba_hoja()





