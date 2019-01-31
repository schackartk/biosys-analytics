#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-01-31
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word = args[0]
    count = 0

    vowels = {i:0 for i in 'aeiouAEIOU'}
    for char in word:
        if char in vowels:
            count += 1
    
    if count == 1:             
        print('There is ' + str(count) + ' vowel in "' + word + '."')
    else:
        print('There are ' + str(count) + ' vowels in "' + word + '."')


# --------------------------------------------------
main()
