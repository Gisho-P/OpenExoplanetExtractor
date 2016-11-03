#import xml.etree.ElementTree
import unittest
#import sys
#sys.path.insert(0, 'f:/work/team01-Project/src/System_Classes/System.py')
#import System
#import System_Classes.System from 'f:\\Work\\team01-Project\\src\\System_Classes'
from src.System_Classes import System
#from System_classes import *

class TestContained(unittest.TestCase):

    def test_hold_data(self):
        url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/ope"
        + "n_exoplanet_catalogue/master/systems/CoRoT-24.xml"
        data = urllib.request.urlopen(url).read().decode('utf-8')
        result = xmltodict.parse(data, dict_constructor=dict)
        system = System(result)
        result = system.declination
        expected = "-03 43 10"
        self.assertEqual(result, expected)
