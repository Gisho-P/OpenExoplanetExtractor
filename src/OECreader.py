import xmltodict
import urllib
import dicttoxml
import collections
import os
import glob
import sys
sys.path.insert(0, './system_classes')
from system import *


def writeSystem(system_name, system_obj):
    ''' Write a system object representation of a system to a xml file in the
    local copy of the oec'''
    system_xml = dicttoxml.dicttoxml(system_obj.getDict(), root=False, attr_type=False)
    path = "./systems/" + system_name + ".xml"
    file = open(path,"w")
    file.truncate()
    file.write(system_xml + "\n")
    file.close()


def readSystem(system_names):
    ''' Read system xml of oec local copy'''
    (name, path) = findSystem(system_names)
    if name is not None:
        file = open(path, "r", encoding='utf-8-sig')
        data = file.read()
        sys_dict = xmltodict.parse(data, dict_constructor=dict)
        system = System(sys_dict)
        return (name, system)
    else:
        return (name, None)


def findSystem(system_names):
    ''' Read system xml of oec local copy'''
    path = None
    # Search the directory for the name
    fileList = os.listdir('./systems')
    print(fileList)
    # search through and try and find a matching file
    for name in system_names:
        if name + ".xml" in fileList:
            # if found return the name that was used and a path to the
            # file
            path = "./systems/" + name + ".xml"
            return (name, path)
    return (None, path)
