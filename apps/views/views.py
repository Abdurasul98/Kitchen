from core.file_manager import FileManager


def show_products():
    products = FileManager("products").read()
    for product in products:
        print(f"ID: {product[0]} Product name: {product[1]} Price: {product[2]} Quantity: {product[3]}")


def calculate():
    pass