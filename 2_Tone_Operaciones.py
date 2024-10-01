
from hojaexcel import *
import random


random.seed( 1 )

a=HojaExcel('Sumas_y_Restas.xlsx',operaciones_por_fila=2,celdas_por_operacion=12)



b=Suma()
b.LoadTerminos([5,4])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([2,3])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([3,4])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([2,3,1])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([15,17])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([20,30])
a.add_operacion(b)

b=Suma()
b.LoadTerminos([20,30,12])
a.add_operacion(b)


b=Resta()
b.LoadTerminos([9,3])
a.add_operacion(b)

b=Resta()
b.LoadTerminos([7,5])
a.add_operacion(b)

b=Resta()
b.LoadTerminos([23,1])
a.add_operacion(b)

b=Resta()
b.LoadTerminos([13,5])
a.add_operacion(b)

b=Resta()
b.LoadTerminos([27,15])
a.add_operacion(b)

a.carga_operaciones()
a.graba_hoja()


a=HojaExcel('Multiplicaion_y_Division.xlsx',operaciones_por_fila=2,celdas_por_operacion=12)



b=Multiplicacion()
b.LoadTerminos([2,4])
a.add_operacion(b)

b=Multiplicacion()
b.LoadTerminos([3,8])
a.add_operacion(b)

b=Multiplicacion()
b.LoadTerminos([12,3])
a.add_operacion(b)

b=Multiplicacion()
b.LoadTerminos([22,4])
a.add_operacion(b)

b=Division()
b.LoadTerminos([8,4])
a.add_operacion(b)

b=Division()
b.LoadTerminos([9,4])
a.add_operacion(b)

b=Division()
b.LoadTerminos([48,2])
a.add_operacion(b)

b=Division()
b.LoadTerminos([23,3])
a.add_operacion(b)

a.carga_operaciones()
a.graba_hoja()


a=HojaExcel('Operaciones_Dificiles.xlsx',operaciones_por_fila=2,celdas_por_operacion=16)



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