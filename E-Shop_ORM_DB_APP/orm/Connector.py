import mysql.connector
class Model:
    def conn():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="e-shop"
        )
        return mydb

    

    def executeUpdateSQL(sql):
        mydb = Model.conn()
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        
    def executeFetchSQL(sql):
        mydb = Model.conn()
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result