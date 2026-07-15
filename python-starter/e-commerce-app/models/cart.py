class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove(self, product_id):
        self.items = [item for item in self.items if item.product.id != product_id]

    def total(self):
        return sum(item.subtotal() for item in self.items)

    def clear(self):
        self.items = []
