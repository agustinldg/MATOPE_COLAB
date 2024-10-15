from hojaexcel import *
from constantes import *
from datetime import datetime
import requests
import json
import builtins

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



   variables_usuario = {
      key: value
      for key, value in builtins.__dict__.items()
      if key not in built_in_no_usage  and key.isupper() # Exclude built-in names
   }

   url = "https://script.google.com/macros/s/AKfycbxM7zHjcOLxu02w2OrzUaicr5tkhiNElPZV-23D82SlLE2D0lgaj9y2oPLuoeBiuYb8/exec"
   payload = json.dumps({
   "fecha":  datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,
   "user": "NA",
   "file": f'{NOMBRE_FICHERO}.xlsx',
   "opes": OPERACIONES,
   "error": 'OK' if errores =="\n" else errores,
   "params": json.dumps(variables_usuario, indent=4)})
   headers = {
   'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   if not response.ok:
     print(response.text)
   else:
     print("Usage archivado OK") 

   if errores !="\n" :
            print ("La Hoja de Cálculo no se ha generado KO")
    
            print
            print ("Errores:")
            print (errores)
   
            raise RuntimeError(errores)
   else:
      print("Hoja de Cálculo generada.")        



