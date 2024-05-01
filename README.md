# Online Shopping Application
Welcome to the **Simple Online Shopping Application** project! This project is designed to implement a simple shopping experience in Python. Users can browse products, add them to their cart, and place orders. Additionally, this project covers aspects like product inventory management, error handling, and function modularity for code reusability and maintainability.

## Features
1. **Product Inventory Management**: Manage the product inventory with functions to add, update, or remove products.
2. **User Interface and Input Handling**: Display a user-friendly menu for navigation and handle user inputs.
3. **Product Browsing and Cart Management**: Allow users to browse products, add to their cart, and modify the cart's contents.
4. **Order Placement and Summary**: Handle the order placement process and generate an order summary.
5. **Function Modularity and Reusability**: Organize the code into modular and reusable functions.
6. **Error Handling and Exception Handling**: Implement robust error handling to improve user experience and code stability.

## Requirements
To run this project, you need:
- Python 3.x
- A terminal/command line interface

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>

2. Navigate to the project directory:
    ```bash
     cd Online-Shopping-Application

## How to Use
1. **Start the Application**:
   - Run the main Python script to start the application:
     ```bash
     python app.py
     ```

2. **Browse Products**:
   - Select the "Browse Products" option from the menu to view available products.
   - Use the product ID to view product details.

3. **Add Items to Cart**:
   - After browsing products, you can add items to your cart by entering the product ID and quantity.
   - View the cart at any time to check its contents.

4. **Place an Order**:
   - Once you've added items to your cart, you can proceed to place an order.
   - Follow the prompts to provide necessary information (e.g., shipping address, payment details).
   - An order summary will be generated upon successful placement.

5. **Exit**:
   - Select "Exit" from the menu to close the application.

## Test Cases
### Test Case 1: Adding Products to Inventory
- **Scenario**: Add new products to the inventory and verify their details.
- **Steps**:
  1. Add a product to the inventory (e.g., ID: 001, Name: T-shirt, Price: EGP 450, Quantity: 50).
  2. Add another product (e.g., ID: 002, Name: Jeans, Price: EGP 600, Quantity: 30).
- **Expected Outcome**: Products are added successfully to the inventory.
![Alt Text](https://github.com/Tasneemsherif/Online-Shopping-Application/blob/main/Test-(2).png)

### Test Case 2: Browsing Products
- **Scenario**: Browse through available products and view their details.
- **Steps**:
  1. Display the list of available products.
  2. Select a product and view its details.
- **Expected Outcome**: Product details are displayed correctly.

### Test Case 3: Adding Items to Cart
- **Scenario**: Add items to the cart and verify the cart's contents.
- **Steps**:
  1. Add multiple items to the cart.
  2. View the cart to confirm its contents.
- **Expected Outcome**: The cart contains the selected items with correct quantities.
![Alt Text](https://github.com/Tasneemsherif/Online-Shopping-Application/blob/main/Test-(3).png)

### Test Case 4: Placing Order
- **Scenario**: Place an order for items in the cart and generate an order summary.
- **Steps**:
  1. Confirm the cart contains items.
  2. Place the order and provide necessary details.
- **Expected Outcome**: Order is successfully placed, and an order summary is generated.
![Alt Text](https://github.com/Tasneemsherif/Online-Shopping-Application/blob/main/Test-(4).PNG)

### Test Case 5: Error Handling
- **Scenario**: Test error handling for invalid inputs and scenarios.
- **Steps**:
  1. Enter an invalid product ID when browsing products.
  2. Attempt to add an out-of-stock product to the cart.
  3. Provide invalid payment information during order placement.
- **Expected Outcome**: Appropriate error messages are displayed, guiding users to correct their inputs.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE). Please refer to the LICENSE file for more details.



