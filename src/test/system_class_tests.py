import unittest
import urllib
import dicttoxml
import xmltodict
import sys
sys.path.insert(0, '../system_classes')
import system

class TestContained(unittest.TestCase):

    def test_hold_data(self):
        data = open('CoRoT-24.xml', 'r').read()
        result = xmltodict.parse(data, dict_constructor=dict)
        system = System(result)
        result = system.declination
        expected = "-03 43 10"
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
