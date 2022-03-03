#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """this class gather all test concerning state"""
    def test_name_type(self):
        """test name type from state file"""
        var = State()
        self.assertIsInstance(var.name, str)


if __name__ == '__main__':
    unittest.main()