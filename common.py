import csv
import sys

HEADER='Date,Payee,Category,Memo,Outflow,Inflow'
CAT_GROCERIES       = 'Groceries'
CAT_EATING_OUT      = 'Eating out'
CAT_IVAN            = 'Ivan'
CAT_SHOPPING        = 'Shopping'
CAT_CLAIMABLE       = 'Claimable'
CAT_TAXI            = 'Taxi'
CAT_PERSONAL_CARE   = 'Personal care'
CAT_UNKNOWN         = 'Others'

CATEGORY_LISTS = {
    CAT_GROCERIES      : (
        'COLD STORAGE',
        'BREADTALK',
        'PAUL BAKERY',
        'MMMM!',
        'FAIRPRICE',
        'SHENG SIONG',
        'PHOON HUAT',
        'GUARDIAN',
        "WATSON'S",
    ),
    CAT_EATING_OUT      : (
        'STARBUCKS',
        'COSTA COFFEE',
        'AJISEN RAMEN',
        'MCDONALD',
        'IPPUDO',
        'HUGGS',
        'SUBWAY',
        'THE CHOP HOUSE',
    ),
    CAT_IVAN            : (
        'MOTHERCARE',
        "TOYS'R'US",
    ),
    CAT_TAXI            : (
        'GRAB COM',
    ),
    CAT_SHOPPING        : (
        'TAKASHIMAYA',
        'QOO10',
        'UNIQLO',
        'ROYCE',
        'OG - ',
        'MARKS & SPENCER',
        'GOODSTUFF.SG',
        'METRO-',
    ),
    CAT_PERSONAL_CARE   : (
        'WAN YANG FOOT',
        'TONI&GUY',
    ),
    CAT_CLAIMABLE       : (
        'TP DENTAL',
    ),
}

CATEGORIES = dict([(label, c) for c in CATEGORY_LISTS for label in CATEGORY_LISTS[c]])

class YnabConverter():
    
    def get_category(self, description):
        description = description.upper()
        for c in CATEGORIES:
            if description.find(c) != -1:
                return CATEGORIES[c]

        return CAT_UNKNOWN

    def process(self, stream):
        return []

    def process_stdin(self):
        rows = self.process(sys.stdin)
        print('%s\n%s' % (HEADER, '\n'.join([','.join(row) for row in rows])))
