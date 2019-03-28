#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-02-28
Purpose: Blast something or other homework
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'blast', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    blast_file = args.blast
    annotations = args.annotations
    out_file = args.outfile
    ann_dict = {}
    out_dict = {}
    out_dict['seq_id'] = {}
    out_dict['seq_id']['pident'] = 'pident'
    out_dict['seq_id']['genus'] = 'genus'
    out_dict['seq_id']['species'] = 'species'

    for files in [blast_file, annotations]:
        if not os.path.isfile(files):
            die('"{}" is not a file'.format(files))

    with open(annotations) as f:
        for line in f:
            fields = line.split(',')
            ann_dict[fields[0]] = {}
            if not fields[6] == '':
                ann_dict[fields[0]]['genus'] = fields[6]
            else:
                ann_dict[fields[0]]['genus'] = 'NA'
            if not fields[7].strip() == '':
                ann_dict[fields[0]]['species'] = fields[7].strip()
            else:
                ann_dict[fields[0]]['species'] = 'NA' 

    with open(blast_file) as b:
        for lines in b:
            fields = lines.split()
            seq_id = fields[1]
            pident = fields[2] 
            sam_dict = ann_dict.get(seq_id)
            if not sam_dict:
                warn('Cannot find seq "{}" in lookup'.format(seq_id))
                continue
            out_dict[seq_id] = {}
            out_dict[seq_id]['pident'] = pident
            out_dict[seq_id]['genus'] = sam_dict.get('genus')
            out_dict[seq_id]['species'] = sam_dict.get('species')            
    
    if out_file:
        with open(out_file,"w") as o:    
            for items in out_dict:
                print('{}\t{}\t{}\t{}'.format(items,out_dict[items]['pident'],out_dict[items].get('genus'),out_dict[items].get('species')),file=o)
    else:
         for items in out_dict:
                print('{}\t{}\t{}\t{}'.format(items,out_dict[items]['pident'],out_dict[items].get('genus','NA'),out_dict[items].get('species','NA')))

# --------------------------------------------------
if __name__ == '__main__':
    main()
