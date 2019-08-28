#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from jinja2 import Template
with open('listingtemplate.html') as f:
    tmpl = Template(f.read())
json = { "aparts":
	[{'apartname' : 'OceanHouse',
	'imagenums' : [1,2,3,4,5,6],
	'location' : 'En mi casa',
	'propertyname' : 'Ocean House - modelo XxX',
	'precio' : '123,123',
	'tamano' : 250,
	'precioporm' : '1,234',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 456,
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 3,
	'mapa' : 'dame un sec',
	'apartamenities' : ["Aqui va 1 amentity", "Aqui iria en teoria otro"],
	'buildingamenities' : ["Aquí va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro"] 
	},
	{'apartname' : 'OceanHouse',
	'imagenums' : [1,2,3,4,5,6],
	'location' : 'En mi casa',
	'propertyname' : 'Ocean House - modelo XxX',
	'precio' : '123,123',
	'tamano' : 250,
	'precioporm' : '1,234',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 456,
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 3,
	'mapa' : 'dame un sec',
	'apartamenities' : ["Aqui va 1 amentity", "Aqui iria en teoria otro"],
	'buildingamenities' : ["Aquí va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro"] 
	},
	{'apartname' : 'OceanHouse',
	'imagenums' : [1,2,3,4,5,6],
	'location' : 'En mi casa',
	'propertyname' : 'Ocean House - modelo XxX',
	'precio' : '123,123',
	'tamano' : 250,
	'precioporm' : '1,234',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 456,
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 3,
	'mapa' : 'dame un sec',
	'apartamenities' : ["Aqui va 1 amentity", "Aqui iria en teoria otro"],
	'buildingamenities' : ["Aquí va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro"] 
	},
	{'apartname' : 'OceanHouse',
	'imagenums' : [1,2,3,4,5,6],
	'location' : 'En mi casa',
	'propertyname' : 'Ocean House - modelo XxX',
	'precio' : '123,123',
	'tamano' : 250,
	'precioporm' : '1,234',
	'cuartos' : 3,
	'banos' : 3.5,
	'mantenimiento' : 456,
	'entrega' : 'YA',
	'ultimocambio' : 0,
	'estacionamientos' : 3,
	'mapa' : 'dame un sec',
	'apartamenities' : ["Aqui va 1 amentity", "Aqui iria en teoria otro"],
	'buildingamenities' : ["Aquí va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro","Aqui va 1 amentity", "Aqui iria en teoria otro"] 
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

