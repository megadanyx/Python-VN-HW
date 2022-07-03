## ORM (object relation mapping)
from orm.ProductStock import ProductStock
from orm.Product import Product
from orm.Client import Client
from orm.Bag import Bag
from orm.BagItems import BagItems
from orm.CartManager import CartManager

Costumer = Client(3,"John_1" ,"IonBForce@mail.ru" , "+3735234568" , 1 ,"321654")
CartManager.clearCart(Costumer)
# CartManager.addItem(Costumer, 2, 10)
# CartManager.viewCart(Costumer)

# ProductStock.addProduct(4, 200)

# CartManager.addItem(client, 3 ,10)
# Client.create(client)
# Client.save(client)
# howpass = CartManager.CreateCart(client)
# print(howpass.mypass)


# p1 = Product(5, "My Product", 100, "UDS", "1111111111111", 100)
# ProductStock.subProductQuantity(p1, 5)

# p1 = Product(5, "My Product", 100, "UDS", "1111111111111", 10)
# ProductStock.addProduct(p1)




# p1.delet()
# all = Product.all()
# Prod_1 = all[0]
# print(Prod_1.price_value)

# available = ProductStock.isProductAvailable(1)
# print(available)

# p1 = Product(5, "My Prod", 100, "UDS", "1100464008403", 10)
# p2 = Product(2, "Second", 100,"UDS","213564688453",10)
# p1.create()
# p1.name = "Modify"
# p1.save()
# print(p2)
# products = Product.all()
# print(*products, sep = "\n")
# prod = Product.get(5)
# print(prod)
