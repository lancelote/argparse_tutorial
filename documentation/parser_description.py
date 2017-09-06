"""
>>> parser.print_help()  # doctest: +ELLIPSIS
usage: ... [-h]
...
A foo that bars
...
optional arguments:
  -h, --help  show this help message and exit
"""

import argparse

parser = argparse.ArgumentParser(description='A foo that bars')
