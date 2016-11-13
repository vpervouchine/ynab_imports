#!/usr/bin/env python

import re
import calendar
from common import *

months = dict((v,k) for k, v in enumerate(calendar.month_abbr))

def get_date(s):
    parts = s.split()
    return '%s/%s/%s' % (parts[0], months[parts[1]], parts[2])

def get_amount(s):
    return s.replace('S$', '')

def tx_gen(stream):
    date = None
    memo = None
    amount = None
    for line in stream:
        line = line.strip()
        if line:
            if not date:
                date = get_date(line)
            elif not memo:
                memo = line
            elif not amount:
                amount = get_amount(line)
                yield (date, memo, amount)
                (date, memo, amount) = (None, None, None)


class PosbYnabConverter(YnabConverter):

    def process(self, stream):
        return [(tx[0], '', self.get_category(tx[1]), tx[1], tx[2], '') for tx in tx_gen(stream)]
            
def main():
    converter = PosbYnabConverter()
    converter.process_stdin()

if __name__ == '__main__':
    main()
