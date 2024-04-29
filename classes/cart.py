# class for cart management

class Cart:
    def __init__(self,inventory):
        self.items = []
        self.inventory = inventory

    def add_item(self, product, quantity):
        if quantity <= product.quantity:
           self.items.append((product, quantity))
           return f"Added {product.name} - {product.product_id} to your cart successfully!"
        else:
          return "Sorry, insuffecient quantity!"
        
    def view_cart(self):
        if len(self.items) == 0:
            print("Your cart is empty. Please add items to your cart first.")
            return
        else:
            for (p,q) in self.items:
              print(f"Product: {p.name}, Quantity: {q}")

            action = input("Do you want to remove/update items from your cart? (yes/no): ")
            if action.lower() == 'yes':
                product_id = int(input("Enter the ID of the product you want to remove/update: "))
                doesProductExist = True #self.check_item(product_id)
                if doesProductExist:
                    product = self.inventory.get_product(product_id)
                    print("1.Remove Item from cart.")
                    print("2.Update item Quantity")
                    action = input("Please choose (1-2): ")
                    if action == "1" :
                        self.remove_item(product)
                    elif action == "2":
                        newQuantity = int(input("please enter new quantity"))   
                        self.update_quantity(product , newQuantity) 
                 
                else:
                  print("Product not found in cart.")
 
    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def update_quantity(self, product, quantity):
        self.remove_item(product)
        self.add_item(product,quantity)
        

    def check_item(self,product_id):
        for (p, q) in self.items:
            if p.product_id == product_id:
                return True
        return False       

        
