#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-03-26
Purpose: HW use regular expressions to interpret and reformat dates
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Date reformatter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'date',
        metavar='STR',
        help='A date in some random format')

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
    raw_date = args.date
    raw_date.lower()
    
    month_val = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }

    date_re1 = re.compile('(?P<year>\d{4})'
                         '[/-]?'
                         '(?P<month>\d{1,2})'
                         '[/-]?'
                         '(?P<day>\d{,2})?'
                         '($|\D)')
    
    date_re2 = re.compile('(?P<month>\d{,2})'
                          '[/-]'
                          '(?P<year>\d{2})')
    
    date_re3 = re.compile('(?P<month>[A-Za-z]+)'
                         '[ ,-]+'
                         '(?P<year>\d{4})')
    
    match1 = date_re1.match(raw_date)
    match2 = date_re2.match(raw_date)
    match3 = date_re3.match(raw_date)
     
    if match1:
        year = match1.group('year')
        month = match1.group('month')
        day = match1.group('day') if match1.group('day') else '01'
        if len(year) < 4:
            year = '20' + year
        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
    elif match2:
        year = '20' + match2.group('year')
        month = match2.group('month')
        if len(month) < 2:
            month = '0' + month
        day = '01'
    elif match3:
        year = match3.group('year')
        month_str = match3.group('month')
        month = month_val[str.lower(month_str[0:3])]
        day = '01'
    else:
        die('No match')

    print('{}-{}-{}'.format(year,month,day))
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
