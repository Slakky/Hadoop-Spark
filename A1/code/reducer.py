#!/usr/bin/python3

"""reducer.py"""

import sys
import json

current_pronoun = None
current_count = 0
pronoun = None

for line in sys.stdin:
    line = line.strip()
    pronoun, count = line.split(',',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if current_pronoun == pronoun:
        current_count += count
    else:
        if current_pronoun:
            print('{},{}'.format(current_pronoun, current_count))
        current_count = count
        current_pronoun = pronoun

if current_pronoun == pronoun:
    print('{},{}'.format(current_pronoun, current_count))
