# Product Inventory Management
from classes.Inventory import Inventory
from classes.ShoppingApp import ShoppingApp
from classes.cart import Cart

inventory = Inventory()
cart = Cart(inventory)

# Add initial products
inventory.add_product(101, 'T-shirt', 450, 50)#40
inventory.add_product(102, 'Jeans', 600, 30)#10
app = ShoppingApp(inventory,cart)

app.products = inventory.products
app.run()


# def main():
    
#     # Display products
#     inventory.display_inventory()

#     # Update products
#     inventory.update_product(101, 'blouse', 450, 60)
#     inventory.display_inventory()

#     # Remove product
#     inventory.remove_product (102)
#     inventory.display_inventory()

# if __name__ == "__main__":
#     main()

# Order placement class
# from classes.Inventory import Inventory
# from classes.Product import Product
# from classes.cart import Cart
