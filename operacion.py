#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:53:38 2017

@author: aldg
"""
from constantes import *
import random

class Regla:
    def __init__(self, tipo, valor, posx,posy , test_valor=None,test_posx=None,test_posy=None):
        self.tipo = tipo
        self.valor = valor
        self.posx = posx
        self.posy = posy
        self.test_valor=test_valor
        self.test_posx=test_posx
        self.test_posy=test_posy
        # los valores test comprubean una casilla que no son las que se van a ver afectadas (para resta auxiliares en division)
    def __repr__(self):
        return "Regla[%i, %s, %i, %i, %s, %i, %i]" % (self.tipo, self.valor, self.posx, self.posy, self.test_valor, self.test_posx, self.test_posy)


class Operacion:
  
#    matrix = []
#    for row in range(10):
#       matrix.append([Celda("a","b")] * 10)
    def __init__(self):
        """

        :rtype:
        """
        self.reglas = []
        self.terminos=[]
        self.x=0
        self.y=0
    tipo=0
    def setTipo(self,tipo):
        self.tipo=tipo

    def setXy(self,posx,posy):
        self.x=posx
        self.y=posy
    
    

    # def appendRegla(self,tipo, valor, posx,posy):
    #     self.reglas.append(Regla(tipo,valor,posx,posy))
    # def appendDRegla(self,tipo, valor, posx,posy):
    #     self.appendRegla(tipo,valor,posx-len(str(valor))+1 ,posy)        


    def appendRegla(self,tipo, valor, posx,posy, test_valor=None,test_posx=None,test_posy=None):
        self.reglas.append(Regla(tipo,valor,posx,posy, test_valor,test_posx,test_posy))
    def appendDRegla(self,tipo, valor, posx,posy ,test_valor=None,test_posx=None,test_posy=None):
        self.appendRegla(tipo,valor,posx-len(str(valor))+1 ,posy, test_valor,test_posx,test_posy)




    def escribe (self):
        for r in self.reglas:
            print (r)

    def printCaracter(self,caracter)    :
        if caracter.isdigit():
            c=int(caracter)
        else:
            c=caracter
        self.appendRegla(self.tipo,c,self.x,self.y)
        self.x+=1
        
    def printLn(self)    :
        self.y+=1
    
    def printICadena(self,cadena)     :
         for c in cadena:
             self.printCaracter(c)

    def printDCadena(self,cadena,posx)     :
        self.x=posx-len(cadena)+1 
        self.printICadena(cadena)
    
    def LoadTerminos(self,terminos)  :                        
        self.terminos=terminos
        self.LoadReglas()          
        
    def GetAncho(self):
        l=[r.posx for r in self.reglas]
        return (max(l)-min(l))
    def GetAlto(self):
        l=[r.posy for r in self.reglas]
        return (max(l)-min(l))
    def GetTamano(self):
        return self.GetAncho(),self.GetAlto()
    def GetIzquierda(self):
        return min([r.posx for r in self.reglas])
             
      
class Suma(Operacion):
        def LoadTerminosAleatorios(self):
          llevadas=random.choice([True,True, False])
          ndigitos=random.randint(1, 7)
          nterminos=random.randint(2, 5)
          if nterminos>3:
              llevadas=True
          dificultad=[llevadas,ndigitos,nterminos]
          self.LoadTerminosDificultad(dificultad)

        def LoadTerminosDificultad(self, dificultad):
            llevadas=dificultad[0]
            ndigitos=dificultad[1]
            nterminos=dificultad[2]
            terminos=[]
            if llevadas :
                terminos.append( random.randint(10 ** (ndigitos - 1), 10 ** ndigitos - 1))
                for n in range (nterminos-1):
                    terminos.append(random.randint(10 ** (ndigitos - 1), 10 ** ndigitos - 1))
            else:
                terminos.append( random.randint(10 ** (ndigitos - 1), 10 ** ndigitos - 1))
                for n in range(nterminos - 1):
                    sumando=''
                    for p in range(0,len(str(terminos[0]))):
                        suma=0
                        for ter in terminos:
                            suma+=int(str(ter).rjust(len(str(terminos[0])),'0')[p])
                        sumando+=str(random.randint(0,9-suma))
                    terminos.append(int(sumando))
            self.terminos = terminos
            self.LoadReglas()
        def LoadReglas(self):
            self.setTipo(T_ENUNCIADO)
            for t in self.terminos:
                self.printDCadena(str(t),CFG_MARGEN_DERECHO)
                self.printLn()

            self.setTipo(T_ENUNCIADO_SIGNO)
            self.setXy( CFG_MARGEN_DERECHO-self.GetAncho()-1,self.y-1)
            self.printCaracter("+")
            self.printLn()

            self.setTipo(T_FC_RESULTADO)
            resultado=sum(self.terminos)
            self.printDCadena(str(resultado), CFG_MARGEN_DERECHO)
            self.appendDRegla(T_FC_RESULTADO_RANGE, str(resultado), CFG_MARGEN_DERECHO,self.y)

            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
            self.setXy( CFG_MARGEN_DERECHO-self.GetAncho(),self.y-1)
            self.printICadena(" "*(CFG_MARGEN_DERECHO-self.x+1))

class Resta(Operacion):
    def LoadTerminosAleatorios(self):
        llevadas = random.choice([True,  False])
        ndigitos = random.randint(1, 9)

        dificultad = [llevadas, ndigitos]
        self.LoadTerminosDificultad(dificultad)



    def LoadTerminosDificultad(self, dificultad):
        llevadas = dificultad[0]
        ndigitos = dificultad[1]
        terminos = []

        if llevadas:
            terminos.append(random.randint(10 ** (ndigitos - 1), 10 ** ndigitos - 1))
            terminos.append(random.randint(1, terminos[0]))
        else:
            terminos.append(random.randint(10 ** (ndigitos - 1), 10 ** ndigitos - 1))

            sustraendo = ''
            for p in range(0, len(str(terminos[0]))):
                sustraendo += str(random.randint(0, int(str(terminos[0])[p])   ))
            terminos.append(int(sustraendo))
        self.terminos = terminos
        self.LoadReglas()

    def LoadReglas(self):


        sustraendo=self.terminos[0]
        minuendo=self.terminos[1]
        self.setTipo(T_ENUNCIADO)
        self.printDCadena(str(sustraendo),CFG_MARGEN_DERECHO)
        self.printLn()
        self.printDCadena(str(minuendo), CFG_MARGEN_DERECHO)
        self.printLn()

        self.setTipo(T_ENUNCIADO_SIGNO)
        self.setXy( CFG_MARGEN_DERECHO-self.GetAncho()-1,self.y-1)
        self.printCaracter("-")
        self.printLn()


        self.setTipo(T_FC_RESULTADO)
        resultado=sustraendo-minuendo
        resultado='0'*(len(str(sustraendo))-len(str(resultado)))+str(resultado)
        self.printDCadena(resultado, CFG_MARGEN_DERECHO)
        self.appendDRegla(T_FC_RESULTADO_RANGE, resultado, CFG_MARGEN_DERECHO,self.y)

        self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
        self.setXy( CFG_MARGEN_DERECHO-self.GetAncho(),self.y-1)
        self.printICadena(" "*(CFG_MARGEN_DERECHO-self.x+1))
            
            
class Multiplicacion(Operacion):
        def LoadTerminosAleatorios(self):
            ceros = random.choice([True, False])
            ndigitosfactor1 = random.randint(1, 6)
            ndigitosfactor2 = min(random.randint(1, 3,),ndigitosfactor1)

            dificultad = [ceros, ndigitosfactor1,ndigitosfactor2]
            self.LoadTerminosDificultad(dificultad)

        def LoadTerminosDificultad(self, dificultad):
            ceros = dificultad[0]
            ndigitosfactor1 = dificultad[1]
            ndigitosfactor2 = dificultad[2]
            terminos = []

            if ceros:
                terminos.append(random.randint(10 ** (ndigitosfactor1 - 1), 10 ** ndigitosfactor1 - 1))
                terminos.append(random.randint(10 ** (ndigitosfactor2 - 1), 10 ** ndigitosfactor2 - 1))
            else:
                terminos.append(random.randint(10 ** (ndigitosfactor1 - 1), 10 ** ndigitosfactor1 - 1))

                factor = ''
                for p in range(0, ndigitosfactor2):
                    factor += str(random.randint(1, 9))
                terminos.append(int(factor))
            self.terminos = terminos
            self.LoadReglas()


        def LoadReglas(self):
            factor1=self.terminos[0]
            factor2=self.terminos[1]
            self.setTipo(T_ENUNCIADO)
            self.printDCadena(str(factor1),CFG_MARGEN_DERECHO)
            self.printLn()
            self.printDCadena(str(factor2), CFG_MARGEN_DERECHO)
            self.printLn()
            self.setTipo(T_ENUNCIADO_SIGNO)
            self.setXy( CFG_MARGEN_DERECHO-self.GetAncho()-1,self.y-1)
            self.printCaracter("X")
            self.printLn()
            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
            self.setXy( CFG_MARGEN_DERECHO-self.GetAncho(),self.y-1)
            self.printICadena(" "*(CFG_MARGEN_DERECHO-self.x+1))
            self.printLn()
            self.setTipo(T_FC_RESULTADO)    #<---- poner otro tipo/color
            noceros=0
            for z in str(factor2):
                if z!='0':
                    noceros+=1
            if noceros>1:   # no contar los caracteres =0
                n=0
                for f in reversed(str(factor2)):
                    if f != '0' :
                         self.printDCadena(str(factor1*int(f)*10**n), CFG_MARGEN_DERECHO)
                         self.printLn()
                    n+=1
                self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
                self.setXy(CFG_MARGEN_DERECHO - self.GetAncho(), self.y - 1)
                self.printICadena(" " * (CFG_MARGEN_DERECHO - self.x + 1))
                self.printLn()

            self.setTipo(T_FC_RESULTADO)
            resultado = factor1*factor2
            resultado = str(resultado)
            self.printDCadena(resultado, CFG_MARGEN_DERECHO)
            self.appendDRegla(T_FC_RESULTADO_RANGE, resultado, CFG_MARGEN_DERECHO, self.y)



class Division(Operacion):

        def LoadTerminosAleatorios(self):
            restocero = random.choice([True,False])
            CocienteUndigito=random.choice([True,False])
              #  ['Resto0', 'NoResto0','CocienteUndigito'])

            ndigitosdividendo = random.randint(2, 8)
            ndigitosdivisor = min(random.randint(1, 1,),ndigitosdividendo)

            dificultad = [restocero,CocienteUndigito, ndigitosdividendo,ndigitosdivisor]
            self.LoadTerminosDificultad(dificultad)

        def LoadTerminosDificultad(self, dificultad):
            restocero = dificultad[0]
            CocienteUndigito=dificultad[1]
            ndigitosdividendo = dificultad[2]
            ndigitosdivisor = dificultad[3]
            terminos = []
            if not CocienteUndigito:
                if  restocero:
                    divisor=random.randint(10 ** (ndigitosdivisor - 1), 10 ** ndigitosdivisor - 1)
                    dividendo=random.randint(max(divisor,10 ** (ndigitosdividendo - 1)    ), 10 ** ndigitosdividendo - 1)
                    dividendo=int(dividendo/divisor)*divisor
                else :  #'NoResto0':
                    divisor = random.randint(10 ** (ndigitosdivisor - 1), 10 ** ndigitosdivisor - 1)
                    dividendo = random.randint(max(divisor,10 ** (ndigitosdividendo - 1)  ), 10 ** ndigitosdividendo - 1)
            else:
                cociente=random.randint(1,9)
                divisor=random.randint(2,9)
                dividendo=cociente*divisor
                if  not restocero :
                    dividendo+= random.randint(1, divisor - 1)

            terminos.append(dividendo)
            terminos.append(divisor)

            self.terminos = terminos
            self.LoadReglas()





        def LoadReglas(self):
            dividendo=str(self.terminos[0])
            divisor=str(self.terminos[1])
            cociente=int(int(dividendo)/int(divisor))


            self.setTipo(T_ENUNCIADO)
            self.setXy(0,0)
            self.printICadena(str(dividendo))
            self.printICadena(str(divisor))

            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR_IZQ)
            self.setXy( len(str(dividendo)),0)
            self.printICadena(" ")
            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
            self.printICadena(" "*(max(len(str(cociente)),len(str(divisor)))-1))

            self.setTipo(T_FC_RESULTADO)
            self.setXy( len(str(dividendo)),1)
            self.printICadena(str(cociente))

            self.appendRegla(T_FC_RESULTADO_RANGE, str(cociente), len(str(dividendo)),1)

            col = len(str(divisor))
            resto = str(dividendo)[0:col]
            self.setTipo(T_FC_RESULTADO)
            self.setXy(0, 0)
            lenanteriorresto = 0

            while True:
                while int(resto) < int(divisor) and col < len(dividendo):
                    resto = resto + dividendo[col]
                    col += 1
                lenanteriorresto = len(resto)
                resto = str(int(resto) % int(divisor))

                while int(resto) < int(divisor) and col < len(dividendo):  # bajo uno
                    resto = resto + dividendo[col]
                    col += 1

                if (len(resto) +1) < lenanteriorresto:
                    resto = '0' + resto
                self.setXy(col-len(resto), self.y + 1)
                self.printICadena(resto)

                if col >= len(dividendo) and int(resto) < int(divisor):
                    break
            self.appendRegla(T_FC_RESULTADO_RANGE,resto, col-len(resto), self.y )


class Division_con_restas(Division):
        def LoadReglas(self):
            dividendo=str(self.terminos[0])
            divisor=str(self.terminos[1])
            cociente=int(int(dividendo)/int(divisor))


            self.setTipo(T_ENUNCIADO)
            self.setXy(0,0)
            self.printICadena(str(dividendo))
            self.printICadena(str(divisor))

            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR_IZQ)
            self.setXy( len(str(dividendo)),0)
            self.printICadena(" ")
            self.setTipo(T_ENUNCIADO_BORDE_INFERIOR)
            self.printICadena(" "*(max(len(str(cociente)),len(str(divisor)))-1))

            self.setTipo(T_FC_RESULTADO)
            self.setXy( len(str(dividendo)),1)
            self.printICadena(str(cociente))

            self.appendRegla(T_FC_RESULTADO_RANGE, str(cociente), len(str(dividendo)),1)

            col = len(str(divisor))
            resto = str(dividendo)[0:col]
            self.setTipo(T_FC_RESULTADO)
            self.setXy(0, 0)
            anteriorresto = ""
            n_resta=1   #numero de el  sustraendo de la resta 1 correponde al proucto del divisor*conciente[r_resta-1]

            while True:
                while int(resto) < int(divisor) and col < len(dividendo):
                    resto = resto + dividendo[col]
                    col += 1

                anteriorresto = resto
                resto = str(int(resto) % int(divisor))

                # añado resta
                
                tmp_sustraendo=int(divisor)*int(str(cociente)[n_resta-1])
                tmp_sustraendo=str(tmp_sustraendo).zfill(len(str(int(anteriorresto))))
                self.setXy(col-len(tmp_sustraendo)-1, self.y + 1)

                self.setTipo(T_ENUNCIADO_RESTA_DIVI)
                self.printCaracter("-")

                self.setTipo(T_FC_RESULTADO)
                self.printICadena(tmp_sustraendo)

                
 


                self.appendRegla(T_FC_RESULTADO_SIGNO_RESTA_DIVI," "*1, col-len(tmp_sustraendo)-1, self.y,
                                  str(cociente)[n_resta-1], len(str(dividendo))+n_resta-1,1  )

                self.appendRegla(T_FC_RESULTADO_RESTA_DIVI," "*(len(tmp_sustraendo)+1), col-len(tmp_sustraendo)-1, self.y ,
                                  str(cociente)[n_resta-1], len(str(dividendo))+n_resta-1,1  )



                # fin  resta


                digitos_bajados=0
                while int(resto) < int(divisor) and col < len(dividendo):  # bajo uno
                    resto = resto + dividendo[col]
                    col += 1
                    digitos_bajados+=1

                #if (len(resto) +1) < len(anteriorresto):
                #    resto = '0' + resto

                resto=resto.zfill(  len(str(int(anteriorresto)))   + digitos_bajados )    
                self.setTipo(T_FC_RESULTADO)
                self.setXy(col-len(resto), self.y + 1)
                self.printICadena(resto)

                if col >= len(dividendo) and int(resto) < int(divisor):
                    break

                #resta    
                n_resta+=1
                while str(cociente)[n_resta-1] =='0' and len(str(cociente))>(n_resta-1+1):
                    n_resta+=1

            self.appendRegla(T_FC_RESULTADO_RANGE,resto, col-len(resto), self.y )

            # relleno las casillas vacias con <>' ' par que se pongan en error T_FC_RESULTADO  si se rellenan

            
            celdas_rellenas=  {(regl.posx+n,regl.posy) for regl in self.reglas  for n in range(len(str( regl.valor) ))  }
            
       

            cuadricula=  {(x,y)  for x in   range(
                              min( coordenada[0] for coordenada in celdas_rellenas),
                              max( coordenada[0] for coordenada in celdas_rellenas) +2)  
                                    for y in   range(
                                        min( coordenada[1] for coordenada in celdas_rellenas),
                                        max( coordenada[1] for coordenada in celdas_rellenas) +2)  
                          }

            for coordenada in (cuadricula-celdas_rellenas):
                self.appendRegla(T_FC_ESCRITO_FUERA,'" "', coordenada[0], coordenada[1] )


  