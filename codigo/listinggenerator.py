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
	if apart["apartname"] == "CocoPlaceB": 
		print html


