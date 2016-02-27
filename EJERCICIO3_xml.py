#!/usr/bin/python
# -*-coding: utf-8 -*-

#3. Pedir por teclado un precio máximo y un mínimo para mostrar los identificadores de las facturas y sus títulos que se encuentre entre estos valores.

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()

preciomax=float(raw_input("Introduce el precio máximo: "))
preciomin=float(raw_input("Introduce el precio minimo: "))
datos=raiz.findall("result")
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		precio=float(b.find("amount").text)
		if precio>=preciomin and precio<=preciomax:
 			print b.find("title").text
