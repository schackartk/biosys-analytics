#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-04-25
Purpose: Find the number of similar words between documents
"""

import argparse
import sys
import os
import logging
import re
import itertools
from tabulate import tabulate
import io

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find similar words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'files',
        metavar='FILE',
        nargs=2,
        type=argparse.FileType('r', encoding='UTF-8'),
        help='Input files')

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)
    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        default='.log')

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true')
   
    parser.add_argument(
        '-t',
        '--table',
        help='Table output',
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
def dist(pair):
    s1, s2 = pair
    d = abs(len(s1) - len(s2)) + sum(map(lambda p: 0 if p[0] == p[1] else 1, zip(s1, s2)))
    
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, d))

    return d
# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3), ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC', 9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(tuple([s1, s2]))
        assert d == n
# --------------------------------------------------
def uniq_words(file, min_len):
    """Find unique words in a file"""
    
    all_words = list(map(lambda s: re.sub('[^a-z0-9]', '', s.lower()), file.read().split()))

    long_words = list(map(lambda w: w if len(w) >= min_len else '', all_words))

    words = set(filter(lambda x: x != '',long_words))
    
    logging.debug('{}'.format(words))

    return words
# --------------------------------------------------
def test_uniq_words():
    """Test uniqu_words"""

    s1 = '?foo, "bar", Foo: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])
    
    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    min_ham = args.hamming_distance
    out_name = args.logfile

    logging.basicConfig(
        filename=out_name,
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL
    )
    
    if min_ham < 0:
        die('--distance "{}" must be > 0'.format(min_ham))
    
    all_words = {}
    words = {}
    for i, fh in enumerate(args.files):
        words[i] = uniq_words(fh, args.min_len)    

    comm = []
    for combo in itertools.product(words[0],words[1]):
        hamm = dist(combo)
        if hamm <= min_ham:
                comm.append(list([combo[0],combo[1],hamm]))

    comm.sort()    
    if comm:
        if args.table:
             print(tabulate(comm,headers=["word1","word2", "distance"],tablefmt="psql"))
        else:
             print('{}\t{}\t{}'.format('word1','word2','distance'))
             for lists in comm:
                 print('{}\t{}\t{}'.format(lists[0],lists[1],lists[2]))
    else:
        print('No words in common.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
