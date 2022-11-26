# ДЗ_1 - Жила Сергій. Добрий день!

class Product:
    def __init__(self, name_product: str, price: float):
        self.name= name_product
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity


class ShoppingCart():
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity):
        self.products.update({product: quantity})

    def total_price_cart(self):
        sum = 0
        for (product, quantity) in self.products.items():
            sum += product.total_price(quantity)
        return sum


banana = Product('banana', 7)
print(banana.total_price(7))
cart = ShoppingCart()
cart.add_product(Product('beer', 11), 3)
cart.add_product(Product('banana', 4), 8)
# cart.add_product(Product('banana', 4), 8)
print(cart.total_price_cart())
