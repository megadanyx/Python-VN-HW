from .Connector import Model
from .Product import Product

class ProductStock(Model):
    def isProductAvailable(productId):
        product = Product.get(productId)
        if product == None :
            return False
        elif product.quantity == 0:
            return False
        else:
            return True

    #HW3: finish this method
    def addProduct(ProdID, quantity):
        # Add Product in Stock
        product = Product.get(ProdID)        # 1. check if the porduct exists in the table                                                                             
        if product == None:    
            Product.create(product)              # 2. if it doest exist -> product.create()
        else:
            sql = f"UPDATE product SET quantity = quantity + {quantity} WHERE id = {ProdID};"
            Model.executeUpdateSQL(sql)          # 3. if it exist?      -> sum up the quanities -> product.save()                                                             
    
    #HW4: finish the method that removes the product completely       
    def removeProduct(prodID):
        #REMUVE PROD
        sql = f"DELETE FROM product WHERE id = {prodID};"
        Model.executeUpdateSQL(sql)
        
    #HW5: finish the method that subtracts a product quantity from the stock
    def subProductQuantity(prod_id, amount):
        # Drop quanities produs from stock
        product = ProductStock.isProductAvailable(prod_id)
        if product == True:
            sql = f"UPDATE product SET quantity = quantity - {amount} WHERE id = {prod_id};"
            Model.executeUpdateSQL(sql)
            return True
        else:
            print("This product is not in stock!")
            return False