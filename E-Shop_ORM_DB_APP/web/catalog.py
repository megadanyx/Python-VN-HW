#!/usr/bin/python
import sys
sys.path.append("D:\Curs Python\Curs_Python_niv_2\Project_temp\ORM_Class_DB")

from orm.ProductCatalog import ProductCatalog

products = ProductCatalog.index()

print()
for product in products:

    print(f"{product.name:30} | {product.price_value} {product.price_unit} | Quantity: {product.quantity}")
