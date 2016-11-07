import xmltodict
import urllib
import dicttoxml
import collections
import os
import glob

def readOEC():
    url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/master/systems/Kepler-489.xml"
    data = urllib.request.urlopen(url).read().decode('utf-8')
    result = xmltodict.parse(data, dict_constructor=dict)
    return result


def dicttoXML(data):
    result = dicttoxml.dicttoxml(data, root=False, attr_type=False)
    return result

def csvToDictToXML():
    result = dicttoxml.dicttoxml(exoplanetEUreader.readExoplaneteu()[0], root=False, attr_type=False)
    return result

def searchForNew(system_name):
    # Search the directory for the name
    fileList = os.listdir('./systems')
    # Loop through and get rid of all the file extensions
    path = " "
    for name in fileList:
        if(name[:len(name) -4] == system_name):
            # Return the path of the file
            path = "./systems/" + system_name + ".xml"

    return(path)














#print(readOEC())
#print(dicttoXML(readCatalogue()))
#print(csvToDictToXML())
#print(searchForNew('11 Com'))