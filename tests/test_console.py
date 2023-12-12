#!/usr/bin/python3
"""
console test
"""
import console
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    testing console
    """

    def create(self):
        return HBNBCommand()

    def test_quit(self):
        """
        testing quit method
        """
        cons = self.create()
        self.assertTrue(cons.onecmd("quit"))

    def test_EOF(self):
        """
        testing EOF method
        """
        cons = self.create()
        self.assertTrue(cons.onecmd("EOF"))
