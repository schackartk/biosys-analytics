#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-22
Purpose: Pull the first line of each poem within a directory
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Get the first lines',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', nargs='+', help='A positional argument')

    parser.add_argument(
        '-w',
        '--width',
        type=int,
        metavar='int',
        help='Output line width',
        default=50)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    dirs = args.positional
    width = args.width

    out = {}
    for dir_n in dirs:
        if not os.path.isdir(dir_n):
            print('"{}" is not a directory'.format(dir_n), file=sys.stderr)
        else:
            print(dir_n)
            files = os.listdir(dir_n)
            for file_n in files:
                with open('{}/{}'.format(dir_n,file_n)) as f:
                    out[f.readline().strip()] = file_n    
            for items in sorted (out):
                num_dots = width - len(items) - len(out[items])
                dots = '.' * num_dots
                print('{} {} {}'.format(items,dots,out[items]))
            out.clear()

# --------------------------------------------------
if __name__ == '__main__':
    main()
