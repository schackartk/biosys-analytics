#!/usr/bin/env python3

"""
Author : schackartk
Date   : 2019-04-04
Purpose: Find the unclustered proteins by comparing FASTA file to Blast Hits file
"""

import argparse
import sys
import re
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Unlustered protein detector',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        help='Output file from CH-HIT (clustered proteins)',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-p',
        '--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='file',
        type=str,
        default='unclustered.fa')

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
    hits = args.cdhit
    fasta = args.proteins
    out_file = args.outfile
    clustered_set = set()

    if not os.path.isfile(fasta):
        die('--proteins "{}" is not a file'.format(fasta))
  
    if not os.path.isfile(hits):
        die('--cdhit "{}" is not a file'.format(hits))

    if os.path.isfile(out_file):
        os.remove(out_file)

    clust_reg = re.compile('[|]' +
                           '(?P<prot_id>\d+)' +
                           '[|]')

    for line in open(hits):
        match_clust = clust_reg.search(line)
        if match_clust:
            clustered_set.add(match_clust.group('prot_id'))

    unclustered = 0
    total = 0
    out_fh = open(out_file,mode='a')

    for record in SeqIO.parse(fasta,'fasta'):
        prot_id = re.sub('[|].*','',record.id)
        total += 1
        if prot_id not in clustered_set:
            unclustered += 1
            SeqIO.write(record,out_fh,'fasta')
    
    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(unclustered,total,out_file))


# --------------------------------------------------
if __name__ == '__main__':
    main()
