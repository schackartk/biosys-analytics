#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-04-21
Purpose: Find instrnaces of similar words between files
"""

import argparse
import sys
import os
import re
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find frequency of similar words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'File',
        metavar='FILE',
        nargs='+',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='File input(s)')

    parser.add_argument(
        '-s',
        '--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum count',
        metavar='int',
        type=int,
        default=0)

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
    file_handles = args.File
    sort = args.sort
    min_count = args.min
    words = []
    d = defaultdict(int)

    for handle in file_handles:
        for line in handle:
            for word in line.rstrip().split():
                string = word.lower()   
                words.append(re.sub('[^a-zA-Z0-9]', '', string))

    for word in words:
        d[word] += 1

    if '' in d: del d['']

    if sort == 'word':
        listed = list(d.keys())
        listed.sort()
   
        for item in listed:
            if d[item] >= min_count:
                print('{:20} {}'.format(item,d[item]))
    elif sort == 'frequency':
        pairs = sorted([(x[1], x[0]) for x in d.items()])
        for count, word in pairs:
            if count >= min_count:
                print('{:20} {}'.format(word,str(count)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
