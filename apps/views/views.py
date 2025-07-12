from core.file_manager import FileManager


def show_products():
    products = FileManager("products").read()
    for product in products:
        print(product)