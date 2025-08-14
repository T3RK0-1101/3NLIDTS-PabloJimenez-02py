from tkinter import*
import tkinter as sapo # normalmete es ttk en libros

ventana = Tk()
ventana.title("Chamoy")
ventana.geometry("520x480")

boton = sapo.Button(text="Aceptar")
boton.place(x=120,y=140)

entrada = sapo.Entry()
entrada.place(x=120,y=180,width=200)

lbl = sapo.Label(ventana,text = "Ingresa tu nombre:")
lbl.place(x=120,y=110)

ventana.mainloop()
