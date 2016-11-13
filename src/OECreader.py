import xmltodict
import urllib
import dicttoxml
import collections
import os
import glob
import sys
sys.path.insert(0, './system_classes')
from system import *


def writeSystem(system_obj):
    ''' Write a system object representation of a system to a xml file in the
    local copy of the oec'''
    system_xml = dicttoxml.dicttoxml(system_obj.toDict(), root=False, attr_type=False)
    path = findSystem(system_obj.mainName)
    file = open(path,"w")
    file.truncate()
    file.write(system_xml + "\n")
    file.close()


def readSystem(system_name):
    ''' Read system xml of oec local copy'''
    path = findSystem(system_name)
    file = open(path,"r")
    data = file.read()
    # Temporary fix, ****CHECK LATER*****
    data = data[3:]
    sys_dict = xmltodict.parse(data, dict_constructor=dict)
    system = System(sys_dict)
    return(system)

def findSystem(system_name):
    ''' Read system xml of oec local copy'''
    # Search the directory for the name
    fileList = os.listdir('./systems')
    # Loop through and get rid of all the file extensions
    path = " "
    for name in fileList:
        if(name[:len(name) -4] == system_name):
            # Return the path of the file
            path = "./systems/" + system_name + ".xml"
    # Take the path and read the data in the path
    return path











#print(readOEC())
#print(dicttoXML(readCatalogue()))
#print(csvToDictToXML())
#searchForSys('11 Com')