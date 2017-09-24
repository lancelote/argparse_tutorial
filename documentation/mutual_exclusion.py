"""
>>> parser0.parse_args(['--foo'])
Namespace(bar=True, foo=True)
>>> parser0.parse_args(['--bar'])
Namespace(bar=False, foo=False)
>>> parser0.parse_args('--foo --bar')  # doctest: +SKIP
usage: PROG [-h] [--foo | --bar]
PROG: error: argument --bar: not allowed with argument --foo

>>> parser1.parse_args([])  # doctest: +SKIP
usage: PROG [-h] (--foo | --bar)
PROG: error: one of the arguments --foo --bar is required
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG')
group0 = parser0.add_mutually_exclusive_group()
group0.add_argument('--foo', action='store_true')
group0.add_argument('--bar', action='store_false')

# at least one is required #
############################

parser1 = argparse.ArgumentParser(prog='PROG')
group1 = parser1.add_mutually_exclusive_group(required=True)
group1.add_argument('--foo', action='store_true')
group1.add_argument('--bar', action='store_false')
