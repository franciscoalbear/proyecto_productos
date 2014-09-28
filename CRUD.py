#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import *
from datetime import *
from time import *

conexion = Connection()
db = conexion['abarrotes']
coleccion = db['productos']


def registrar(nombre,marca,costo,codigo):

	try:
	    datos = {"Nombre": nombre,"Marca": marca,"Costo": costo,"Codigo": codigo}

	    coleccion.insert(datos)

	except Exception, e:
		print "no se pudo hacer la conexion"

def eliminar(nombre):

	try:
		eliminar = {"Nombre": nombre}
		coleccion.remove(eliminar)

	except Exception, e:
	    print "no se pudo eliminar el elemento"