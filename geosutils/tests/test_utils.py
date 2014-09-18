# pylint: disable=R0904,W0142,C0103
""":mod:`geosutils.utils` tests.

"""
import unittest2

from geosutils.utils import hashcode


class TestUtils(unittest2.TestCase):
    """:mod:`geosutils.utils`
    """
    def test_hashcode(self):
        """Hash code generation.
        """
        source = 'b4c937e3ca5c78d1f7a3fc47dc727e78'
        received = hashcode(source)
        expected = 1182110976
        msg = 'Hash code generation error'
        self.assertEqual(received, expected, msg)
