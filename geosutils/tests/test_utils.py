# pylint: disable=R0904,W0142,C0103
""":mod:`geosutils.utils` tests.

"""
import unittest2

from geosutils.utils import (hashcode,
                             get_reverse_timestamp)


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

    def test_get_reverse_timestamp(self):
        """Generate reverse timestamp.
        """
        received = get_reverse_timestamp('19961217102630')
        expected = '09222521218464775807'
        msg = 'Reverse timestamp error'
        self.assertEqual(received, expected, msg)

        newer = get_reverse_timestamp('19971217102630')
        msg = 'Reverse timestamp of newer date should be less'
        self.assertLess(int(newer), int(received), msg)

    def test_get_reverse_timestamp_current_time(self):
        """Generate reverse timestamp: current time.
        """
        received = get_reverse_timestamp()
        msg = 'Reverse timestamp (current time) error'
        self.assertIsNotNone(received, msg)

    def test_get_reverse_timestamp_invalid_source_utc_length(self):
        """Generate reverse timestamp: invalid source UTC length.
        """
        received = get_reverse_timestamp('199612171026')
        msg = 'Reverse timestamp error: invalid UTC length'
        self.assertIsNone(received, msg)

    def test_get_reverse_timestamp_invalid_source_unknown_delimeter(self):
        """Generate reverse timestamp: invalid source (unknown delimiter).
        """
        received = get_reverse_timestamp('1996121710--')
        msg = 'Reverse timestamp error: invalid source (unknown delim)'
        self.assertIsNone(received, msg)
