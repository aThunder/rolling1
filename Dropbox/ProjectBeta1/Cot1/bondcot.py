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

    def populateSQL(self):
        counter = 0
        for line in self.datax['dataset']['data']:
            # print('day: ',line)

            self.c.execute("INSERT OR IGNORE INTO comboCOT"
                           "(Dataset,Database,Name,Date,OpenInt,RptableLong,RptableShort,NonRptableLong,NonRptableShort)"
                            " VALUES(?,?,?,?,?,?,?,?,?)",
                            (self.datax['dataset']['dataset_code'],
                            self.datax['dataset']['database_code'],
                            self.datax['dataset']['name'],
                            self.datax['dataset']['data'][counter][0],
                            self.datax['dataset']['data'][counter][1],
                            self.datax['dataset']['data'][counter][14],
                            self.datax['dataset']['data'][counter][15],
                            self.datax['dataset']['data'][counter][16],
                            self.datax['dataset']['data'][counter][17]))

            counter += 1
            self.conn.commit()

            # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    url = "https://www.quandl.com/api/v3/datasets/CFTC/US_F_ALL.json"
    a = spCOT(url)
    a.getData()
    a.populateSQL()

if __name__ == '__main__': main()

##########

# "column_names":["Date","Open Interest","Dealer Longs","Dealer Shorts","Dealer Spreads",
#                 "Asset Manager Longs","Asset Manager Shorts","Asset Manager Spreads",
#                 "Leveraged Funds Longs","Leveraged Funds Shorts","Leveraged Funds Spreads",
#                 "Other Reportable Longs","Other Reportable Shorts","Other Reportable Spreads",
#                 "Total Reportable Longs","Total Reportable Shorts","Non Reportable Longs",
#                 "Non Reportable Shorts"]
