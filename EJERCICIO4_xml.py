#!/usr/bin/python
# -*-coding: utf-8 -*-

#4. Mostrar título de la estructura organizativa que empiecen por una cadena introducida por teclado.

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()

lista=[]
lista2=[]
cadena=raw_input("Introduce una cadena: ")
datos=raiz.findall("result")
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		entidades=b.findall("entidad")
		for c in entidades:
			estructuras=c.findall("estructura-organizativa")
			for t in estructuras:					
				if t.find("title").text.startswith(cadena):
					lista.append(t.find("title").text)
for i in lista:
	if i not in lista2:
		lista2.append(i)
for l in lista2:
	print l

