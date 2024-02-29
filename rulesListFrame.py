from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Combobox, Style

from variables import *
from reglas_calidad import *
from ventana_config import * 

class rulesListFrame:
    def __init__(self,window,rules_frame):
        self.window = window
        self.rules_frame = rules_frame
        self.reglas = dic_reglas

        ##CONFIGURACION DEL FRAME RULES##
        #creacion del scrollbar
        self.scroll = Scrollbar(self.rules_frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        #creacion del listbox
        self.list = Listbox(self.rules_frame,yscrollcommand=self.scroll.set)
        self.list.pack(side= TOP, fill= BOTH,expand=True)
        #configuracion para que el scroll bar maneje el scroll de la lista
        self.scroll.config(command= self.list.yview)

        #creacion del boton de seleccion
        self.button_select = ttk.Button(self.rules_frame,text="Configurar Regla",width=20,command=self.seleccionar_regla)
        self.button_select.pack(fill=BOTH,side=BOTTOM)

        #Generacion del listado de reglas
        for regla in list(self.reglas.keys()):
            self.list.insert(END,regla)

    def seleccionar_regla(self):
        """ESTA FUNCION GUARDA LA REGLA QUE SE SELECCIONE
        DE LA LISTA, PARA PODER GENERAR LA VENTANA DE CONFIGURACION
        """
        seleccion = self.list.curselection()

        if seleccion:
            indice = seleccion[0]
            regla_seleccionada = self.list.get(indice)
            #self.config_regla = config_regla(regla_seleccionada,self.window)

            self.config_rule = config_rule(regla_seleccionada,self.window)
        else:
            regla_seleccionada = None
    
    