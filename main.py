from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Miš", 20, 10))
manager.add_product(Product("Tastatura", 50, 7))
