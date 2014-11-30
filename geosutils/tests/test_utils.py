# pylint: disable=R0904,W0142,C0103
""":mod:`geosutils.utils` tests.

"""
import unittest2

from geosutils.utils import (hashcode,
                             get_reverse_timestamp,
                             geodesic_points)


class TestUtils(unittest2.TestCase):
    """:mod:`geosutils.utils`
    """
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None

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

    def test_get_reverse_timestamp_invalid_format(self):
        """Generate reverse timestamp: invalid format).
        """
        received = get_reverse_timestamp('19961211ZOCT11')
        msg = 'Reverse timestamp error: invalid format'
        self.assertIsNone(received, msg)

    def test_geodesic_points(self):
        """Get a list of equidistan points along geodesic.
        """
        melbourne_point = (-37.8136, 144.9631)
        canberra_point = (-35.3075, 149.1244)
        precision = 30000
        received = geodesic_points(melbourne_point,
                                   canberra_point,
                                   precision)
        expected = [(-37.813600000000001, 144.9631),
                    (-37.651180475092076, 145.24900472421263),
                    (-37.488066561147427, 145.53366416727224),
                    (-37.324265238324998, 145.8170858217176),
                    (-37.159783433818511, 146.09927724163992),
                    (-36.994628021840498, 146.38024603940255),
                    (-36.828805823626439, 146.65999988243817),
                    (-36.662323607457836, 146.93854649012337),
                    (-36.495188088704282, 147.21589363072945),
                    (-36.327405929883099, 147.49204911844899),
                    (-36.158983740736559, 147.76702081049712),
                    (-35.989928078325697, 148.04081660428702),
                    (-35.820245447140181, 148.31344443467856),
                    (-35.649942299223774, 148.58491227129917),
                    (-35.479025034314645, 148.85522811593623),
                    (-35.307500000000005, 149.12440000000001)]
        msg = 'Geodesic point error'
        self.assertListEqual(received, expected, msg)
