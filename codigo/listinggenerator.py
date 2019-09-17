#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from jinja2 import Template
import json

with open('aparts.txt', 'r') as json_file:
    aparts = json.load(json_file)

with open('listingtemplate.html') as f:
    tmpl = Template(f.read())

for apart in aparts['aparts']:
	html = tmpl.render(apart)
	falta_planos = ["SanFranciscoPark","Panamar","TorreZeus","PearlAtTheSea",
	"OceanTwo","PacificVillage","StarBay","Bahia","Montemar",
	"Firenze","FairmontPlaza","LomaAlegre","FairwayEstates", "CocoMar"]
	if apart["apartname"] in falta_planos:
		print apart["apartname"]
		f = open("listing"+apart["apartname"]+".html", "w")
		f.write(html)
		f.close()


