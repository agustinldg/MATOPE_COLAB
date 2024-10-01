from hojaexcel import *

def crea_hoja ():


    a=HojaExcel('Operaciones_Dificiles_test.xlsx',OPERACIONES_POR_FILA,CELDAS_POR_OPERACION)



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





