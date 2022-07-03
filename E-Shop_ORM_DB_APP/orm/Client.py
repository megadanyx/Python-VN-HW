# from .Connector import *
from .Connector import Model
from .crypto import MyHasher
# Modelul tabelului SQL Product

class Client(Model):
    def __init__(self, id, name, Email, Phone, is_vip, password ):
        self.id = id
        self.name = name
        self.Email = Email
        self.Phone = Phone
        self.is_vip = is_vip
        self.password = MyHasher(password,Email)
        # Pentru a extrage din DB get(id).mypass !!
        self.mypass = password
    def create(self):
            sql = f"INSERT INTO client(id, name, Email, Phone, is_vip, password)\
                VALUES ({self.id},  \"{self.name}\",  \"{self.Email}\",  \"{self.Phone}\",  {self.is_vip},  \"{self.password}\");"
            Model.executeUpdateSQL(sql)
            
    def save(self):
        
        sql = f"UPDATE client SET name=\"{self.name}\" , Email=\"{self.Email}\", Phone=\"{self.Phone}\", is_vip=\"{self.is_vip}\", password=\"{self.password}\" WHERE id = {self.id};"
        Model.executeUpdateSQL(sql)

        # HW1 Finis Delete Method

    def delet(self):
       
        sql = f"DELETE FROM client WHERE id = {self.id};"
        Model.executeUpdateSQL(sql)
        
    
    def get(id):
        ## Parola corecta o aflam prin variabila mypass
        sql = f"SELECT * FROM client WHERE id = {id};"
        client_list = Model.executeFetchSQL(sql)
        if len(client_list) == 1:
            id, name, Email, Phone, is_vip, password  = client_list[0]
            client = Client(id, name, Email, Phone, is_vip, password)
        else :
            client = None
        return client


    # def getpass(self):    
    #     ## Aceasta functie returneaza reala parola a clientului hashata !!!!
    #     ## Prin get() vom primi parola rehashata!!
    #     ## Pentru a obtine parola hashata reala trebuie sa adaugi obiectul clientului cu parola lui reala -->
    #     ## Hasherul o va hasha si in asa mod vei obtine parola hashata!! (parola se va extrage din DB)    
    #     sql = f"SELECT * FROM client WHERE password = \"{self.password}\";" 
    #     client_list = Model.executeFetchSQL(sql)
    #     if len(client_list) == 1:
    #         client = client_list[0][5]
    #     else :
    #         client = None
    #     return client
        
    def all():
        sql = f"Select * from client;"
        Client_List = Model.executeFetchSQL(sql)
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
