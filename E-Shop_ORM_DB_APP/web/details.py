#!/usr/bin/python
import sys
import cgi
# takes the input and puts in into the DATA vatiable

data = cgi.FieldStorage()

sys.path.append("D:\Curs Python\Curs_Python_niv_2\Project_temp\ORM_Class_DB")

from orm.ProductCatalog import ProductCatalog

product = ProductCatalog.details(data.getvalue('id'))

print()

print(f"{product.name:30} | {product.price_value} {product.price_unit} | Quantity: {product.quantity}")
