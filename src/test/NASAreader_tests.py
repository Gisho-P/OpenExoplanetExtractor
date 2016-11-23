import unittest
import urllib
import sys
sys.path.insert(0, '../system_classes')
sys.path.insert(0, '..')
from system import *
import dicttoxml
import xmltodict
import NASAreader

class TestNASAReader(unittest.TestCase):
    
    def setUp(self):
        self.systems = NASAreader.readNASAExoplanetArchive()
    
    # Checks that there is only one system for a star that has multiple planets
    def test_Single_System(self):
        count = 0
        for sys in self.systems:
            if sys["system"]["name"] == 'CoRoT-24':
                count = count + 1
        self.assertEqual(count, 1)
        
    # Checks that there is multiple planets in the system
    def test_multiPlanet_System(self):
        numPlanets = 0
        for sys in self.systems:
            # 5 planets
            if sys["system"]["name"] == '55 Cnc':
                numPlanets = len(sys["system"]["star"]["planet"])
        self.assertTrue(numPlanets > 1)

    # Checks that there is no empty values for a key
    def test_empty_values(self):
        for sys in self.systems:
            for value in sys["system"]:
                self.assertTrue(sys["system"][value])

if __name__ == '__main__':
    unittest.main(exit=False)
