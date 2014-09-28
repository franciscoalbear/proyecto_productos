#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import CRUD

def ventana_principal():
	root = Tk()

	root.title("Abarrotes")
	root.geometry("400x400")

	frame = Frame(root)
	frame.pack(padx = 30,pady = 30)

	label = Label(frame, text="Tienda de Abarrotes",fg = "blue",font=("Arial",18))
	label.pack(padx = 10,pady = 20)

	b1 = Button(frame,text="Agregar un artículo",command=ventana_agregar)
	b1.pack(padx = 10,pady = 10)

	b2 = Button(frame,text="Buscar una artículo")
	b2.pack(padx = 10,pady = 10)

	b3 = Button(frame,text="Eliminar un artículo",command=ventana_eliminar)
	b3.pack(padx = 10,pady = 10)

	b4 = Button(frame,text="Actualizar un artículo")
	b4.pack(padx = 10,pady = 10)

	b5 = Button(frame,text="Acerca de")
	b5.pack(padx = 10,pady = 10)

	b6 = Button(frame,text="Salir",command=root.destroy)
	b6.pack(padx = 10,pady = 10)

	root.mainloop()

def display_eliminarnombre():
	dn = Tk()
	dn.title("Eliminar por nombre")
	dn.geometry("300x100")
	label = Label(dn,text="Escriba el nombre del producto a eliminar").pack()
	enom = Entry(dn,textvariable = 1)
	enom.pack()
	bn = Button(dn,text="Eliminar",command=lambda:CRUD.eliminar(Entry.get(enom)))
	bn.pack()
	dn.mainloop()
def display_eliminarcodigo():
	dn = Tk()
	dn.title("Eliminar por codigo")
	dn.geometry("300x100")
	label = Label(dn,text="Escriba el código del producto a eliminar").pack()
	ecodigo = Entry(dn).pack()
	bc = Button(dn,text="Eliminar")
	bc.pack()
	dn.mainloop()
def display_eliminarid():
	dn = Tk()
	dn.title("Eliminar por id")
	dn.geometry("300x100")
	label = Label(dn,text="Escriba el id del producto a eliminar").pack()
	eid = Entry(dn).pack()
	bi = Button(dn,text="Eliminar")
	bi.pack()
	dn.mainloop()

def display_message():
	m = Tk()
	m.geometry("90x200")
	label = Label(m,text="Se ha realizado la operación con éxito")
	m.mainloop()

def ventana_agregar():
	v2 = Tk()
	v2.title("Agregar productos")
	v2.geometry("400x400")
	v2.focus_set()
	v2.grab_set()
	#v2.transient(master=root)

	f = Frame(v2)
	f.pack()

	label = Label(v2, text="Agregar productos",fg = "blue",font=("Arial",18))
	label.pack(padx = 10,pady = 20)

	lnombre = Label(v2,text="Nombre:").pack()

	enombre = Entry(v2,textvariable = 1)
	enombre.pack()

	lmarca = Label(v2,text="Marca:").pack()

	emarca = Entry(v2,textvariable = 2)
	emarca.pack()

	lcosto = Label(v2,text="Costo:").pack()

	ecosto = Entry(v2,textvariable = 3)
	ecosto.pack()

	lcodigo = Label(v2,text="Código:").pack()

	ecodigo = Entry(v2,textvariable = 4)
	ecodigo.pack()

	b1v2 = Button(v2,text="Agregar",command=lambda:CRUD.registrar(Entry.get(enombre),Entry.get(emarca),Entry.get(ecosto),Entry.get(ecodigo)) or display_message)
	b1v2.pack(padx=30,pady=0)

	b2v2 = Button(v2,text="Atrás",command=v2.destroy).pack(padx=30,pady=0)

	v2.mainloop()
def ventana_eliminar():
	v3 = Tk()
	v3.title("Eliminar productos")
	v3.geometry("400x400")
	v3.focus_set()
	v3.grab_set()

	f = Frame(v3).pack()

	label = Label(v3,text="Eliminar producto",fg="blue",font=("Arial",18)).pack(padx = 10,pady = 20)

	b1 = Button(v3,text="Por nombre",command=display_eliminarnombre)
	b1.pack(padx=10,pady=20)
	b2 = Button(v3,text="Por Código",command=display_eliminarcodigo)
	b2.pack(padx=10,pady=20)
	b3 = Button(v3,text="Por id",command=display_eliminarid)
	b3.pack(padx=10,pady=20)

	v3.mainloop()

ventana_principal()