# from .Connector import *
from .Connector import executeUpdateSQL,executeFetchSQL
from .crypto import MyHasher
# Modelul tabelului SQL Product

class Client:
    def __init__(self, id, name, Email, Phone, is_vip, password ):
        self.id = id
        self.name = name
        self.Email = Email
        self.Phone = Phone
        self.is_vip = is_vip
        self.password = MyHasher(password,Email)
    def create(self):
            sql = f"INSERT INTO client(id, name, Email, Phone, is_vip, password)\
                VALUES ({self.id},  \"{self.name}\",  \"{self.Email}\",  \"{self.Phone}\",  {self.is_vip},  \"{self.password}\");"
            executeUpdateSQL(sql)
            
    def save(self):
        
        sql = f"UPDATE client SET name=\"{self.name}\" , Email=\"{self.Email}\", Phone=\"{self.Phone}\", is_vip=\"{self.is_vip}\", password=\"{self.password}\" WHERE id = {self.id};"
        executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM client WHERE id = {self.id};"
        executeUpdateSQL(sql)
        
    
    def get(id):
        sql = f"SELECT * FROM client WHERE id = {id};"
        client_list = executeFetchSQL(sql)
        if len(client_list) == 1:
            id, name, Email, Phone, is_vip, password  = client_list[0]
            client = Client(id, name, Email, Phone, is_vip, password)
        else :
            client = None
        return client
        # HW 2 : Write a condition that returns None when there is no product anvalible
        # product = mycursor.fetchall().copy()
        # if len(product) == 1 :
        #    return product[0]
        # else : 
        #    return None 
    def getpass(self):
        sql = f"SELECT * FROM client WHERE password = \"{self.password}\";"
        client_list = executeFetchSQL(sql)
        if len(client_list) == 1:
            client = client_list[0][5]
        else :
            client = None
        return client
        
    def all():
        sql = f"Select * from client;"
        Client_List = executeFetchSQL(sql)
        clients = []
        for product_tuple in Client_List:
            # HW1: try to optimize multiple parametrs into a functio
            id, name, Email, Phone, is_vip, password = product_tuple
            client = Client(id, name, Email, Phone, is_vip, password)   
            clients.append(client) 
        return clients

    def __str__(self):
        return f"Client id {self.id}"
    def __repr__(self):
        return str(self)
