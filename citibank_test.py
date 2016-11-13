import StringIO
from citibank import *

TEST_INPUT = '''
"16/09/2016","MOTHERCARE @ PARAGON     SINGAPORE    SG","-23.04","","'4265697003501009'"
"16/09/2016","TAKASHIMAYA (S) LTD      SINGAPORE    SG","-15.00","","'4265697003501009'"
"16/09/2016","GUARDIAN - MTE           SINGAPORE    SG","-9.10","","'4265697003501009'"
"16/09/2016","MOTHERCARE @ PARAGON     SINGAPORE    SG","-23.04","","'4265697003501009'"
"16/09/2016","TAKASHIMAYA (S) LTD      SINGAPORE    SG","-15.00","","'4265697003501009'"
"15/09/2016","MARKS & SPENCER - ROADSHOSINGAPORE    SG","-13.40","","'4265697003501009'"
"14/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-24.55","","'4265697003501009'"
"14/09/2016","SHENG SIONG              Singapore    SG","-74.54","","'4265697003501009'"
"13/09/2016","HUGGS - UE BIZHUB        SINGAPORE    SG","-5.00","","'4265697003501009'"
"13/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-25.80","","'4265697003501009'"
"11/09/2016","QOO10                    SINGAPORE    SG","-62.90","","'4265697003501009'"
"09/09/2016","SUBWAY - SIGLAP CENTRE   SINGAPORE    SG","-6.40","","'4265697003501009'"
"09/09/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-1.00","","'4265697003501009'"
"08/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-31.50","","'4265697003501009'"
"07/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-37.45","","'4265697003501009'"
"06/09/2016","TP DENTAL SURGEONS P L   SINGAPORE    SG","-139.10","","'4265697003501009'"
"06/09/2016","OG - PEOPLE'S PARK       SINGAPORE    SG","-61.60","","'4265697003501009'"
"06/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-9.80","","'4265697003501009'"
"05/09/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-101.95","","'4265697003501009'"
"02/09/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-12.51","","'4265697003501009'"
"31/08/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-24.10","","'4265697003501009'"
"31/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-73.70","","'4265697003501009'"
"30/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-143.40","","'4265697003501009'"
"29/08/2016","UNIQLO CHINATOWN POINT   SINGAPORE    SG","-15.80","","'4265697003501009'"
"29/08/2016","STANDARD CHARTERED       Visa Direct  SG","1275.13","","'4265697003501009'"
"26/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-43.45","","'4265697003501009'"
"26/08/2016","SHENG SIONG              Singapore    SG","-146.42","","'4265697003501009'"
"25/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-58.15","","'4265697003501009'"
"24/08/2016","ROYCE'                   SINGAPORE    SG","-25.00","","'4265697003501009'"
"24/08/2016","PHOON HUAT PL - SIMEI    SINGAPORE    SG","-43.75","","'4265697003501009'"
"22/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-12.80","","'4265697003501009'"
"22/08/2016","WATSON'S                 SINGAPORE    SG","-81.70","","'4265697003501009'"
"19/08/2016","GRAB COM                 SINGAPORE    SG","-10.00","","'4265697003501009'"
"19/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-61.80","","'4265697003501009'"
"18/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-15.80","","'4265697003501009'"
"17/08/2016","GOODSTUFF.SG             SINGAPORE    SG","-26.92","","'4265697003501009'"
"17/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-39.10","","'4265697003501009'"
"16/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-77.60","","'4265697003501009'"
"15/08/2016","METRO-PARAGON            SINGAPORE    SG","-84.91","","'4265697003501009'"
"11/08/2016","WATSON'S                 SINGAPORE    SG","-50.80","","'4265697003501009'"
"10/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-71.30","","'4265697003501009'"
"08/08/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-19.90","","'4265697003501009'"
"08/08/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-1.05","","'4265697003501009'"
"05/08/2016","GRAB COM                 SINGAPORE    SG","-10.00","","'4265697003501009'"
"05/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-32.85","","'4265697003501009'"
"04/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-61.50","","'4265697003501009'"
"02/08/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-19.48","","'4265697003501009'"
"02/08/2016","PHOON HUAT PL - SIMEI    SINGAPORE    SG","-100.15","","'4265697003501009'"
"02/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-38.05","","'4265697003501009'"
"01/08/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-44.10","","'4265697003501009'"
"31/07/2016","STANDARD CHARTERED       Visa Direct  SG","765.40","","'4265697003501009'"
"30/07/2016","WAN YANG FOOT-REFLEXOLOGYSINGAPORE    SG","-96.30","","'4265697003501009'"
"29/07/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-74.90","","'4265697003501009'"
"27/07/2016","FAIRPRICE FINEST-100AM AMSINGAPORE    SG","-15.25","","'4265697003501009'"
"26/07/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-71.15","","'4265697003501009'"
"25/07/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-3.70","","'4265697003501009'"
"25/07/2016","GUARDIAN - MTE           SINGAPORE    SG","-46.85","","'4265697003501009'"
"24/07/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-11.35","","'4265697003501009'"
"21/07/2016","TONI&GUY ESSENSUALS HAIRDSINGAPORE    SG","-47.20","","'4265697003501009'"
"20/07/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-31.50","","'4265697003501009'"
"20/07/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-7.10","","'4265697003501009'"
"20/07/2016","PHOON HUAT & CO.PL-SIMEI SINGAPORE    SG","-50.60","","'4265697003501009'"
"19/07/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-153.60","","'4265697003501009'"
"18/07/2016","FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG","-99.45","","'4265697003501009'"
"16/07/2016","COLD STORAGE-EASTWOOD    SINGAPORE    SG","-32.09","","'4265697003501009'"
'''

def test_process():
    f = StringIO.StringIO(TEST_INPUT)
    rows = CitibankYnabConverter().process(f)

    assert len(rows) == 65

    assert rows[00] == ("16/09/2016", "", "Ivan",           "MOTHERCARE @ PARAGON     SINGAPORE    SG", "23.04","")
    assert rows[01] == ("16/09/2016", "", "Shopping",       "TAKASHIMAYA (S) LTD      SINGAPORE    SG", "15.00","")
    assert rows[02] == ("16/09/2016", "", "Groceries",      "GUARDIAN - MTE           SINGAPORE    SG", "9.10","")
    assert rows[03] == ("16/09/2016", "", "Ivan",           "MOTHERCARE @ PARAGON     SINGAPORE    SG", "23.04","")
    assert rows[04] == ("16/09/2016", "", "Shopping",       "TAKASHIMAYA (S) LTD      SINGAPORE    SG", "15.00","")
    assert rows[05] == ("15/09/2016", "", "Shopping",       "MARKS & SPENCER - ROADSHOSINGAPORE    SG", "13.40","")
    assert rows[06] == ("14/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "24.55","")
    assert rows[07] == ("14/09/2016", "", "Groceries",      "SHENG SIONG              Singapore    SG", "74.54","")
    assert  rows[8] == ("13/09/2016", "", "Eating out",     "HUGGS - UE BIZHUB        SINGAPORE    SG", "5.00","")
    assert  rows[9] == ("13/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "25.80","")
    assert rows[10] == ("11/09/2016", "", "Shopping",       "QOO10                    SINGAPORE    SG", "62.90","")
    assert rows[11] == ("09/09/2016", "", "Eating out",     "SUBWAY - SIGLAP CENTRE   SINGAPORE    SG", "6.40","")
    assert rows[12] == ("09/09/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "1.00","")
    assert rows[13] == ("08/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "31.50","")
    assert rows[14] == ("07/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "37.45","")
    assert rows[15] == ("06/09/2016", "", "Claimable",      "TP DENTAL SURGEONS P L   SINGAPORE    SG", "139.10","")
    assert rows[16] == ("06/09/2016", "", "Shopping",       "OG - PEOPLE'S PARK       SINGAPORE    SG", "61.60","")
    assert rows[17] == ("06/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "9.80","")
    assert rows[18] == ("05/09/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "101.95","")
    assert rows[19] == ("02/09/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "12.51","")
    assert rows[20] == ("31/08/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "24.10","")
    assert rows[21] == ("31/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "73.70","")
    assert rows[22] == ("30/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "143.40","")
    assert rows[23] == ("29/08/2016", "", "Shopping",       "UNIQLO CHINATOWN POINT   SINGAPORE    SG", "15.80","")
    assert rows[24] == ("29/08/2016", "", "Others",         "STANDARD CHARTERED       Visa Direct  SG", "", "1275.13")
    assert rows[25] == ("26/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "43.45","")
    assert rows[26] == ("26/08/2016", "", "Groceries",      "SHENG SIONG              Singapore    SG", "146.42","")
    assert rows[27] == ("25/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "58.15","")
    assert rows[28] == ("24/08/2016", "", "Shopping",       "ROYCE'                   SINGAPORE    SG", "25.00","")
    assert rows[29] == ("24/08/2016", "", "Groceries",      "PHOON HUAT PL - SIMEI    SINGAPORE    SG", "43.75","")
    assert rows[30] == ("22/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "12.80","")
    assert rows[31] == ("22/08/2016", "", "Groceries",      "WATSON'S                 SINGAPORE    SG", "81.70","")
    assert rows[32] == ("19/08/2016", "", "Taxi",           "GRAB COM                 SINGAPORE    SG", "10.00","")
    assert rows[33] == ("19/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "61.80","")
    assert rows[34] == ("18/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "15.80","")
    assert rows[35] == ("17/08/2016", "", "Shopping",       "GOODSTUFF.SG             SINGAPORE    SG", "26.92","")
    assert rows[36] == ("17/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "39.10","")
    assert rows[37] == ("16/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "77.60","")
    assert rows[38] == ("15/08/2016", "", "Shopping",       "METRO-PARAGON            SINGAPORE    SG", "84.91","")
    assert rows[39] == ("11/08/2016", "", "Groceries",      "WATSON'S                 SINGAPORE    SG", "50.80","")
    assert rows[40] == ("10/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "71.30","")
    assert rows[41] == ("08/08/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "19.90","")
    assert rows[42] == ("08/08/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "1.05","")
    assert rows[43] == ("05/08/2016", "", "Taxi",           "GRAB COM                 SINGAPORE    SG", "10.00","")
    assert rows[44] == ("05/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "32.85","")
    assert rows[45] == ("04/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "61.50","")
    assert rows[46] == ("02/08/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "19.48","")
    assert rows[47] == ("02/08/2016", "", "Groceries",      "PHOON HUAT PL - SIMEI    SINGAPORE    SG", "100.15","")
    assert rows[48] == ("02/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "38.05","")
    assert rows[49] == ("01/08/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "44.10","")
    assert rows[50] == ("31/07/2016", "", "Others",         "STANDARD CHARTERED       Visa Direct  SG", "", "765.40")
    assert rows[51] == ("30/07/2016", "", "Personal care",  "WAN YANG FOOT-REFLEXOLOGYSINGAPORE    SG", "96.30","")
    assert rows[52] == ("29/07/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "74.90","")
    assert rows[53] == ("27/07/2016", "", "Groceries",      "FAIRPRICE FINEST-100AM AMSINGAPORE    SG", "15.25","")
    assert rows[54] == ("26/07/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "71.15","")
    assert rows[55] == ("25/07/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "3.70","")
    assert rows[56] == ("25/07/2016", "", "Groceries",      "GUARDIAN - MTE           SINGAPORE    SG", "46.85","")
    assert rows[57] == ("24/07/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "11.35","")
    assert rows[58] == ("21/07/2016", "", "Personal care",  "TONI&GUY ESSENSUALS HAIRDSINGAPORE    SG", "47.20","")
    assert rows[59] == ("20/07/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "31.50","")
    assert rows[60] == ("20/07/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "7.10","")
    assert rows[61] == ("20/07/2016", "", "Groceries",      "PHOON HUAT & CO.PL-SIMEI SINGAPORE    SG", "50.60","")
    assert rows[62] == ("19/07/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "153.60","")
    assert rows[63] == ("18/07/2016", "", "Groceries",      "FAIRPRICE XTRA-CHANGI BIZSINGAPORE    SG", "99.45","")
    assert rows[64] == ("16/07/2016", "", "Groceries",      "COLD STORAGE-EASTWOOD    SINGAPORE    SG", "32.09","")

