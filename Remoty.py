import requests
import re
from bs4 import BeautifulSoup
import sys

header = {'user-agent: "Mozilla/5.0 (X11; Linux 1686; rv:43.0) Gecko/10100101 Firefox/43.0 Iceweasel/43.0.4'}                        

site = sys.arg[1]
req = requests.get(site, data=header)
html = req.text

bs = BeautifulSoup(html, 'lxml')

exp = re.findall(r'[\w.]+[\w-]+[\w_]@[]+[\w.]+[(yahoo.)?]+[(gmail.)?]', html) #r = raw  string
v = bs.img['src']

for email in exp:
	print('Email > '+str(email))

	print('External Links: ' + str(v))
	