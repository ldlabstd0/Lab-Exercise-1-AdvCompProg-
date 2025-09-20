class Product:
    INVENTORY = [] # stores all the products
    PRODUCT_COUNTER = 0 # auto-increment for unique IDs

    def __init__(self, PRODUCT_ID, NAME, CATEGORY, QUANTITY, PRICE, SUPPLIER):
        self.PRODUCT_ID = PRODUCT_ID
        self.NAME = NAME
        self.CATEGORY = CATEGORY
        self.QUANTITY = int(QUANTITY)
        self.PRICE = float(PRICE)
        self.SUPPLIER = SUPPLIER

    @classmethod
    def _add_product(cls, NAME, CATEGORY, QUANTITY, PRICE, SUPPLIER):
        cls.PRODUCT_COUNTER += 1 # next Id
        
        new_product = cls(cls.PRODUCT_COUNTER, NAME, CATEGORY, QUANTITY, PRICE, SUPPLIER)
        
        cls.INVENTORY.append(new_product) # add new product
        return "Product added successfully"
    
    @classmethod
    def _update_product(cls, PRODUCT_ID, QUANTITY=None, PRICE=None, SUPPLIER=None):
        for product in cls.INVENTORY: # loop to find the product ID
            if product.PRODUCT_ID == PRODUCT_ID:
                if QUANTITY is not None:
                    product.QUANTITY = int(QUANTITY)
                if PRICE is not None:
                    product.PRICE = float(PRICE)
                if SUPPLIER is not None:
                    product.SUPPLIER = SUPPLIER

                return "Product information updated successfully"
            
        return "Product not found"
    
    @classmethod
    def _delete_product(cls, PRODUCT_ID):
        for i, product in enumerate(cls.INVENTORY): # loop with index for easier deletion
            if product.PRODUCT_ID == PRODUCT_ID:
                del cls.INVENTORY[i]
                return "Product deleted successfully"
            
        return "Product not found."
    
    @classmethod
    def _display_inventory(cls):
        if not cls.INVENTORY:
            print("No products shown in inventory.")
        else:
            print(f"ID | Name | Category | Quantity | Price | Supplier")
            
            for product in cls.INVENTORY: # print details for each product
                print(f"{product.PRODUCT_ID} | {product.NAME} | {product.CATEGORY} | {product.QUANTITY} | ${product.PRICE:.2f} | {product.SUPPLIER}")

    @classmethod
    def get_product(cls, PRODUCT_ID):
        for product in cls.INVENTORY:
            if product.PRODUCT_ID == PRODUCT_ID:
                return product
        return None

class Order:
    
    def __init__(self, ORDER_ID, PRODUCT_ID, QUANTITY, CUSTOMER_INFO=None):
        self.ORDER_ID = ORDER_ID
        self.PRODUCT_ID = PRODUCT_ID
        self.QUANTITY = int(QUANTITY)
        self.CUSTOMER_INFO = CUSTOMER_INFO if CUSTOMER_INFO else "Guest"
    
    def place_order(self):
        product_to_order = Product.get_product(self.PRODUCT_ID)
        
        if product_to_order is None:
            return f"Order failed. Product with ID {self.PRODUCT_ID} not found."
            
        if self.QUANTITY > product_to_order.QUANTITY:
            return f"Order failed. Insufficient stock for Product ID {self.PRODUCT_ID}. Available: {product_to_order.QUANTITY}"
        
        product_to_order.QUANTITY -= self.QUANTITY # update and delete stock from the product
        
        return f"Order placed successfully. Order ID: {self.ORDER_ID}"


# DISPLAY ALL PART

p1 = Product._add_product("PC", "Electronics", 50, 1000, "Supplier A")
print(p1)
p2 = Product._add_product("T-Shirt", "Clothing", 100, 25, "Supplier B")
print(p2)
print()
print("Current Inventory:")
Product._display_inventory()
print()

p3 = Product._update_product(1, QUANTITY=45, PRICE=950) 
print(p3)
print()


print("Current Inventory:")
Product._display_inventory()
print()


p4 = Product._delete_product(2) # T-Shirt (ID 2) is removed
print(p4)
print()


print("Current Inventory:")
Product._display_inventory()
print()


order1 = Order(ORDER_ID=1, PRODUCT_ID=1, QUANTITY=2, CUSTOMER_INFO="John Doe")
print(order1.place_order())

print("\nInventory after order:")
Product._display_inventory()
