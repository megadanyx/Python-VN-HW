from numpy import insert
from orm.Product import Product
from .Connector import Model
from .ProductStock import ProductStock
from .BagItems import BagItems

class CartManager(Model):

    def CreateCart(Costumer):
        sql = f"INSERT INTO Bag(Client_id) values ({Costumer.id})"
        Model.executeUpdateSQL(sql)

    def countSelectCart(Costumer): ## Afiseaza cite cosuri are clientul, daca nr este 1 va returna id-ul cosului in caz contrar intreaba cu care vom lucra si returneaza nr/id cosului .
        sql = f"Select * from bag where Client_id=({Costumer.id})"
        carts = Model.executeFetchSQL(sql)
        if len(carts) > 0 and len(carts) != 1:
            print(f"Select Your Cart: ", end="| ")
            for index in range(len(carts)):
                print(f"{carts[index][0]}", end=" | ")
            respons = input(">>>>")
        else:
            respons = carts[0][0]        
        return respons
    # o functiu cind se aduga produsu sa se verifice daca acest produs deja exixta in acest cos sa se adune doar cantitatea!!
    def ifExistProductItems(bagId, product_id): # daca asa produs exista in cosul dat retuneaza True in caz contrar False.
        sql = f"select * from bagItems where bag_id={bagId} and product_id ={product_id};"
        products = Model.executeFetchSQL(sql)
        if len(products) > 0:
            return True
        else:
            return False


    
    def addItem(Costumer ,product_id, quantity ): # daca acest produs nu exita va fi adaugada daca exista va fi adunata doar cantitatea.
        if ProductStock.subProductQuantity(product_id, quantity):
            bagId = CartManager.countSelectCart(Costumer)
        if CartManager.ifExistProductItems(bagId, product_id): ## update!!!
            sql=f"update bagItems set quantity = quantity + {quantity} where bag_id = {bagId} and product_id = {product_id}"
            Model.executeUpdateSQL(sql)
        else:   
            sql = f"Insert INTO bagItems (bag_id, product_id, quantity) value ({bagId}, {product_id}, {quantity})"
            Model.executeUpdateSQL(sql)
                
    
    def removeItem(Costumer, product_id): # sterge produsl din cosul indicat
        bagId = CartManager.countSelectCart(Costumer)
        sql = f"delete from bagItems where bag_id={bagId} and product_id = {product_id};"
        Model.executeUpdateSQL(sql)
    
    def updateItem(Costumer, product_id, quantity): # reutilizeaza functia add ....
        CartManager.addItem(Costumer, product_id, quantity)
    
    def ReduceProdQuantity(Costumer, product_id, quantity): #
        bagId = CartManager.countSelectCart(Costumer)      # verifica cosurile si intreaba cu care se va lucra.
        if CartManager.ifExistProductItems(bagId, product_id):  # daca acest produs exista
            sql = f"update bagItems set quantity = quantity - {quantity} where bag_id = {bagId} and product_id = {product_id}"
            Model.executeUpdateSQL(sql)          # micsoreaza cantitatea cu cantitatea indicata!
            ProductStock.addProduct(product_id, quantity) # adauca cantitatea inapoi in stokul produselor.
            sql = f"select quantity from bagItems where bag_id={bagId} and product_id = {product_id};" 
            dbquantity = Model.executeFetchSQL(sql)  # daca in cos a ramas cantitatea 0 sau mai mica, sterge acest produs din cos
            if dbquantity[0][0] <= 0 :
                sql = f"delete from bagItems where bag_id={bagId} and product_id = {product_id};"
                Model.executeUpdateSQL(sql)
        else:
            print("This Product don't exist in your cart!")



    def clearCart(Costumer):
        bagId = CartManager.countSelectCart(Costumer)
        respons = input("Are you sure you want to remove this cart?(y/n) >> ")
        if respons == "y":
            sql = f"delete from bag where id={bagId};"
            Model.executeUpdateSQL(sql)
        
    def viewCart(Costumer):
        bagId = CartManager.countSelectCart(Costumer)
        sql = f"Select bagItems.bag_id ,product.name , bagItems.quantity from bagItems INNER JOIN Product ON bagItems.product_id = Product.id where bag_id = {bagId};"
        items   = Model.executeFetchSQL(sql)
        if len(items) == 0:
            print("Cart is empty !!!")
        else:
            for item in items:
                print(item)
            
# SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
# FROM Orders
# INNER JOIN Customers
# ON Orders.CustomerID=Customers.CustomerID;











