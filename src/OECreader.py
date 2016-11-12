import xmltodict
import urllib
import dicttoxml
import collections
import os
import glob
import sys
sys.path.insert(0, './system_classes')
from system import *

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

def searchForSys(system_name):
    # Search the directory for the name
    fileList = os.listdir('./systems')
    # Loop through and get rid of all the file extensions
    path = " "
    for name in fileList:
        if(name[:len(name) -4] == system_name):
            # Return the path of the file
            path = "./systems/" + system_name + ".xml"
    # Take the path and read the data in the path
    file = open(path,"r")
    data = file.read()
    # Temporary fix, ****CHECK LATER*****
    data = data[3:]
    sys_dict = xmltodict.parse(data, dict_constructor=dict)
    system = System(sys_dict)
    return(system)














#print(readOEC())
#print(dicttoXML(readCatalogue()))
#print(csvToDictToXML())
searchForSys('11 Com')