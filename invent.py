import json
import os
class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "category": self.category
        }
    @staticmethod
    def from_dict(data):
        return Product(data["name"], data["price"], data["quantity"], data["category"])
products = []
DATA_FILE = "products.json"
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump([p.to_dict() for p in products], f, indent=4)
def load_data():
    global products
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                products = [Product.from_dict(p) for p in data]
        except json.JSONDecodeError:
            products = []

def add_product():
    name = input("Enter product name: ").strip()
    for p in products:
        if p.name.lower() == name.lower():
            print("Error: Product with this name already exists!")
            return
    try:
        price = float(input("Enter product price: "))
        if price <= 0:
            print("Price: Invalid price (must be greater than 0)")
            return
    except ValueError:
        print("Price: Invalid price (not a number)")
        return

    try:
        quantity = int(input("Enter product quantity: "))
        if quantity <= 0:
            print("Quantity: Invalid quantity (must be greater than 0)")
            return
    except ValueError:
        print("Quantity: Invalid quantity (not a number)")
        return

    category = input("Enter product category: ").strip()
    product = Product(name, price, quantity, category)
    products.append(product)
    save_data()
    print("Product added successfully!") 

def view_products():
    if not products:
        print("No products available.")
        return
    print("\n==== Product List ====")
    for product in products:
        print("--------------------------")
        print(f"Name: {product.name}")
        print(f"Price: ${product.price:.2f}")
        print(f"Quantity: {product.quantity}" + (" ⚠️ (Low Stock!)" if product.quantity <= 5 else ""))
        print(f"Category: {product.category}")

def search_product():
    if not products:
        print("No products available.")
        return
    name = input("Enter product name to search: ").strip()
    found = False
    for product in products:
        if product.name.lower() == name.lower():
            print("------------------------")
            print(f"Name: {product.name}")
            print(f"Price: ${product.price:.2f}")
            print(f"Quantity: {product.quantity}")
            print(f"Category: {product.category}")
            found = True
            break
    if not found:
        print("Product is not found.")

def delete_product():
    if not products:
        print("No products available.")        
        return
    name = input("Enter product name to delete: ").strip()
    found = False
    for product in products:
        if product.name.lower() == name.lower():
            products.remove(product)
            save_data()
            print("Product deleted successfully!")
            found = True
            break
    if not found:
        print("Product is not found.")

def update_product():
    if not products:
        print("No products available.")
        return
    name = input("Enter product name to update: ").strip()
    found = False
    for product in products:
        if product.name.lower() == name.lower():
            try:
                new_price = float(input("Enter new price: "))
                if new_price <= 0:
                    print("Price: Invalid price (must be greater than 0)")
                    return
            except ValueError:
                print("Price: Invalid price (not a number)")
                return

            try:
                new_quantity = int(input("Enter new quantity: "))
                if new_quantity <= 0:
                    print("Quantity: Invalid quantity (must be greater than 0)")
                    return
            except ValueError:
                print("Quantity: Invalid quantity (not a number)")
                return

            new_category = input("Enter new category: ").strip()
            product.price = new_price
            product.quantity = new_quantity
            product.category = new_category
            save_data()
            print("Product updated successfully!")
            found = True
            break
    if not found:
        print("Product is not found.")                 

# Load saved products on startup
load_data()

while True:
    print("\n==== Inventory & Product Management System ====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Update Product")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        search_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        update_product()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")