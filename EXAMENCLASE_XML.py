#!/usr/bin/python
# -*-coding: utf-8 -*-

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()
datos=raiz.findall("result")


cadena=raw_input("Introduce una cadena")
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		entidades=b.findall("entidad")
		for c in entidades:
			estructuras=c.findall("estructura-organizativa")			
			for t in estructuras:					
				if t.find("title").text.startswith(cadena):
					print "<h1>",t.find("id").text,"</h1>"
					print "<p>",t.find("title").text,"</p>"
					print "<a href=",t.find("uri").text,"Más información...</a>"

