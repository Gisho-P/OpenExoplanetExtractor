import json
import urllib
import csv

def readExoplanetArchive():
    
    url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    a = json.loads(data)
    print(a)
    
# Needs some fixing reading CSV files
def readExoplaneteu():
    
    url = "http://exoplanet.eu/catalog/csv/"
    response = urllib.request.urlopen(url)
    cr = csv.reader(response)
    for row in cr:
        print(row)

readExoplaneteu()
#readExoplanetArchive()