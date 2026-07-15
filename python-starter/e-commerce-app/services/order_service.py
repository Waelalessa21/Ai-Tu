import uuid
from models.order import Order


class OrderService:
    def __init__(self, storage):
        self.storage = storage

    def create_order(self, cart, payment_method):
        if not cart.items:
            return None

        items = [
            {
                "product_id": item.product.id,
                "name": item.product.name,
                "quantity": item.quantity,
                "price": item.product.price,
            }
            for item in cart.items
        ]

        order = Order(
            id=str(uuid.uuid4())[:8],
            items=items,
            total=cart.total(),
            payment_method=payment_method.__class__.__name__,
        )

        if not payment_method.pay(order.total):
            return None

        self.storage.create(order.to_dict())
        cart.clear()
        return order

    def get_all(self):
        return [Order.from_dict(item) for item in self.storage.get_all()]
