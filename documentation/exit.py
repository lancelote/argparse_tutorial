"""
>>> parser.exit(status=1, message='exit with 1')  # doctest: +SKIP
>>> parser.error(message='error')                 # doctest: +SKIP
"""

import argparse

parser = argparse.ArgumentParser()
