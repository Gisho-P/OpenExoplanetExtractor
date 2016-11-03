import unittest
import urllib
import sys
sys.path.insert(0, '../system_classes')
sys.path.insert(0, '..')
from system import *
import dicttoxml
import xmltodict

class TestContained(unittest.TestCase):

    def test_hold_data(self):
        file = open('CoRoT-24.xml', 'r')
        data = file.read()
        file.close()
        system_dict = xmltodict.parse(data, dict_constructor=dict)
        system = System(system_dict)
        result = system.declination
        expected = "-03 43 10"
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
