from .Connector import *
# Modelul tabelului SQL Product

class BagItems:
    def __init__(self, bag_id, product_id, quantity):
        self.bag_id = bag_id
        self.product_id = product_id
        self.quantity = quantity

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
        sql = f"INSERT INTO bagitems (bag_id, product_id, quantity)\
            VALUES ({self.bag_id}, {self.product_id}, {self.quantity});"
        BagItems.executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE bagitems SET bag_id = {self.bag_id}, product_id= {self.product_id},quantity= {self.quantity};"
        BagItems.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM bagitems WHERE id = {self.bag_id};"
        BagItems.executeUpdateSQL(sql)
        
    
    def get(bag_id):
        sql = f"SELECT * FROM bagitems WHERE bag_id = {bag_id};"
        product_list = BagItems.executeFetchSQL(sql)
        products = []
        for product_tuple in product_list:
            bag_id,product_id,quantity = product_tuple
            product = BagItems(bag_id,product_id,quantity)
            products.append(product)
        return products
        
    def all():
        sql = f"Select * from bagitems;"
        Product_List = BagItems.executeFetchSQL(sql)
        products = []
        for product_tuple in Product_List:
            # HW1: try to optimize multiple parametrs into a functio
            bag_id,product_id,quantity = product_tuple
            product = BagItems(bag_id,product_id,quantity)   
            products.append(product) 
        return products

    def __str__(self):
        return f"\nBag_id: {self.bag_id}\nProduc_id: {self.product_id}\nQuantity: {self.quantity}"
    def __repr__(self):
        return str(self)
