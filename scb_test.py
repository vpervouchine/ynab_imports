import StringIO
from scb import *

TEST_INPUT = '''
VISA PLATINUM REWARDS,'4300920021648348

Transaction History:,19/06/2016 To 17/09/2016

Date,Transaction Description,Currency Amount,SGD Amount
			10/09/2016,COLD STORAGE EASTWOOD    SINGAPORE    SG,,SGD 2.30 DR
		
			10/09/2016,COLD STORAGE EASTWOOD    SINGAPORE    SG,,SGD 2.45 DR
		
			10/09/2016,COLD STORAGE EASTWOOD    SINGAPORE    SG,,SGD 30.55 DR
		
			09/09/2016,PAUL BAKERY@MBLM         SINGAPORE    SG,,SGD 5.80 DR
		
			08/09/2016,COLD STORAGE EASTWOOD    SINGAPORE    SG,,SGD 4.50 DR
		
			06/09/2016,STARBUCKS COFFEE - AST   SINGAPORE    SG,,SGD 5.70 DR
		
			06/09/2016,MMMM!@CHANGI CITY POINT  SINGAPORE    SG,,SGD 70.04 DR
		
			03/09/2016,COLD STORAGE EASTWOOD    SINGAPORE    SG,,SGD 25.67 DR
		
			29/08/2016,PAYMENT - THANK YOU,,SGD 188.00 CR
		
			27/08/2016,VICOM-CHANGI             SINGAPORE    SG,,SGD 18.19 DR
'''

def test_process():
    f = StringIO.StringIO(TEST_INPUT)
    rows = ScbYnabConverter().process(f)

    assert len(rows) == 10
    assert rows[0] == ('10/09/2016', '', 'Groceries',       'COLD STORAGE EASTWOOD    SINGAPORE    SG', '2.30',  '')
    assert rows[1] == ('10/09/2016', '', 'Groceries',       'COLD STORAGE EASTWOOD    SINGAPORE    SG', '2.45',  '')
    assert rows[2] == ('10/09/2016', '', 'Groceries',       'COLD STORAGE EASTWOOD    SINGAPORE    SG', '30.55', '')
    assert rows[3] == ('09/09/2016', '', 'Groceries',       'PAUL BAKERY@MBLM         SINGAPORE    SG', '5.80',  '')
    assert rows[4] == ('08/09/2016', '', 'Groceries',       'COLD STORAGE EASTWOOD    SINGAPORE    SG', '4.50',  '')
    assert rows[5] == ('06/09/2016', '', 'Eating out',      'STARBUCKS COFFEE - AST   SINGAPORE    SG', '5.70',  '')
    assert rows[6] == ('06/09/2016', '', 'Groceries',       'MMMM!@CHANGI CITY POINT  SINGAPORE    SG', '70.04', '')
    assert rows[7] == ('03/09/2016', '', 'Groceries',       'COLD STORAGE EASTWOOD    SINGAPORE    SG', '25.67', '')
    assert rows[8] == ('29/08/2016', '', 'Others',          'PAYMENT - THANK YOU',                      '',      '188.00')
    assert rows[9] == ('27/08/2016', '', 'Others',          'VICOM-CHANGI             SINGAPORE    SG', '18.19', '')

