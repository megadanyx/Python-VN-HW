import mysql.connector

def conn():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="e-shop"
    )
    return mydb

mydb = conn()

def executeUpdateSQL(sql):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    mydb.close()
    
def executeFetchSQL(sql):
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result