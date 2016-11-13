import StringIO
from posb import *

TEST_INPUT = '''
31 Oct 2016
GV DBO
S$15.00
01 Nov 2016
FAIRPRICE XTRA-CHANGI SINGAPORE 065
S$56.15
04 Nov 2016
FAIRPRICE XTRA-CHANGI SINGAPORE 065
S$12.90
05 Nov 2016
TONI&GUY ESSENSUALS HA SINGAPORE 065
S$59.00
07 Nov 2016
TOYS'R'US (S) PL - VIV SINGAPORE 065
S$405.89
07 Nov 2016
THE CHOP HOUSE
S$61.20
08 Nov 2016
FAIRPRICE FINEST-CHANG SINGAPORE 065
S$1.50
09 Nov 2016
FAIRPRICE XTRA-CHANGI SINGAPORE 065
S$30.60
09 Nov 2016
COLD STORAGE EASTWOOD
S$10.10
11 Nov 2016
COLD STORAGE EASTWOOD
S$26.97
11 Nov 2016
FAIRPRICE XTRA-CHANGI SINGAPORE 065
S$23.65
11 Nov 2016
COLD STORAGE EASTWOOD
S$49.97
'''

def test_process():
    f = StringIO.StringIO(TEST_INPUT)
    rows = PosbYnabConverter().process(f)

    assert len(rows) == 12
    assert rows[ 0] == ("31/10/2016", "", "Others",        "GV DBO",                               "15.00", "")
    assert rows[ 1] == ("01/11/2016", "", "Groceries",     "FAIRPRICE XTRA-CHANGI SINGAPORE 065",  "56.15", "")
    assert rows[ 2] == ("04/11/2016", "", "Groceries",     "FAIRPRICE XTRA-CHANGI SINGAPORE 065",  "12.90", "")
    assert rows[ 3] == ("05/11/2016", "", "Personal care", "TONI&GUY ESSENSUALS HA SINGAPORE 065", "59.00", "")
    assert rows[ 4] == ("07/11/2016", "", "Ivan",          "TOYS'R'US (S) PL - VIV SINGAPORE 065", "405.89", "")
    assert rows[ 5] == ("07/11/2016", "", "Eating out",    "THE CHOP HOUSE",                       "61.20", "")
    assert rows[ 6] == ("08/11/2016", "", "Groceries",     "FAIRPRICE FINEST-CHANG SINGAPORE 065", "1.50", "")
    assert rows[ 7] == ("09/11/2016", "", "Groceries",     "FAIRPRICE XTRA-CHANGI SINGAPORE 065",  "30.60", "")
    assert rows[ 8] == ("09/11/2016", "", "Groceries",     "COLD STORAGE EASTWOOD",                "10.10", "")
    assert rows[ 9] == ("11/11/2016", "", "Groceries",     "COLD STORAGE EASTWOOD",                "26.97", "")
    assert rows[10] == ("11/11/2016", "", "Groceries",     "FAIRPRICE XTRA-CHANGI SINGAPORE 065",  "23.65", "")
    assert rows[11] == ("11/11/2016", "", "Groceries",     "COLD STORAGE EASTWOOD",                "49.97", "")

