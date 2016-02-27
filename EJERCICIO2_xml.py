#!/usr/bin/python
# -*-coding: utf-8 -*-

#2. Contar cuántas facturas están pagadas..

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()
datos=raiz.findall("result")
pagadas=0
estado=""
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		estado=b.find("status").text
		if estado=="Pagada":
			pagadas=pagadas+1
print pagadas," facturas pagadas"
