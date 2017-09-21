"""
>>> parser0.parse_args('-x X'.split())
Namespace(foo=None, x='X')
>>> parser0.parse_args('--foo FOO'.split())
Namespace(foo='FOO', x=None)
>>> parser0.parse_args(['--foo=FOO'])
Namespace(foo='FOO', x=None)
>>> parser0.parse_args(['-xX'])
Namespace(foo=None, x='X')

>>> parser1.parse_args(['-xyzZ'])
Namespace(x=True, y=True, z='Z')
"""

import argparse

# passing value as separate argument #
######################################

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('-x')
parser0.add_argument('--foo')

# combining flags #
###################

parser1 = argparse.ArgumentParser(prog='PROG')
parser1.add_argument('-x', action='store_true')
parser1.add_argument('-y', action='store_true')
parser1.add_argument('-z')
