import json
import urllib.request
import sqlite3
import pandas
import numpy as np
import matplotlib.pyplot as plt


class spCOT():

    def __init__(self):
        self.conn = sqlite3.connect('allCot.db')
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row

    def queryData(self,criteria):
        self.criteria = criteria
        counter = 1
        self.netReportableList = []

        for item in self.criteria:
            print(item)
            self.selectALL = self.cursor.execute("SELECT * FROM comboCOT"
                                             " WHERE DATE > '2015-10-01' AND NAME LIKE '{0}'".format(item))

            for item2 in self.selectALL:
                print(counter,item2['Name'],item2['Date'],item2['OpenInt'])
                counter += 1
                netReportable = item2['RptableLong']-item2['RptableShort']
                netNonReportable = item2['NonRptableLong']-item2['NonRptableShort']
                self.netReportableList.append(netReportable)
                print(netReportable,netNonReportable)
    def plot1(self):
        plt.plot(self.netReportableList)
        plt.ylabel("Net Position")
        plt.xlabel("Date")
        plt.title("COT: {0} Net Reportable Position".format('TBonds'))
        plt.show()


    #         # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    a = spCOT()
    criteria1 = '%S&P%'
    criteria2 = '%Gold%'
    criteria3 = '%Bond%'
    criteria4 = [criteria1,criteria2,criteria3]

    criteria5 = ['%S&P%','%Gold%','%Bond%']

    b = a.queryData(criteria4)
    c= a.plot1()

if __name__ == '__main__': main()

##########
