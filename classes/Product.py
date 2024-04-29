# Product Class
class Product:
    #last_id = 0
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id #self.product_id+=1
        self.name = name
        self.price = price
        self.quantity = quantity
    # print when an object is passed to functions
    def __str__(self):
        #return f"ID: {self.product_id} , Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return f"ID: {self.product_id} , Name: {self.name}, Price: {self.price}, Available: {'Yes' if self.quantity >0 else 'No'}"

