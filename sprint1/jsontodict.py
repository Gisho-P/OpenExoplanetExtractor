import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections


def readNASAExoplanetArchive():
    
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    a = json.loads(data)
    
    # Formatted Dictionary
    catalog = {}
    # Loop through all exoplanets
    for planet in range(0, len(a) - 1):
	# Planet name is the key
        planet_name = a[planet]["pl_hostname"]
        del a[planet]["pl_hostname"]
        catalog.update({planet_name: a[planet]})
	
    print(catalog)