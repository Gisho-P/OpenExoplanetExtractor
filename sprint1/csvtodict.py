import xmltodict
import json
import urllib.request
import csv
import dicttoxml
import collections

def readExoplaneteu():

    url = "http://exoplanet.eu/catalog/csv/"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    cat = {}
    data = data.split("\n")
    for line in data:
        temp = line.split(",")
        cat[temp[0]] = temp[1:]
    print(cat)

readExoplaneteu()