from .Connector import Model
# Modelul tabelului SQL Product

class Bag:
    def __init__(self, id, Client_id):
        self.id = id
        self.Client_id = Client_id
      

    def create(self):
        sql = f"INSERT INTO bag (id, Client_id)\
            VALUES ({self.id}, {self.Client_id});"
        Model.executeUpdateSQL(sql)

    def save(self):
        
        sql = f"UPDATE bag SET id_cient= {self.Client_id};"
        Model.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM bag WHERE id = {self.id};"
        Model.executeUpdateSQL(sql)
        
    
    def get(id):
        sql = f"SELECT * FROM bag WHERE id = {id};"
        product_list = Model.executeFetchSQL(sql)
        if len(product_list) == 1:
            id, Client_id = product_list[0]
            product = Bag(id,Client_id)
        else :
            product = None
        return product
        
    def all():
        sql = f"Select * from bag;"
        Product_List = Model.executeFetchSQL(sql)
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
