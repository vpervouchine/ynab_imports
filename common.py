import csv
import sys

HEADER='Date,Payee,Category,Memo,Outflow,Inflow'
CAT_GROCERIES   = 'Groceries'
CAT_EATING_OUT  = 'Eating out'
CAT_UNKNOWN     = 'Others'

CATEGORIES = {
        'COLD STORAGE'  : CAT_GROCERIES,
        'BREADTALK'     : CAT_GROCERIES,
        'STARBUCKS'     : CAT_EATING_OUT,
        'COSTA COFFEE'  : CAT_EATING_OUT,
        'AJISEN RAMEN'  : CAT_EATING_OUT,
        'MCDONALD'      : CAT_EATING_OUT,
}

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
