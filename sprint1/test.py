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
    print(a)

    
# Needs some fixing reading CSV files
def readExoplaneteu():
    
    url = "http://exoplanet.eu/catalog/csv/"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    cat = {}
    data = data.split("\n")
    for line in data:
    	temp = line.split(",")
    	cat[temp[0]] = temp[1:]
    print(cat)
    
def readOEC():
    data = open('test.xml').read()
    result = xmltodict.parse(data, dict_constructor=dict)
    print(result)


def dicttoXML(data):
    result = dicttoxml.dicttoxml(data)
    print(result)




readOEC()