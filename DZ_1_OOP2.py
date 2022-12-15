# ДЗ_2 - Жила Сергій. Добрий день!

class Product:
    def __init__(self, name_product: str, price: float):
        self.name = name_product
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

    def __float__(self):
        return self.price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.name} - {self.price} UAH/piece'


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity):
        self.products.append(product)
        self.quantities.append(quantity)

    def __add__(self, other):
        if isinstance(other, Product):
            self.add_product(other, 1)
            return self
        elif isinstance(other, ShoppingCart):
            cart = ShoppingCart()
            for (product, quantity) in zip(self.products + other.products, self.quantities + other.quantities):
                cart.add_product(product, quantity)
            return cart

    def total_price_cart(self):
        sum = 0
        for (product, quantity) in zip(self.products, self.quantities):
            sum += product.total_price(quantity)
        return round(sum, 2)

    def __float__(self):
        return sum


if __name__ == "__main__":
    banana = Product('banana', 7.0)
    beer = Product('beer', 5.5)
    meat = Product('meat', 50.6)
    bread = Product('bread', 12.1)
    print(banana.total_price(7))
    cart_4 = ShoppingCart()
    cart_1 = ShoppingCart()
    cart_4.add_product(Product('beer', 7), 3)
    cart_4.add_product(Product('banana', 4), 8)
    cart_4.add_product(Product('banana', 4), 8)
    print(cart_4.total_price_cart())
    print(banana)
    cart_2 = ShoppingCart()
    cart_2.add_product(banana, 1)
    cart_2.add_product(meat, 7)
    cart_1.add_product(bread, 2)
    cart_1.add_product(beer, 10)
    print(cart_1.total_price_cart())
    # print(cart_1.products)

    cart_3 = ShoppingCart()
    cart_3.add_product(banana, 1)
    cart_3.add_product(banana, 1)
    cart_3.add_product(banana, 1)
    cart_3.add_product(meat, 7)
    print(cart_2.total_price_cart())
    cart_total = cart_1 + cart_2
    print(cart_total.total_price_cart())

    print(cart_3.total_price_cart())
