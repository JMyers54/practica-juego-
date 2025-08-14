from tkinter import *
import tkinter as tk
import threading as th
from Controllers.funciones import Funciones
#from mariadb

class Interfaz():
    def __init__(self):
        
        self.ventanaInicio = tk.Tk()
        self.ventanaInicio.title("El Eco del Último Día")
        self.ventanaInicio.config(width = 1024 ,height = 576, bg="#111111", )
        self.ventanaInicio.resizable(0, 0)

        self.funciones = Funciones()
        self.play = tk.PhotoImage(file=r"practica-juego-/Iconos/Play.png")
        self.ajustes = tk.PhotoImage(file=r"practica-juego-/Iconos/Ajustes.png")
        self.idioma = tk.PhotoImage(file=r"practica-juego-/Iconos/idioma.png")
        self.titulo1 = tk.Label(self.ventanaInicio, text="El Eco del Último Día", font=("Arial",20), bg="#111111",fg="white")
        self.titulo1.place(relx=0.38, rely=0.2)
        
        self.Play = tk.Button(self.ventanaInicio,image=self.play, bg="#111111", bd=0, highlightthickness=0, command=self.funciones.Play)
        self.Play.place(relx=0.36, rely=0.7)

        self.Ajustes = tk.Button(self.ventanaInicio, image=self.ajustes, bg="#111111",bd=0, highlightthickness=0)
        self.Ajustes.place(relx=0.55, rely=0.7)

        self.Idioma = tk.Button(self.ventanaInicio, text="ajustes",image=self.idioma, bg="#111111", bd=0, highlightthickness=0 )
        self.Idioma.place(relx=0.80, rely=0.2,)

        self.ventanaInicio.mainloop()