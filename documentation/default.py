"""
>>> parser0.parse_args('--foo 2'.split())
Namespace(foo='2')
>>> parser0.parse_args([])
Namespace(foo=42)

>>> parser1.parse_args([])
Namespace(length=10, width=10.5)

>>> parser2.parse_args(['a'])
Namespace(foo='a')
>>> parser2.parse_args([])
Namespace(foo=42)

>>> parser3.parse_args([])
Namespace()
>>> parser3.parse_args('--foo 1'.split())
Namespace(foo='1')
"""

import argparse

# simple example #
##################

parser0 = argparse.ArgumentParser()
parser0.add_argument('--foo', default=42)

# type is applied to default if it's str #
##########################################

parser1 = argparse.ArgumentParser()
parser1.add_argument('--length', default='10', type=int)
parser1.add_argument('--width', default=10.5, type=int)

# default is used when there're no arguments #
##############################################

parser2 = argparse.ArgumentParser()
parser2.add_argument('foo', nargs='?', default=42)

# prevent adding None if no argument #
######################################

parser3 = argparse.ArgumentParser()
parser3.add_argument('--foo', default=argparse.SUPPRESS)
