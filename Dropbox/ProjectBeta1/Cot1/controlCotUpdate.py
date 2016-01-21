#controlCotUpdate.py

'''prompts user to create new SQL table or use existing
and then calls 3 other files to populate SQL table
'''

import json
import urllib.request
import sqlite3

class spCOT():

    def __init__(self):
        self.conn = sqlite3.connect('allCot.db')
        self.c = self.conn.cursor()

    def createSQL(self):
        self.c.execute("DROP TABLE IF EXISTS comboCOT")

        self.c.execute("CREATE TABLE comboCOT (ID INTEGER PRIMARY KEY,Dataset TEXT,Database TEXT,Name TEXT,Date,OpenInt INTEGER,RptableLong INTEGER,RptableShort INTEGER, "
                  "NonRptableLong INTGER,NonRptableShort INTEGER, UNIQUE (Name,Date))")


            # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

    def populateTables(self):
        import sp5cot,bondcot,goldcot
        stocks = sp5cot.main()
        bonds = bondcot.main()
        gold = goldcot.main()

def main():
    a = spCOT()
    print()
    newOrExist = input("Create a new table('c') or use existing table('e')?: ")
    print()
    if newOrExist == 'c':
        print("CAUTION: Creating a new table will delete all current data")
        print()
        doubleCheck = input("Type 'yes' to verify you want to create a new table: ")
        if doubleCheck == 'yes':
            a.createSQL()
        else:
            print("No new table created")

    b = a.populateTables()



if __name__ == '__main__': main()


