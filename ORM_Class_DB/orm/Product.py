from .Connector import executeUpdateSQL,executeFetchSQL
# Modelul tabelului SQL Product

class Product:
    def __init__(self, id, name, price_value, price_unit, bar_code, quantity ):
        self.id = id
        self.name = name
        self.price_value = price_value
        self.price_unit = price_unit
        self.bar_code = bar_code
        self.quantity = quantity

    # def executeUpdateSQL(sql):
    #     mycursor = mydb.cursor()
    #     mycursor.execute(sql)
    #     mydb.commit()
    #     mycursor.close()
    #     mydb.close()
    # def executeFetchSQL(sql):
    #     mycursor = mydb.cursor()
    #     mycursor.execute(sql)
    #     result = mycursor.fetchall()
    #     return result
    
    def create(self):
        sql = f"INSERT INTO product (id, name, price_value, price_unit, bar_code, quantity)\
            VALUES ({self.id},  \"{self.name}\",  {self.price_value},  \"{self.price_unit}\",  \"{self.bar_code}\",  {self.quantity});"
        executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE product SET name=\"{self.name}\" , price_value={self.price_value}, price_unit=\"{self.price_unit}\", bar_code=\"{self.bar_code}\", quantity={self.quantity} WHERE id = {self.id};"
        executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM product WHERE id = {self.id};"
        executeUpdateSQL(sql)
        
    
    def get(id):
        sql = f"SELECT * FROM product WHERE id = {id};"
        product_list = executeFetchSQL(sql)
        if len(product_list) == 1:
            id, name, price_value, price_unit, bar_code, quantity = product_list[0]
            product = Product(id, name, price_value, price_unit, bar_code, quantity)
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
        Product_List = executeFetchSQL(sql)
        products = []
        for product_tuple in Product_List:
            # HW1: try to optimize multiple parametrs into a functio
            id, name, price_value, price_unit, bar_code, quantity = product_tuple
            product = Product(id, name, price_value, price_unit, bar_code, quantity)   
            products.append(product) 
        return products

    def __str__(self):
        return f"Product id {self.id}"
    def __repr__(self):
        return str(self)
