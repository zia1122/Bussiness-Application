# Initialize an empty product list
products = []

# Function to display all products
def show_products():
    if len(products) == 0:
        print("No products available.")
    else:
        print("Products List:")
        for index, product in enumerate(products, start=1):
            print(f"{index}. Name: {product['name']}, Description: {product['description']}, "
                  f"Price: {product['price']}, Rating: {product['rating']}, Image: {product['image']}")

# Function to add a new product
def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    rating = float(input("Enter product rating (0.0 - 5.0): "))
    image = input("Enter product text image (text representing the image): ")

    # Append new product to the list
    products.append({"name": name, "description": description, "price": price, "rating": rating, "image": image})
    print(f"Product '{name}' added successfully.")

# Function to delete a product
def delete_product():
    show_products()
    if len(products) > 0:
        try:
            product_index = int(input("Enter the product number to delete: "))
            if 1 <= product_index <= len(products):
                removed_product = products.pop(product_index - 1)
                print(f"Product '{removed_product['name']}' deleted successfully.")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to update product rating
def update_product_rating():
    show_products()
    if len(products) > 0:
        try:
            product_index = int(input("Enter the product number to update rating: "))
            if 1 <= product_index <= len(products):
                new_rating = float(input("Enter new rating (0.0 - 5.0): "))
                products[product_index - 1]["rating"] = new_rating
                print(f"Product '{products[product_index - 1]['name']}' rating updated to {new_rating}.")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Function to display the menu
def display_menu():
    print("\nBusiness Application Menu")
    print("1. Show all products")
    print("2. Add new product")
    print("3. Delete a product")
    print("4. Update product rating")
    print("5. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                show_products()
            elif choice == 2:
                add_product()
            elif choice == 3:
                delete_product()
            elif choice == 4:
                update_product_rating()
            elif choice == 5:
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please choose between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the main program
    main()
