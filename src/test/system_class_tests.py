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

    def test_hold_data(self):
        system = System(self.system_dict)
        result = system.declination
        expected = "-03 43 10"
        self.assertEqual(result, expected)

    def test_holds_different_planet_data(self):
        system = System(self.system_dict)
        result = system.stars.planets[0].mass_upper_limit == '0.018'
        result = result and system.stars.planets[1].mass_upper_limit == ''
        result = result and system.stars.planets[0].mass_error_minus == ''
        result = result and system.stars.planets[1].mass_error_minus == '0.035'
        self.assertTrue(result)

    def test_basic_update(self):
        system_A = System(self.system_dict)
        system_B = System(self.system_dict)
        # system_B.stars.age = '12'
        result = system_A.update(system_B)
        expected = []
        # expected = [['CoRoT-24', ['CoRoT-24',
        #                          '2MASS 06474141-0343094'], 'age']]
        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
