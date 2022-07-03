from .Connector import Model
# Modelul tabelului SQL Product

class BagItems(Model):
    def __init__(self, bag_id, product_id, quantity):
        self.bag_id = bag_id
        self.product_id = product_id
        self.quantity = quantity
    def create(self):
        sql = f"INSERT INTO bagitems (bag_id, product_id, quantity)\
            VALUES ({self.bag_id}, {self.product_id}, {self.quantity});"
        Model.executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE bagitems SET bag_id = {self.bag_id}, product_id= {self.product_id},quantity= {self.quantity};"
        Model.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM bagitems WHERE id = {self.bag_id};"
        Model.executeUpdateSQL(sql)
        
    
    def get(bag_id):
        sql = f"SELECT * FROM bagitems WHERE bag_id = {bag_id};"
        product_list = Model.executeFetchSQL(sql)
        products = []
        for product_tuple in product_list:
            bag_id,product_id,quantity = product_tuple
            product = BagItems(bag_id,product_id,quantity)
            products.append(product)
        return products
        
    def all():
        sql = f"Select * from bagitems;"
        Product_List = Model.executeFetchSQL(sql)
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
