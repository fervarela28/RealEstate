#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from jinja2 import Template
with open('listingtemplate.html') as f:
    tmpl = Template(f.read())
json = { "aparts":
	[{'apartname' : 'Asia',
	'imagenums' : [1,2,3,4,5,6,7,8,9,10],
	'location' : 'Costa del Este',
	'propertyname' : 'Asia - modelo A',
	'precio' : '398,000',
	'tamano' : 155,
	'precioporm' : '2,568',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 'PENDIENTE',
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 'PENDIENTE',
	'mapa' : 'PENDIENTE',
	'apartamenities' : ["Balcón", "Vista a la ciudad"],
	'buildingamenities' : ["4 ascensores", "Piscina + jacuzzi","Área de niños", "Cancha de squash","Coworking space", "Gimnasio","Canchas de deportes de Costa del Mar"] 
	}, 
	{'apartname' : 'AsiaC',
	'imagenums' : [1,2,3,4,5,6,7,8,9,10],
	'location' : 'Costa del Este',
	'propertyname' : 'Asia - modelo C',
	'precio' : '385,000',
	'tamano' : 155,
	'precioporm' : '2,484',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 'PENDIENTE',
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 'PENDIENTE',
	'mapa' : 'PENDIENTE',
	'apartamenities' : ["Balcón", "Vista al parque"],
	'buildingamenities' : ["4 ascensores", "Piscina + jacuzzi","Área de niños", "Cancha de squash","Coworking space", "Gimnasio","Canchas de deportes de Costa del Mar"] 
	}
	]
}
for apart in json['aparts']:
	print tmpl.render(apart)
# print tmpl.render(
#     apartname = 'OceanHouse',
# 	imagenums = [1,2,3,4,5,6],
# 	location = 'En mi casa',
# 	propertyname = 'Ocean House - modelo XxX',
# 	precio = '123,123',
# 	tamano = 250,
# 	precioporm = '1,234',
# 	cuartos = 3,
# 	banos = 3.5,
# 	mantenimiento = 456,
# 	entrega = 'YA',
# 	ultimocambio = 0,
# 	estacionamientos = 3,
# 	mapa = 'dame un sec',
# 	apartamenities = ["Aqui va 1 amentity", "Aqui iria en teoria otro"],
# 	buildingamenities= ["Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro"] 
# )

