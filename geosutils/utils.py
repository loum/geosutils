"""Generic file-based utilities and helpers.

"""
__all__ = ['hashcode',
           'get_reverse_timestamp']

import sys
import time
import calendar

from geosutils.log import log


def hashcode(source):
    """Will convert the variable length *source* string into a hash code.

    Typcial usage would be to generate a hash value that can be used
    for "binning" objects into hash tables (such as a dictionary).  The
    resultant hash provides a uniform distribution or common *source*
    values.

    Iterates through each character in the *source* string

    **Args**:
        *source*: the string to convert

    **Returns**:
        integer representation

    """
    code = 0
    for char_seq in str(source):
        code = (31 * code + ord(char_seq)) & 0xFFFFFFFF

    log.debug('Hash code for source "%s": %d' % (source, code))

    return ((code + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def get_reverse_timestamp(utc_time=None):
    """Converts a string representation of time denoted by *utc_time*
    into a reverse timestamp.

    Supported *utc_time* construct is ``CCYYMMDDhhmmss``, where:

    * **CC** is the century (00 to 99)
    * **YY** is the last two digits of the year (00 to 99)
    * **MM** is the month (01 to 12)
    * **DD** is the day (01 to 31)
    * **hh** is the hour (00 to 23)
    * **mm** is the minute (00 to 59)
    * **ss** is the second (00 to 59)

    Timezone designator is assumed UTC (Zulu).

    **Args:**
        *utc_time*: string representation of time as per the
        definition within the National Imagery Transmission Format
        Version 2.1.  For example, ``19961217102630``

        .. note::

            The assumption here is a well-formed *utc_time* value
            of 14 digits without the hyphens denoting unknown
            or not expressed values.  Malformed *utc_time*
            will not be converted.

            If *utc_time* is ``None`` then the current time is used.

    **Returns:**
        String of uniform length 20 character representing the
        reverse timestamp of the the given *utc_time* or ``None``
        if the conversion fails

    """
    log.debug('Generating reverse timestamp for UTC string "%s"' %
                utc_time)
    reverse_ts = None
    secs_since_epoch = None

    if utc_time is None:
        secs_since_epoch = time.time()
    elif len(utc_time) == 14 and '-' not in utc_time:
        utc_struct_time = time.strptime(utc_time, '%Y%m%d%H%M%S')
        secs_since_epoch = calendar.timegm(utc_struct_time)
    else:
        log.error('Unsupported UTC time: "%s"' % utc_time)

    if secs_since_epoch is not None:
        reverse_ts = sys.maxint - int(secs_since_epoch * 10 ** 6)
        reverse_ts = str(reverse_ts).zfill(20)

    log.info('Source UTC|Reverse timestring: "%s|%s"' %
                (utc_time, reverse_ts))

    return reverse_ts
