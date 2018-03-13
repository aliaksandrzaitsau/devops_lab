"""test_task6"""
# pylint: disable=invalid-name
import unittest
from task6 import MyClass


class TestSequence(unittest.TestCase):
    """Unittest Class"""
    def start(self):
        """Init"""

    def testsample(self):
        """test something"""
        mc = MyClass()
        self.assertTrue(mc.WriteJson() < "3.6.5")

    def finish(self):
        """Finish"""
