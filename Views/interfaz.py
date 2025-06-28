from tkinter import *
import tkinter as tk
import threading as th
#from mariadb

class Interfaz():
    def __init__(self):
        
        self.ventana = tk.Tk()
        self.ventana.title("El Eco del Último Día")
        self.ventana.config(width = 1024 ,height = 576)
        self.ventana.resizable(0, 0)
        self.ventana.mainloop()