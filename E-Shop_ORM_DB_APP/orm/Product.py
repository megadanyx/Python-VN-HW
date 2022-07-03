from .Connector import Model
# Modelul tabelului SQL Product

class Product(Model):
    def __init__(self, id, name, price_value, price_unit, bar_code, quantity ):
        self.id = id
        self.name = name
        self.price_value = price_value
        self.price_unit = price_unit
        self.bar_code = bar_code
        self.quantity = quantity
    
    def create(self):
        sql = f"INSERT INTO product (id, name, price_value, price_unit, bar_code, quantity)\
            VALUES ({self.id},  \"{self.name}\",  {self.price_value},  \"{self.price_unit}\",  \"{self.bar_code}\",  {self.quantity});"
        Model.executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE product SET name=\"{self.name}\" , price_value={self.price_value}, price_unit=\"{self.price_unit}\", bar_code=\"{self.bar_code}\", quantity={self.quantity} WHERE id = {self.id};"
        Model.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM product WHERE id = {self.id};"
        Model.executeUpdateSQL(sql)
        
    
    def get(id):
        sql = f"SELECT * FROM product WHERE id = {id};"
        product_list = Model.executeFetchSQL(sql)
        if len(product_list) == 1:
            product = Product(*product_list[0])
        else :
            product = None
        return product
        # HW 2 : Write a condition that returns None when there is no product anvalible
        # product = mycursor.fetchall().copy()
        # if len(product) == 1 :
        #    return product[0]
        # else : 
        #    return None 
        
    def all():
        sql = f"Select * from product;"
        Product_List = Model.executeFetchSQL(sql)
        products = []
        for product_tuple in Product_List:
            # HW1: try to optimize multiple parametrs into a functio
            # id, name, price_value, price_unit, bar_code, quantity = product_tuple
            product = Product(*product_tuple)   
            products.append(product) 
        return products

    def __str__(self):
        return f"Product id {self.id}"
    def __repr__(self):
        return str(self)
