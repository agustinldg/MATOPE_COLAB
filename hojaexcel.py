#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:10:10 2017

@author: aldg
"""
from operacion import Regla, Operacion,Suma,Resta,Multiplicacion,Division

from openpyxl import Workbook
#from openpyxl.compat import range
from openpyxl.utils import get_column_letter

from openpyxl.formatting import Rule
from openpyxl.styles import Font, PatternFill, Border, Side,Alignment
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
# from openpyxl.styles.colors import RED,GREEN,DARKGREEN,DARKRED
from openpyxl.worksheet.datavalidation import DataValidation

from constantes import *





class HojaExcel:
    def __init__ (self, nombre, operaciones_por_fila=3, celdas_por_operacion=10):
        self.nombre = nombre
        self.operaciones_por_fila = operaciones_por_fila
        self.celdas_por_operacion = celdas_por_operacion

        self.operaciones=[]
        self.wb = Workbook()
        self.ws1 = self.wb.active
        self.ws1.title = "Operaciones"

        self.celdanivel="$N$2"
        self.celdanivelcombo="$H$2"
        self.inicializa()

    def inicializa(self):
        self.ws1.freeze_panes='A3'
        for n in range(1,int(20*self.celdas_por_operacion/self.operaciones_por_fila)):
            self.ws1.row_dimensions[n].height=12
        self.ws1.row_dimensions[2].height=24

        for n in range(1,self.operaciones_por_fila*self.celdas_por_operacion+30):
            self.ws1.column_dimensions[ get_column_letter(n)].width=2
            #self.ws1.column_dimensions[get_column_letter(n)].font =Font(bold=True)


        for y in range(1,int(120*self.celdas_por_operacion/self.operaciones_por_fila)):
            for x in range(1, self.operaciones_por_fila * self.celdas_por_operacion + 30):
                self.ws1.cell(row=y, column=x).alignment  = Alignment(horizontal="center", vertical="center")
                self.ws1.cell(row=y, column=x).font=Font(bold=True)
# al = Alignment(horizontal="center", vertical="center")




        celdanivelcombo=self.celdanivelcombo
        celdanivel = self.celdanivel

        self.ws1.merge_cells('C2:G2')
        self.ws1["C2"].font=Font(bold=True,size=14,color="0066FF")
        self.ws1["C2"]="MODO = "

        self.ws1.merge_cells('H2:M2')

        dv = DataValidation(type="list", formula1='"Fácil,Pro,SuperPro"', allow_blank=False,showDropDown=False)
        self.ws1.add_data_validation(dv)

        self.ws1[celdanivelcombo].font=Font(bold=True,size=15,color="0066FF")
        self.ws1[celdanivelcombo] ="Fácil"
        dv.add(self.ws1[celdanivelcombo])

        self.ws1[celdanivel]='=IF('+celdanivelcombo+'="Fácil",0,IF('+celdanivelcombo+'= "Pro",1,IF('+celdanivelcombo+'= "SuperPro",2,"")))'
        self.ws1[celdanivel].font =Font(color="FFFFFF")

# RESUELTAS
        self.ws1.merge_cells('P2:V2')
        self.ws1["P2"].font=Font(bold=True,size=14,color="04B431")
        self.ws1["P2"]="RESUELTAS ="

        self.ws1.merge_cells('W2:Z2')
        self.ws1["W2"].font = Font(bold=True, size=20, color="04B431")
        self.ws1["W2"]='=COUNTIF(1:1,"=1")'

#faltan
        self.ws1.merge_cells('AA2:AF2')
        self.ws1["AA2"].font=Font(bold=True,size=14,color="DF0101")
        self.ws1["AA2"]="FALTAN ="

        self.ws1.merge_cells('AG2:AJ2')
        self.ws1["AG2"].font = Font(bold=True, size=20, color="DF0101")
        self.ws1["AG2"]='=COUNTIF(1:1,"=0")'

# =CONTAR.SI(1:1;"=0")



    def add_operacion(self,ope):
        self.operaciones.append(ope)




    def carga_operaciones(self):


        self.x_operacion=0
        self.y_operacion=0

        for ope in self.operaciones:
            self.carga_operacion(ope)
            self.x_operacion=(self.x_operacion+1)% self.operaciones_por_fila
            if self.x_operacion==0 :
                self.y_operacion+=1
            print (ope ,ope.terminos,"--> OK")

    def carga_operacion(self,ope):
        desp_x=self.x_operacion*self.celdas_por_operacion+CFG_MARGEN_X
        desp_y=self.y_operacion*self.celdas_por_operacion+CFG_MARGEN_Y
        izqui=ope.GetIzquierda()

        tx,ty=ope.GetTamano()
        desp_x=desp_x+int((self.celdas_por_operacion-tx)/2)-izqui
        desp_y=desp_y+int((self.celdas_por_operacion-ty)/2)

        greenFill = PatternFill("solid", bgColor ="E0F8E6")
        colordarkgreen="2EFE2E"
        darkgreenFill = PatternFill("solid", bgColor = colordarkgreen)


        # T_ENUNCIADO,T_ENUNCIADO_SIGNO
        for n in [ r for r in ope.reglas if r.tipo in(T_ENUNCIADO,T_ENUNCIADO_SIGNO)  ]:
            self.ws1.cell(column=n.posx+desp_x, row=n.posy+desp_y,value=n.valor)

        # T_ENUNCIADO_BORDE_INFERIOR
        thick = Side(border_style='medium', color="000000")
        bottom = Border( bottom=thick)
        for n in [ r for r in ope.reglas if r.tipo==T_ENUNCIADO_BORDE_INFERIOR]:
            self.ws1.cell(column=n.posx + desp_x, row=n.posy + desp_y).border=bottom

        # T_ENUNCIADO_BORDE_INFERIOR_IZQ
        thick = Side(border_style='medium', color="000000")
        bottom = Border( bottom=thick,left=thick)
        for n in [ r for r in ope.reglas if r.tipo==T_ENUNCIADO_BORDE_INFERIOR_IZQ]:
            self.ws1.cell(column=n.posx + desp_x, row=n.posy + desp_y).border=bottom


        # T_FC_RESULTADO_RANGE
        # darkgreenFill = PatternFill(start_color=RED , end_color=RED,
        #                         fill_type='solid')



        formula = "AND("
        rango = []
        for n in [r for r in ope.reglas if r.tipo == T_FC_RESULTADO_RANGE]:

            if formula != "AND(":
                formula+=","

            rango.append("$" + get_column_letter(n.posx + desp_x) + "$" + str(n.posy + desp_y) \
                   + ":$" + get_column_letter(n.posx + desp_x + len(n.valor) - 1) + "$" + str(n.posy + desp_y))
            # print( rango)

            for c in range(n.posx, n.posx + len(n.valor) ):
                if formula!="AND(" and formula[-1]!=',' :
                    formula+="&"
                formula += "$" + get_column_letter(c +desp_x) + "$" + str(n.posy +desp_y)
            formula += '&"" ="' + str(n.valor) + '"'   # le concateno un texto vacio "" para convertirlo a texto cuando solo hay un digito
            # print(formula)
        formula +=")"   # cierro el AND de la formula excel
        # print(formula)

        celdaformula="$"+get_column_letter(self.y_operacion*self.operaciones_por_fila+ self.x_operacion +1)+"$1"
        self.ws1[celdaformula]="=IF("+formula+",1,0)"
        self.ws1[celdaformula].font=Font(color="FFFFFF")
        self.ws1.conditional_formatting.add(celdaformula,   FormulaRule(formula=[celdaformula+"=1"], font=Font(color=colordarkgreen), fill=darkgreenFill))


        formula="$"+get_column_letter(self.y_operacion*self.operaciones_por_fila+ self.x_operacion +1)+"$1=1"
        formula = 'AND(' + self.celdanivel + '<2,' + formula + ')'
        for rg in rango:
          self.ws1.conditional_formatting.add(rg,
                                           FormulaRule(formula=[formula], fill=darkgreenFill))

        # T_FC_RESULTADO

        for n in [ r for r in ope.reglas if r.tipo==T_FC_RESULTADO ]:
             formula="$"+get_column_letter(n.posx+desp_x)+"$"+str(n.posy+desp_y)+'= '+str(n.valor)
             if n.valor==0:
                 formula='AND(NOT(ISBLANK('+"$"+get_column_letter(n.posx+desp_x)+"$"+str(n.posy+desp_y)+')),'+formula+')'

             formula='AND('+self.celdanivel +'=0,'+formula+')'

             self.ws1.conditional_formatting.add("$"+get_column_letter(n.posx+desp_x)+"$"+str(n.posy+desp_y),FormulaRule(formula=[formula], fill=greenFill))

             # print("formula: "+"$"+get_column_letter(n.posx+desp_x)+"$"+str(n.posy+desp_y),formula)


    def graba_hoja(self):
        self.wb.save(filename = self.nombre)

