#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-26
Purpose: Get GC content from FASTA files
"""

import argparse
import sys
import os
from Bio import SeqIO
import collections

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Segregate FASTA sequences by GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta_file',
        metavar='FASTA',
        nargs='+',
        help='FASTA file for analysis')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
        '--pct_gc',
        help='High vs Low GC threshold',
        metavar='int',
        type=int,
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
    args = get_args()
    pct_thr = args.pct_gc
    out_dir = args.outdir
    fastas = args.fasta_file
    num_writes = 0

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)

    if not 0<=pct_thr<=100:
        die('--pct_gc "{}" must be between 0 and 100'.format(pct_thr))
    
    for i, file in enumerate(fastas,1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue
        print('{}: {}'.format(i,file))
        basename, ext = os.path.splitext(os.path.basename(file))
        low_out = os.path.join(out_dir,basename+'_low'+ext)
        high_out = os.path.join(out_dir, basename+'_high'+ext)
        low_out_fh = open(low_out, 'wt')
        high_out_fh = open(high_out, 'wt')
        for record in SeqIO.parse(file, 'fasta'):
            seq_len = len(record.seq)
            nucs = collections.Counter(record.seq)
            gc = nucs.get('G', 0) + nucs.get('C', 0)
            gc_content = gc/seq_len * 100
            if gc_content < pct_thr:
                go_to = low_out_fh
            else:
                go_to = high_out_fh
            SeqIO.write(record,go_to,'fasta')
            num_writes += 1
    print('Done, wrote {} sequences to out dir "{}"'.format(num_writes,out_dir))
 
# --------3------------------------------------------
if __name__ == '__main__':
    main()
