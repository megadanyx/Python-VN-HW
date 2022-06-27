from .Connector import *
# Modelul tabelului SQL Product

class Bag:
    def __init__(self, id, Client_id):
        self.id = id
        self.Client_id = Client_id
      

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
    def create(self):
        sql = f"INSERT INTO bag (id, Client_id)\
            VALUES ({self.id}, {self.Client_id});"
        Bag.executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE bag SET id_cient= {self.Client_id};"
        Bag.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM bag WHERE id = {self.id};"
        Bag.executeUpdateSQL(sql)
        
    
    def get(id):
        sql = f"SELECT * FROM bag WHERE id = {id};"
        product_list = Bag.executeFetchSQL(sql)
        if len(product_list) == 1:
            id, Client_id = product_list[0]
            product = Bag(id,Client_id)
        else :
            product = None
        return product
        
    def all():
        sql = f"Select * from bag;"
        Product_List = Bag.executeFetchSQL(sql)
        products = []
        for product_tuple in Product_List:
            # HW1: try to optimize multiple parametrs into a functio
            id, Client_id = product_tuple
            product = Bag(id, Client_id)   
            products.append(product) 
        return products

    def __str__(self):
        return f"Bag ->{self.id} For Client ->{self.Client_id}"
    def __repr__(self):
        return str(self)
