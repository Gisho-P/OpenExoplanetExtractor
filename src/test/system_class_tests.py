#import xml.etree.ElementTree
import unittest
import sys
sys.path.insert(0, '../system_classes')
import system
#from ...system_classes import system
#from System_classes import *

class TestContained(unittest.TestCase):

    def test_hold_data(self):
        url = "https://raw.githubusercontent.com/OpenExoplanetCatalogue/ope" \
        "n_exoplanet_catalogue/master/systems/CoRoT-24.xml"
        data = urllib.request.urlopen(url).read().decode('utf-8')
        result = xmltodict.parse(data, dict_constructor=dict)
        system = System(result)
        result = system.declination
        expected = "-03 43 10"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
