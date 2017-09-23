"""
>>> parser0.print_help()  # doctest: +ELLIPSIS
usage: PROG [--foo FOO] bar
...
group:
  --foo FOO  foo help
  bar        bar help

>>> parser1.print_help()  # doctest: +ELLIPSIS
usage: PROG [--bar BAR] foo
...
group1:
  group1 description
...
  foo        foo help
...
group2:
  group2 description
...
  --bar BAR  bar help
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG', add_help=False)
group0 = parser0.add_argument_group('group')
group0.add_argument('--foo', help='foo help')
group0.add_argument('bar', help='bar help')

# title and description for group #
###################################

parser1 = argparse.ArgumentParser(prog='PROG', add_help=False)
group1 = parser1.add_argument_group('group1', 'group1 description')
group1.add_argument('foo', help='foo help')
group2 = parser1.add_argument_group('group2', 'group2 description')
group2.add_argument('--bar', help='bar help')
