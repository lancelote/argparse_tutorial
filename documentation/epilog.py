"""
>>> parser.print_help()  # doctest: +ELLIPSIS
usage: epilog [-h]
...
And that's how you'd foo a bar
"""


import argparse

parser = argparse.ArgumentParser(
    prog='epilog',
    description='A foo that bars',
    epilog='And that\'s how you\'d foo a bar'
)
