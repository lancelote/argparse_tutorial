"""
>>> parser0.parse_args('--raw raw.dat file.txt')  # doctest: +SKIP
Namespace(out=<_io.TextIOWrapper name='file.txt' mode='w' encoding='UTF-8'>,
          raw=<_io.FileIO name='raw.dat' mode='wb'>)

>>> parser1.parse_args(['-'])  # doctest: +SKIP
Namespace(infile=<_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>)
"""

import argparse

parser0 = argparse.ArgumentParser()
parser0.add_argument('--raw', type=argparse.FileType('wb', 0))
parser0.add_argument('out', type=argparse.FileType('w', encoding='UTF-8'))

# stdin and stdout #
####################

parser1 = argparse.ArgumentParser()
parser1.add_argument('infile', type=argparse.FileType('r'))
