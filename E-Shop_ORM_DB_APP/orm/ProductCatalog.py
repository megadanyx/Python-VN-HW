from .Product import Product

class ProductCatalog:
    def index():
        products = Product.all()
        return products
    def details(id):
           product = Product.get(id)
           return product