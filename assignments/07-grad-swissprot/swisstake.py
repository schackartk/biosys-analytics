#!/usr/bin/env python3

"""
Author : schackartk
Date   : 2019-03-06
Purpose: Grad homework do something with SwissProt files
"""

import argparse
import sys
import os
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'uniprot', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
        '--skip',
        help='Skip taxa',
        metavar='STR',
        type=str,
        nargs='+',
        default='')

    parser.add_argument(
        '-k',
        '--keyword',
        help='Take on keyword',
        metavar='STR',
        type=str,
        default='',
        required=True)
  
    parser.add_argument(
        '-o',
        '--output',
        help='Output file name',
        metavar='FILE',
        type=str,
        default='out.fa')

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
    args = get_args()
    out_file = args.output
    key = args.keyword
    key = key.lower()
    uni = args.uniprot
    skip = args.skip
    skip = skip.lower() if type(skip) == str else [s.lower() for s in skip]

    if not os.path.isfile(uni):
        die('"{}" is not a file'.format(uni))

    out_fh = open(out_file, 'w')

    print('Processing"{}"'.format(uni))
    num_writes = 0
    num_skips = 0
    for record in SeqIO.parse(uni, "swiss"):
        annotations = record.annotations

        if 'keywords' in annotations:
            keys = annotations['keywords']
            keys = [k.lower() for k in keys]
            taxa = annotations['taxonomy']
            taxa = [t.lower() for t in taxa]
            if any(item in key for item in keys) and not any(thing in skip for thing in taxa):
                SeqIO.write(record,out_fh,'fasta')
                num_writes += 1
            else:
                num_skips += 1
    print('Done, skipped {} and took {}. See output in "{}".'.format(num_skips,num_writes,out_file))

# --------------------------------------------------
if __name__ == '__main__':
    main()
