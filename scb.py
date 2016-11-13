#!/usr/bin/env python

from common import *
import StringIO
import re

def line_gen(stream):
    for line in stream:
        line = line.strip()
        if line and re.search('^\d\d/\d\d/\d\d\d\d', line):
            yield line

def get_amount(s, is_expense):
    amount = s.replace('SGD ', '')
    if amount[-2:] == 'DR':
        return amount.replace(' DR', '') if is_expense else ''
    elif amount[-2:] == 'CR':
        return amount.replace(' CR', '') if not is_expense else ''
    else:
        raise RuntimeError('Unexpected input: "%s"' % s)

class ScbYnabConverter(YnabConverter):
    def process(self, stream):
        s = '\n'.join([line for line in line_gen(stream)])
        reader = csv.reader(StringIO.StringIO(s))
        return [(row[0], '', self.get_category(row[1]), row[1], get_amount(row[3], True), get_amount(row[3], False)) for row in reader]

def main():
    ScbYnabConverter().process_stdin()

if __name__ == '__main__':
    main()
