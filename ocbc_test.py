import StringIO
from ocbc import *

TEST_INPUT = '''
Account details for:,OCBC 365 Credit Card 4524-1920-0289-4073
Credit limit,"SGD 24,000.00"
Credit left,"SGD 23,648.21"

Transaction History 
Main Credit CardOCBC 365 Credit Card 4524-1920-0289-4073
Transaction date,Description,Withdrawals (SGD),Deposits (SGD)
07/11/2016,PAYMENT BY INTERNET,,633.55
06/11/2016,-1393 COLD STORAGE EASTWOSINGAPORE    SG,12.92,
05/11/2016,-1393 AJISEN RAMEN @ CHANSINGAPORE    SG,48.02,
04/11/2016,-1393 STARBUCKS COFFEE - SINGAPORE    SG,5.90,
01/11/2016,-1393 COSTA COFFEE - SOFISINGAPORE    SG,5.70,
31/10/2016,-1393 BREADTALK PL-KATG MSINGAPORE    SG,1.60,
31/10/2016,-1393 MCDONALD'S (CCP)   SINGAPORE    SG,8.00,
30/10/2016,-1393 COLD STORAGE EASTWOSINGAPORE    SG,79.15,
29/10/2016,-1393 COLD STORAGE EASTWOSINGAPORE    SG,10.10,
29/10/2016,-1393 COLD STORAGE EASTWOSINGAPORE    SG,14.20,
'''

def test_process():
    f = StringIO.StringIO(TEST_INPUT)
    rows = OcbcYnabConverter().process(f)
    assert rows[0] == ('07/11/2016', '', 'Others', 'PAYMENT BY INTERNET', '', '633.55')
    assert rows[1] == ('06/11/2016', '', 'Groceries', '-1393 COLD STORAGE EASTWOSINGAPORE    SG', '12.92', '')
    assert rows[2] == ('05/11/2016', '', 'Eating out', '-1393 AJISEN RAMEN @ CHANSINGAPORE    SG', '48.02', '')
    assert rows[3] == ('04/11/2016', '', 'Eating out', '-1393 STARBUCKS COFFEE - SINGAPORE    SG', '5.90', '')
    assert rows[4] == ('01/11/2016', '', 'Eating out', '-1393 COSTA COFFEE - SOFISINGAPORE    SG', '5.70', '')
    assert rows[5] == ('31/10/2016', '', 'Groceries', '-1393 BREADTALK PL-KATG MSINGAPORE    SG', '1.60', '')
