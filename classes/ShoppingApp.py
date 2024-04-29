from colorama import Fore
from classes.Inventory import Inventory
from classes.Product import Product
class ShoppingApp:
    def __init__(self,inventory,cart):
        self.products = []
        self.cart = cart
        self.inventory = inventory

    def display_menu(self):
        print("Welcome to the Shopping App!")
        print("1. Browse Products")
        print("2. View Cart")
        print("3. Add to Cart")
        print("4. Place Order")
        print("5. Exit")
    
    def browse_products(self):
        self.inventory.display_inventory()
     

    def view_cart(self):
        if not self.cart:
            print(Fore.RED +"Your cart is empty." , end="")
        else:
            print("Your Cart:")
            self.cart.view_cart()

    def make_order(self):
        print(Fore.YELLOW +"Enter the ID of the product you want to view: " , end="")
        product_id = int(input())
        product = self.inventory.get_product(product_id)
        if product:
            #product_obj = Product(product)
            print(product)
            print(Fore.YELLOW +"Do you want to add this item to your cart? (yes/no): " , end="")
            action = input()
            if action.lower() == 'yes':
                print(Fore.YELLOW +"Enter the quantity: " , end="")
                quantity = int(input())
                isAdded = self.cart.add_item(product, quantity)
                print(Fore.GREEN + isAdded , end="")
        else:
            print("Product not found.")  
        print("1.Continue Adding to cart")
        print("2.Go Back To Menu")
        action = input("Please Choose (1-2): ")
        if action == "1":
          self.make_order()
        else: return

    def place_order(self):
        if not self.cart:
            print("Your cart is empty. Please add items to your cart first.")
            return

        print("Placing Order...")
        # Add your logic for placing the order here
        # This could involve processing payment, generating an order confirmation, etc.
        print("Order placed successfully!")

        # Clear the cart after placing the order
        self.cart = []

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.browse_products()
            elif choice == "2":
                self.view_cart()
            elif choice == "3":
                self.browse_products()
                self.make_order()
            elif choice == "4":
                self.place_order()
            elif choice == "5":
                print("Thank you for using the Shopping App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

