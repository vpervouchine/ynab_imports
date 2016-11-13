#!/usr/bin/env python

import re
from common import *

def get_amount(s, is_expense):
    is_negative = s[0] == '-'
    if is_negative == is_expense:
        return s.replace('-', '')
    else:
        return ''

class CitibankYnabConverter(YnabConverter):

    def process(self, stream):
        reader = csv.reader(stream)
        return [(row[0], '', self.get_category(row[1]), row[1], get_amount(row[2], True), get_amount(row[2], False)) for row in reader if row]

def main():
    converter = CitibankYnabConverter()
    converter.process_stdin()

if __name__ == '__main__':
    main()
