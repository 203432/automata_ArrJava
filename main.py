import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import archivo as automata


class Aplicacion(tk.Tk):

    def __init__(self):
        super().__init__()

        self.inicializar_gui()
    
    def inicializar_gui(self):
        self.title('Selector archivos y carpetas')
        self.geometry('500x500')

        text = tk.Label(self, text="Bienvenido al automata de arreglos de java")
        text.pack(padx=60,pady=30)

        btn_seleccionar_archivo = tk.Button(self, text='Seleccionar archivo...')
        btn_seleccionar_archivo['command'] = self.seleccionar_archivo
        

        btn_seleccionar_archivo.pack(padx=60, pady=50)
    
    def seleccionar_archivo(self):
        tipos = (('Todos los archivos', '*'),('Texto plano', '*.txt'), ('Imágenes', '*.jpg *.png *.gif'))

        archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/', filetypes=tipos)

        if archivo:
            automata.readFile(archivo)
            
            
def main():
    app = Aplicacion()
    app.mainloop()


if __name__ == '__main__':
    main()