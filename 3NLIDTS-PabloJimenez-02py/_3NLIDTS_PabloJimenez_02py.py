from tkinter import*
import tkinter as sapo # normalmete es ttk en libros

# componentes
ventana = Tk()
ventana.title("Ingreso de nombres")
ventana.geometry("520x480")

boton = sapo.Button(text="Aceptar")
boton.place(x=120,y=140)

entrada = sapo.Entry()
entrada.place(x=120,y=180,width=200)

lbl = sapo.Label(ventana,text = "Agrega tu nombre:")
lbl.place(x=120,y=110)

ventana.mainloop()
