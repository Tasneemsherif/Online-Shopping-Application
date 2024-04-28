class ShoppingApp:
    def __init__(self):
        self.products = []
        self.cart = []

    def display_menu(self):
        print("Welcome to the Shopping App!")
        print("1. Browse Products")
        print("2. View Cart")
        print("3. Place Order")
        print("4. Exit")

    def browse_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"- {product}")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item in self.cart:
                print(f"- {item}")

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
                self.place_order()
            elif choice == "4":
                print("Thank you for using the Shopping App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Example usage
app = ShoppingApp()
app.products = ["Product 1", "Product 2", "Product 3"]
app.run()