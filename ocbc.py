#!/usr/bin/env python

import re
from common import *

class OcbcYnabConverter(YnabConverter):

    def is_tx_row(self, row):
        return True if row and re.search('\d\d/\d\d/\d\d\d\d', row[0]) else False

    def process(self, stream):
        reader = csv.reader(stream)
        return [(row[0], '', self.get_category(row[1]), row[1], row[2], row[3]) for row in reader if self.is_tx_row(row)]

def main():
    converter = OcbcYnabConverter()
    converter.process_stdin()

if __name__ == '__main__':
    main()
