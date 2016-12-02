import unittest
import urllib
import sys
sys.path.insert(0, '../system_classes')
sys.path.insert(0, '..')
from system import *
from Conflict import *

class TestConflict(unittest.TestCase):

    def test_same_conflict(self):
        self.assertTrue(not Conflict.isConflicting("Planet A changed to Planet B", "Planet A changed to Planet B"))


    def test_different_conflict(self):
        self.assertTrue(Conflict.isConflicting("Planet A changed to Planet B", "Planet A changed to Planet C"))


if __name__ == '__main__':
    unittest.main(exit=False)
