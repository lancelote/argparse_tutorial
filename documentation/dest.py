"""
>>> parser0.parse_args(['XXX'])
Namespace(bar='XXX')

>>> parser1.parse_args('-f 1 -x 2'.split())
Namespace(foo_bar='1', x='2')
>>> parser1.parse_args('--foo 1 -y 2'.split())
Namespace(foo_bar='1', x='2')

>>> parser2.parse_args('--foo XXX'.split())
Namespace(bar='XXX')
"""

import argparse

# positional argument name #
############################

parser0 = argparse.ArgumentParser()
parser0.add_argument('bar')

# optional argument name #
##########################

parser1 = argparse.ArgumentParser()
parser1.add_argument('-f', '--foo-bar', '--foo')
parser1.add_argument('-x', '-y')

# custom argument name #
########################

parser2 = argparse.ArgumentParser()
parser2.add_argument('--foo', dest='bar')
