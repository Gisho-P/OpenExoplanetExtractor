import unittest
import urllib
import sys
sys.path.insert(0, '../system_classes')
sys.path.insert(0, '..')
from system import *
import dicttoxml
import xmltodict

class TestContained(unittest.TestCase):

    def setUp(self):
        file = open('CoRoT-24.xml', 'r')
        data = file.read()
        file.close()
        self.system_dict = xmltodict.parse(data, dict_constructor=dict)
        self.other_dict = xmltodict.parse(data, dict_constructor=dict)

    def test_hold_data(self):
        system = System(self.system_dict)
        result = self.system_dict['system']['declination']
        expected = "-03 43 10"
        self.assertEqual(result, expected)

    def test_holds_different_planet_data(self):
        system = System(self.system_dict)
        result = self.system_dict['system']['star']['planet'][0]['mass'][
            '@upperlimit'] == '0.018'
        result = result and self.system_dict['system']['star']['planet'][1][
            'mass']['@errorminus'] == '0.035'
        self.assertTrue(result)

    def test_basic_update(self):
        system_A = System(self.system_dict)
        system_B = System(self.system_dict)
        result = system_A.update(system_B)
        expected = []
        self.assertEquals(result, expected)

    def test_one_update(self):
        system_A = System(self.system_dict)
        system_B = System(self.other_dict)
        system_B.system_dict['system']['star']['age'] = '12'
        result = system_A.update(system_B)
        expected = [['CoRoT-24', ['CoRoT-24',
                                  '2MASS 06474141-0343094'], 'age']]
        self.assertEqual(result, expected)

    def test_if_updated_one(self):
        system_A = System(self.system_dict)
        system_B = System(self.other_dict)
        system_B.system_dict['system']['star']['age'] = '12'
        system_A.update(system_B)
        result = system_A.system_dict['system']['star']['age']
        expected = '12'
        self.assertEqual(result, expected)

    def test_if_original_changed(self):
        system_A = System(self.system_dict)
        system_B = System(self.other_dict)
        system_A.system_dict['system']['star']['age'] = '12'
        system_A.update(system_B)
        result = system_A.system_dict['system']['star']['age']
        expected = '11'
        self.assertEqual(result, expected)        

    def test_two_update(self):
        system_A = System(self.system_dict)
        system_B = System(self.other_dict)
        system_B.system_dict['system']['distance']['#text'] = '534'
        system_B.system_dict['system']['star']['mass']['#text'] = '0.91'
        result = system_A.update(system_B)
        expected = [['CoRoT-24', 'distance'], ['CoRoT-24', ['CoRoT-24',
                                  '2MASS 06474141-0343094'], 'mass']]
        self.assertEqual(result, expected)

    def test_if_update_two(self):
        system_A = System(self.system_dict)
        system_B = System(self.other_dict)
        system_B.system_dict['system']['distance']['#text'] = '534'
        system_B.system_dict['system']['star']['mass']['#text'] = '0.91'
        system_A.update(system_B)
        result = system_A.system_dict['system']['distance']['#text'] == '534'
        result = result and system_B.system_dict['system']['star']['mass'][
            '#text'] == '0.91'
        expected = True
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
