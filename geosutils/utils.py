"""Generic file-based utilities and helpers.

"""
__all__ = ['hashcode']

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
