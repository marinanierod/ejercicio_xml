#!/usr/bin/python
# -*-coding: utf-8 -*-

#5. Introducir fecha para mostrar el título de la factura.

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()
fecha=raw_input("Introduce la fecha de la factura con este formato YYYY-MM-DD: ")
datos=raiz.findall("result")
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		fechas=b.findall("issued")
		if b.find("issued").text.startswith(fecha):
			print b.find("title").text
