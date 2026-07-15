from datetime import datetime


class Order:
    def __init__(self, id, items, total, payment_method, status="completed"):
        self.id = id
        self.items = items
        self.total = total
        self.payment_method = payment_method
        self.status = status
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "items": self.items,
            "total": self.total,
            "payment_method": self.payment_method,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        order = cls(
            id=data["id"],
            items=data["items"],
            total=data["total"],
            payment_method=data["payment_method"],
            status=data.get("status", "completed"),
        )
        order.created_at = data.get("created_at", order.created_at)
        return order
