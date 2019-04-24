#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-04-12
Purpose: String some sequences togeth
"""

import argparse
import sys
from Bio import SeqIO
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Program to help join sequences together',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='file', help='FASTA file')

    parser.add_argument(
        '-k',
        '--overlap',
        help='Required overlap between two sequences',
        metavar='int',
        type=int,
        default=3)


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
def find_kmers(seq,k):
    n = len(seq) -k + 1
    out = []

    for j in range(0, n, 1):
        out.append(str(seq[j:j+k]))
    
    return(out)

# --------------------------------------------------
def main():
    args = get_args()
    fi = args.fasta
    k = args.overlap
    mers = {}

    if k < 2:
        die('-k "{}" must be a positive integer'.format(k))

    if not os.path.isfile(fi):
        die('"{}" is not a file'.format(fi))

    for record in SeqIO.parse(fi,'fasta'):
        kmers = find_kmers(record.seq,k)
        mers[record.id] = (kmers[0],kmers[-1])

    for mer in mers:
        _,end = mers[mer]
        for mur in mers:
            begin,_ = mers[mur]
            if end == begin and mur != mer:
                print('{} {}'.format(mer,mur))   

    

# --------------------------------------------------
if __name__ == '__main__':
    main()
