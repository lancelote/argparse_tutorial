"""
>>> args = parser.parse_args('--foo BAR'.split())
>>> vars(args)
{'foo': 'BAR'}

>>> c = C()
>>> args = parser.parse_args('--foo BAR'.split(), namespace=c)
>>> c.foo
'BAR'
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')


class C:
    foo: str
