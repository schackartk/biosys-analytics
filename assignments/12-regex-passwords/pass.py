#!/usr/bin/env python3
"""
Author : schackartk
Date   : 2019-04-02
Purpose: Facebook password thing
"""

import os
import sys
import re


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: PASSWORD ALT')
        sys.exit(1)

    password = args[0]
    alt = args[1]
    match = False

    acceptable = [password,password.upper(),password.capitalize()]

    regular = re.compile('.?' + password +'.?')

    if regular.match(alt):
        match = True
    elif alt in acceptable:
        match = True

    print('{}'.format("ok" if match else "nah"))


# --------------------------------------------------
main()
