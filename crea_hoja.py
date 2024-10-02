from hojaexcel import *
from constantes import *
from datetime import datetime
import requests
import json

def splitope(fope,simbolo_ope):
   fope=  fope.split(simbolo_ope)
   try:
      fope=list(map(int, fope))
   except ValueError as e:   
      fope=[]  
   return   fope  

def crea_hoja ():


   a=HojaExcel(f'{NOMBRE_FICHERO}.xlsx',OPERACIONES_POR_FILA,CELDAS_POR_OPERACION)

   opes=OPERACIONES.split()
   errores="\n"
   for i in range(len(opes)):
      ope=opes[i]
      b=None 
      
      terminos=splitope(ope,'*')
      if len(terminos)==2:
         b=Multiplicacion() 
         b.LoadTerminos(terminos)
         a.add_operacion(b)

      terminos=splitope(ope,'+')
      if len(terminos)>=2:
         b=Suma() 
         b.LoadTerminos(terminos)
         a.add_operacion(b)
      
      terminos=splitope(ope,':')
      if len(terminos)==2:
         if terminos[0] < terminos[1]:
               errores+=f"En la operacion {i+1}ª ' {ope} '  el divisor es mayor que el dividendo."+"\n"
         else:
               b=Division() 
               b.LoadTerminos(terminos)
               a.add_operacion(b)

      terminos=splitope(ope,'-')
      if len(terminos)==2:
         if terminos[0] < terminos[1]:
               errores+=f"En la operacion {i+1}ª ' {ope} '  el minuendo es menor que el sustraendo."+"\n"
         else:
               b=Resta() 
               b.LoadTerminos(terminos)
               a.add_operacion(b)                  
         
      if b is None:
                  errores+=f"Ls operacion {i+1}ª ' {ope} ' no se puede incorporar ."+"\n"
   
   if errores =="\n" :
      a.carga_operaciones()
      a.graba_hoja()

   url = "https://script.google.com/macros/s/AKfycbxM7zHjcOLxu02w2OrzUaicr5tkhiNElPZV-23D82SlLE2D0lgaj9y2oPLuoeBiuYb8/exec"
   payload = json.dumps({
   "fecha":  datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
   "user": "NA",
   "file": f'{NOMBRE_FICHERO}.xlsx',
   "opes": OPERACIONES,
   "error": errores,
   "params": "raf"})
   headers = {
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.text)
   if errores !="\n" :
            raise RuntimeError(errores)




