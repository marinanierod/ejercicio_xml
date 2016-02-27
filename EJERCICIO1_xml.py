#!/usr/bin/python
# -*-coding: utf-8 -*-

#1. Listar todos títulos de las facturas.

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()
datos=raiz.findall("result")
for t in datos:
	facturas=t.findall("factura/title")
	for x in facturas:
		print x.text
