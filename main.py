from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Miš", 20, 10))
manager.add_product(Product("Tastatura", 50, 7))

cart = Cart()

cart.add_to_cart(manager.products[0])  
cart.add_to_cart(manager.products[1])  
cart.add_to_cart(manager.products[2])  

print("\n--- Korpa kupca ---")
cart.display_cart()
print(f"Ukupna vrednost za naplatu: {cart.total_cart_value()} dinara")
