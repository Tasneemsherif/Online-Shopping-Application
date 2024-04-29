# Class for the inventory
from classes.Product import Product


class Inventory :
    def __init__(self):
        self.products = []

    # add new product
    def add_product (self, product_id, name, price, quantity):
        new_product = Product(product_id, name, price, quantity)
        self.products.append(new_product)
    
    # add new product
    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    #Upadate product
    def update_product (self, product_id, name, price, quantity):
        for product in self.products:
            if product.product_id == product_id :
                if name :
                    product.name = name
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                return print ("Updated!")
        return print ("Can't update the inventory.")
    
    #remove product
    def remove_product (self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove (product)
                return print(f"product with ID: {product_id} is Removed successfully")
        return print("Can't remove this product")
    
    # display inventory
    def display_inventory (self):
        print("Available products in the inventory:")
        for product in self.products:
            print (product)
          
