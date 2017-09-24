"""
>>> parser0.parse_args(['736'])
Namespace(bar=42, baz='badger', foo=736)

>>> parser1.parse_args([])
Namespace(foo='spam')

>>> parser2.get_default('foo')
'badger'
"""

import argparse

parser0 = argparse.ArgumentParser()
parser0.add_argument('foo', type=int)
parser0.set_defaults(bar=42, baz='badger')

# parser defaults overrides args default #
##########################################

parser1 = argparse.ArgumentParser()
parser1.add_argument('--foo', default='bar')
parser1.set_defaults(foo='spam')

# get arg default value #
#########################

parser2 = argparse.ArgumentParser()
parser2.add_argument('--foo', default='badger')
