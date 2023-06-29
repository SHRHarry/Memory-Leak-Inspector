# -*- coding: utf-8 -*-

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class postgreSQL:
    def __init__(self):
        self.client = psycopg2.connect(database="postgres",
                                       user="postgres",
                                       password="admin",
                                       host="127.0.0.1",
                                       port="5432")
        self.client.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        print("Opened database successfully")
        
        # self.cur = self.client.cursor()
    
    def CreateTable(self, TableText):
        cur = self.client.cursor()
        cur.execute(TableText)
        
        self.client.commit()
        
        print("Table created successfully")
        cur.close()
        
        # self.client.close()
    
    def Insert(self, ValueText):
        cur = self.client.cursor()
        cur.execute(ValueText)
        self.client.commit()
        #print("Records created successfully")
        cur.close()
        
        # self.client.close()
        
    def SelectTableData(self, TableText):
        cur = self.client.cursor()
        cur.execute(f"SELECT TransactionID, TotalPrice, SettlementTime from {TableText}")
        rows = cur.fetchall()
        
        print("\n")
        for row in rows:
            print(f"TransactionID = {row[0]}\nTotalPrice = {row[1]}\nSettlementTime = {row[2]}")
        
        print("\nOperation done successfully")
        cur.close()
        
        # self.client.close()
    
    def UpdateTable(self, TableText, ItemText, ItemValue, IDText, IDValue):
        cur = self.client.cursor()
        
        UpdateText = f"UPDATE {TableText} set {ItemText} = {ItemValue} where {IDText}={IDValue}"
        cur.execute(UpdateText)
        self.client.commit()
        
        print("Total number of rows updated :", cur.rowcount)
        self.SelectTableData(TableText)
        
    def DeleteTableValue(self, TableText, IDText, IDValue):
        cur = self.client.cursor()
        
        DeleteText = f"DELETE from {TableText} where {IDText}={IDValue};"
        cur.execute(DeleteText)
        self.client.commit()
        
        print("Total number of rows deleted :", cur.rowcount)
        self.SelectTableData(TableText)
        
    def DeteteTable(self, TableText):
        cur = self.client.cursor()
        DeleteText = f"DROP TABLE {TableText};"
        cur.execute(DeleteText)
        self.client.commit()
        
        print("Table deleted :", cur.rowcount)
        
    def Close(self):
        self.client.close()

if __name__ == "__main__":
    '''
    postgresql = postgreSQL()
    TotalItem = "TotalItem"
    try:
        TableText = f'CREATE TABLE {TotalItem}
        (TransactionID INT PRIMARY KEY     NOT NULL,
         TotalPrice REAL    NOT NULL,
         SettlementTime INT     NOT NULL);'
        
        postgresql.CreateTable(TableText)
    except Exception as e:
        print(e)
        postgresql.DeteteTable(TotalItem)
        TableText = f'CREATE TABLE {TotalItem}
        (TransactionID INT PRIMARY KEY     NOT NULL,
         TotalPrice REAL    NOT NULL,
         SettlementTime INT     NOT NULL);'
        
        postgresql.CreateTable(TableText)
    
    ValueText = 'INSERT INTO TotalItem (TransactionID,TotalPrice,SettlementTime) 
    VALUES (1, 20000.00, 10)'
    postgresql.Insert(ValueText)
    
    ValueText = 'INSERT INTO TotalItem (TransactionID,TotalPrice,SettlementTime) 
    VALUES (2, 25000.00, 12)'
    postgresql.Insert(ValueText)
    
    ValueText = 'INSERT INTO TotalItem (TransactionID,TotalPrice,SettlementTime) 
    VALUES (3, 30000.00, 14)'
    postgresql.Insert(ValueText)
    
    postgresql.SelectTableData("TotalItem")
    
    TableText = "TotalItem"
    ItemText = "TotalPrice"
    ItemValue = 1000.00
    IDText = "TransactionID"
    IDValue = 2
    postgresql.UpdateTable(TableText, ItemText, ItemValue, IDText, IDValue)
    
    postgresql.DeleteTableValue(TableText, IDText, IDValue)
    
    postgresql.Close()
    '''