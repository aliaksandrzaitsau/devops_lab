"""test_task6"""
from task6 import *
import unittest


class TestSequence(unittest.TestCase):
    def testsample(self):
        mc = MyClass()
        self.assertFalse(mc.WriteJson())
