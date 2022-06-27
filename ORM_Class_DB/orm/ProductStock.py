from .Product import Product

class ProductStock:
    def isProductAvailable(productId):
        product = Product.get(productId)
        if product == None :
            return False
        elif product.quantity == 0:
            return False
        else:
            return True
    #HW3: finish this method
    def addProduct(myproduct):
        product = Product.get(myproduct.id)        # 1. check if the porduct exists in the table                                                                             
        if product == None:    
            Product.create(myproduct)              # 2. if it doest exist -> product.create()
        else:
            sql = f"UPDATE product SET quantity = quantity + {myproduct.quantity} WHERE id = {product.id};"
            Product.executeUpdateSQL(sql)          # 3. if it exist?      -> sum up the quanities -> product.save()                                                             
    
    #HW4: finish the method that removes the product completely       
    def removeProduct(product):
        product.delet()
        
    #HW5: finish the method that subtracts a product quantity from the stock
    def subProductQuantity(myproduct, amount):
        product = ProductStock.isProductAvailable(myproduct.id)
        if product == True:
            sql = f"UPDATE product SET quantity = quantity - {amount} WHERE id = {myproduct.id};"
            Product.executeUpdateSQL(sql)
        else:
            print("This product is not in stock!")