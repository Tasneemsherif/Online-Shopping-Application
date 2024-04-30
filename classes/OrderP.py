# Order placement class

import datetime
 
class OrderP:
# Assigning order id
    counter = 0
    def __init__(self,Cart):
        
        self.timestamp_part = datetime.datetime.now().strftime("%Y%m%d%H%M")
        OrderP.counter += 1
        self.items = Cart.items
        self.total_amount = 0
        # return f"{timestamp_part}-{counter}"

    def check_decrement(self):
       for (product,quantity) in self.items: 
        
            if quantity <= product.quantity:
                product.quantity -= quantity
            elif product.quantity > 0 :
                print( f"Sorry, insuffecient quantity! Please, try again with an amout lower then {product.quantity}")
                return
            else:
                print( "Sorry, zero stock item")
                return

        
    def total (self):

        for (p,q) in self.items: 
            self.total_amount += p.price * q
        self.payment()
            

    def checkout(self):
        print (f"your purchase of")
        for (p,q) in self.items:
            print (f"{q} {p.name} , with a Unit Price of: {p.price}EGP")
        print(f'''with a total of {self.total_amount}EGP is successful
        Your order Id : {self.timestamp_part}-{OrderP.counter}''') 
        
    def payment(self):
        print("Please, choose a payment method")
        print("1.Cash.")
        print("2.Visa")
        action = input("Please choose (1-2): ")
        
        if action == "1":
            self.checkout()
        elif action == "2":
            cardNumber= input('Please, enter the 16 digits on your card')
            try:
                if len(cardNumber)==16 and int(cardNumber)>0:
                    self.checkout()

                else:
                    print("Invalid card number.")
                    print("Any key to exit")
                    print("2.Retry")
                    action = input("Please choose (1-2): ")
                    if action == "2":
                        self.payment()
                    else:
                        return
            except ValueError:
                print('Invalid card number.')
                print("Any key to exit")
                print("2.Retry")
                action = input("Please choose (1-2): ")
                if action == "2":
                    self.payment()
                else:
                    return
    
        
        