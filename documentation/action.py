"""
>>> parser0.parse_args('--foo 1'.split())
Namespace(foo='1')

>>> parser1.parse_args(['--foo'])
Namespace(foo=42)

>>> parser2.parse_args('--foo --bar'.split())
Namespace(bar=False, baz=True, foo=True)

>>> parser3.parse_args('--foo 1 --foo 2'.split())
Namespace(foo=['1', '2'])

>>> parser4.parse_args('--str --int'.split())
Namespace(types=[<class 'str'>, <class 'int'>])

>>> parser5.parse_args(['-vvv'])
Namespace(verbose=3)

>>> parser6.parse_args(['--version'])  # doctest: +SKIP
PROG 2.0

>>> args = parser7.parse_args('1 --foo 2'.split())
Namespace(bar=None, foo=None) '1' None
Namespace(bar='1', foo=None) '2' '--foo'
>>> args
Namespace(bar='1', foo='2')
"""

import argparse

# default action - store value #
################################

parser0 = argparse.ArgumentParser()
parser0.add_argument('--foo', action='store')

# store constant value #
########################

parser1 = argparse.ArgumentParser()
parser1.add_argument('--foo', action='store_const', const=42)

# store boolean value #
#######################

parser2 = argparse.ArgumentParser()
parser2.add_argument('--foo', action='store_true')
parser2.add_argument('--bar', action='store_false')
parser2.add_argument('--baz', action='store_false')

# specify flag multiple times #
###############################

parser3 = argparse.ArgumentParser()
parser3.add_argument('--foo', action='append')

# append constant to one list #
###############################

parser4 = argparse.ArgumentParser()
parser4.add_argument('--str', dest='types', action='append_const', const=str)
parser4.add_argument('--int', dest='types', action='append_const', const=int)

# count number of keywords #
############################

parser5 = argparse.ArgumentParser()
parser5.add_argument('-v', '--verbose', action='count')

# shows version #
#################

parser6 = argparse.ArgumentParser(prog='PROG')
parser6.add_argument('--version', action='version', version='%(prog)s 2.0')

# custom action #
#################


class FooAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(FooAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)


parser7 = argparse.ArgumentParser(prog='PROG')
parser7.add_argument('--foo', action=FooAction)
parser7.add_argument('bar', action=FooAction)
