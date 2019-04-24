#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-04-09
Purpose: Find Hamm distances between words in files
"""

import argparse
import sys
import logging
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find Hamm distances between words in files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files',
        metavar='FILE',
        nargs=2,
        help='Files containing strings for analysis')

    parser.add_argument(
        '-d',
        '--debug',
        help='Turn on debugging',
        action='store_true')

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
def dist(s1,s2):
    
    return sum(l1 != l2 for l1,l2 in zip(s1,s2)) + abs(len(s1) - len(s2))

# --------------------------------------------------
def main():
    args = get_args()
    files = args.files
    words = [[],[]]

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )

    for f in files:
        if not os.path.isfile(f):
            die('"{}" is not a file'.format(f))    
  
    logging.debug('file1 = {}, file2 = {}'.format(files[0],files[1]))

    for i, fi in enumerate(files):
        with open(fi) as f:
            words[i] = [word for line in f for word in line.split()]
              
    word_pairs = list(zip(words[0],words[1]))
    
    total =0
    for s1,s2 in word_pairs:
        distance = dist(s1,s2)
        logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2,distance))
        total += distance
    print(total)

# --------------------------------------------------
if __name__ == '__main__':
    main()
