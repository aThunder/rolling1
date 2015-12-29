import json
import urllib.request
import sqlite3

class spCOT():

    def __init__(self,url):
        self.url = url
        self.conn = sqlite3.connect('allCot.db')
        self.c = self.conn.cursor()


    def getData(self):
        openURL = urllib.request.urlopen(self.url)
        readURL = openURL.read()
        self.datax = json.loads(readURL.decode("utf8"))

        print("TTL Reportable Long: ",self.datax['dataset']['data'][0][14])
        print("TTL Reportable Short: ",self.datax['dataset']['data'][0][15])
        print("Non-Reportable Long: ",self.datax['dataset']['data'][0][16])
        print("Non-Reportable Short: ",self.datax['dataset']['data'][0][17])

    def createSQL(self):
        self.c.execute("DROP TABLE IF EXISTS sp5")

        self.c.execute("CREATE TABLE sp5 (ID INTEGER PRIMARY KEY,Date,OpenInt,RptableLong REAL,RptableShort REAL, "
                  "NonRptableLong REAL,NonRptableShort)")

    def populateSQL(self):
        counter = 0
        for line in self.datax['dataset']['data']:
            # print('day: ',line)

            self.c.execute("INSERT OR IGNORE INTO sp5"
                           "(date,OpenInt,RptableLong,RptableShort,NonRptableLong,NonRptableShort)"
                            " VALUES(?,?,?,?,?,?)",
                            (self.datax['dataset']['data'][counter][0],
                            self.datax['dataset']['data'][counter][1],
                            self.datax['dataset']['data'][counter][14],
                            self.datax['dataset']['data'][counter][15],
                            self.datax['dataset']['data'][counter][16],
                            self.datax['dataset']['data'][counter][17]))

            counter += 1
            self.conn.commit()

            # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

url = "https://www.quandl.com/api/v3/datasets/CFTC/TIFF_CME_SC_ALL.json"
a = spCOT(url)
b = a.getData()
newOrExist = input("Create a new table('c') or use existing table('e')?: ")
if newOrExist == 'c':
    c1 = a.createSQL()
    c2 = a.populateSQL()
elif newOrExist == 'e':
    c2 = a.populateSQL()
else:
    print("'{0}' is an Invalid entry".format(newOrExist))


##########
# 'column_names': ['Date', 'Open Interest', 'Dealer Long Positions', 'Dealer Short Positions',
        #                  'Dealer Spread Positions', 'Asset Mgr LongPositions', 'Asset Mgr Short Positions',
        #                  'Asset Mgr Spread Positions', 'Lev Money Long Positions', 'Lev Money Short Positions',
        #                  'Lev Money Spread Positions', 'Other Reportable Long Positions',
        #                  'Other Reportable Short Positions', 'Other Reportable Spread Positions',
        #                  'Total Reportable Long Positions', 'Total Reportable Short Positions',
        #                  'Non-Reportable Long Positions', 'Non-Reportable Reportable Positions']
