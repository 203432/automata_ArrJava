from email import message
from tkinter import Tk
import tkinter.messagebox as mb
import tkinter as tk
import arregloAutomata as au
import main as inter

validos = []
def validarCadena(cadena):
    if au.dfa.accepts_input(cadena):
        validos.append(cadena)

def readFile(filename):
    with open(filename) as f_obj:
        for line in f_obj:
            validarCadena(line.rstrip())
        abrirVentana()

def abrirVentana():
    win = tk.Toplevel()
    win.geometry('500x500')
    text1 = tk.Label(win,text="Los arreglos encontrados son:")
    text1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    for arr in validos:
        tk.Label(win,text=arr).pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
