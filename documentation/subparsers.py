"""
>>> parser0.parse_args('a 12'.split())
Namespace(bar=12, foo=False)
>>> parser0.parse_args('--foo b --baz Z'.split())
Namespace(baz='Z', foo=True)

>>> parser0.parse_args(['--help'])  # doctest: +SKIP
usage: PROG [-h] [--foo] {a,b} ...

positional arguments:
  {a,b}   sub-command help
    a     a help
    b     b help

optional arguments:
  -h, --help  show this help message and exit
  --foo   foo help

>>> parser0.parse_args('a --help'.split())  # doctest: +SKIP
usage: PROG a [-h] bar

positional arguments:
  bar     bar help

optional arguments:
  -h, --help  show this help message and exit

>>> parser0.parse_args('b --help'.split())  # doctest: +SKIP
usage: PROG b [-h] [--baz {X,Y,Z}]

optional arguments:
  -h, --help     show this help message and exit
  --baz {X,Y,Z}  baz help

>>> parser1.print_help()
usage: PROG [-h] {foo,bar} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  valid subcommands

  {foo,bar}   additional help

>>> parser2.parse_args('co bar'.split())
Namespace(foo='bar')

>>> args = parser3.parse_args('foo 1 -x 2'.split())
>>> args.func(args)
2.0
>>> args = parser3.parse_args('bar XYZYX'.split())
>>> args.func(args)
((XYZYX))

>>> parser4.parse_args('2 frobble'.split())
Namespace(subparser_name='2', y='frobble')
"""

import argparse

parser0 = argparse.ArgumentParser(prog='PROG')
parser0.add_argument('--foo', action='store_true', help='foo help')
subparsers0 = parser0.add_subparsers(help='sub-command help')

# parser for the "a" command
parser_a = subparsers0.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# parser for the "b" command
parser_b = subparsers0.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

# title and description for sub parser #
########################################

parser1 = argparse.ArgumentParser(prog='PROG')
subparsers1 = parser1.add_subparsers(title='subcommands',
                                     description='valid subcommands',
                                     help='additional help')
subparsers1.add_parser('foo')
subparsers1.add_parser('bar')

# aliases for subparsers #
##########################

parser2 = argparse.ArgumentParser()
subparsers2 = parser2.add_subparsers()
checkout = subparsers2.add_parser('checkout', aliases=['co'])
checkout.add_argument('foo')


# default command for subparser #
#################################


# sub-command functions
def foo(args):
    print(args.x * args.y)


def bar(args):
    print('((%s))' % args.z)


# top level parser
parser3 = argparse.ArgumentParser()
subparsers3 = parser3.add_subparsers()

# parser for the "foo" command
parser_foo = subparsers3.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# parser for the "bar" command
parser_bar = subparsers3.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)

# check subparser name #
########################

parser4 = argparse.ArgumentParser()
subparsers4 = parser4.add_subparsers(dest='subparser_name')
subparser1 = subparsers4.add_parser('1')
subparser1.add_argument('-x')
subparser2 = subparsers4.add_parser('2')
subparser2.add_argument('y')
