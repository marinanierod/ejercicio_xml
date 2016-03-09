#!/usr/bin/python
# -*-coding: utf-8 -*-

from lxml import etree
arbol=etree.parse("facturas.xml")

raiz=arbol.getroot()
datos=raiz.findall("result")

f=open("index.html","w")            

cadena=raw_input("Introduce una subcadena: ")
for a in datos:
	facturas=a.findall("factura")
	for b in facturas:
		entidades=b.findall("entidad")
		for c in entidades:
			estructuras=c.findall("estructura-organizativa")			
			for t in estructuras:					
				if t.find("title").text.find(cadena)!=-1:
					f.write("<h1>"+t.find("id").text+"</h1>"+"\n")
					f.write("<p>"+t.find("title").text+"</p>"+"\n")
					f.write('<a href="'+t.find("uri").text+'"> Más información...</a>'+"\n")
					f.write("\n")
f.close()